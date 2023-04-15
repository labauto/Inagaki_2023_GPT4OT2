import datetime
import glob
import os
import shutil
import subprocess
import uuid
from typing import (Any, Callable, Dict, Generic, List, Optional, Set, Tuple,
                    Type, TypeVar, Union, cast, overload)

import openai
import pandas as pd
import tiktoken

from config import OPENAI_TOKEN, STOP_PROMPT

openai.api_key = OPENAI_TOKEN


def extract_markdown_code_blocks(text: List[str]):
    """Extracts markdown python code blocks from txt file"""

    code_blocks = []
    in_code_block = False
    for line in text:
        if line.startswith("```python"):
            in_code_block = True
            code_block = []
        elif line.startswith("```"):
            in_code_block = False
        elif in_code_block:
            code_blocks.append(line)
    return code_blocks


def prepare_python_script(file_path: str) -> Union[str, None]:
    """prepare python script from generated answer by GPT-3"""
    SEPARATOR = "answer:*************************\n"

    # remove the last line
    text = open(file_path, "r").readlines()
    # get text after SEPARATOR
    indices = [i for i, x in enumerate(text) if x == SEPARATOR]
    # if separated section is more than two, remove the last one
    # e.g.
    # aaaaa
    # bbbbb
    # answer:*************************
    # ccccc
    # ddddd
    # answer:*************************
    # eeeee
    # fffff
    #
    # then, get the text after the first separator and remove the last one
    if len(indices) > 1:
        text = text[indices[0] + 1 : indices[-1]]
    else:
        text = text[indices[0] + 1 :]

    # if there's markdown code notation, extract the code
    # e.g.
    # ```python
    # aaaaa
    # bbbbb
    # ```
    # then, get the text between ```python and ```
    if any("```python" in s for s in text):
        text = extract_markdown_code_blocks(text)

    if len(text) == 0:
        return None

    # save it as an tmp python script
    tmp_file_path = f"./question_and_answer/tmp/tmp_{uuid.uuid4()}.py"
    if not os.path.exists("./question_and_answer/tmp"):
        os.makedirs("./question_and_answer/tmp")
    with open(tmp_file_path, "w") as f:
        f.writelines(text)
    return tmp_file_path


def run_opentrons_simulate(protocol_file: str, output_filename: str) -> Tuple[str, str, str]:
    """
    run opentrons_simulate in the terminal and get the stdout
    and save it to a file
    """
    cmd = "opentrons_simulate " + protocol_file

    output_dir = "./question_and_answer/eval/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = output_dir + output_filename

    result_type = ""
    with open(output_path, "w") as f:
        print(f"run subprocess, cmd: {cmd}")
        stdout = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(stdout)
        output_text = ""
        if stdout.returncode != 0:
            output_text += stdout.stderr
            f.write(stdout.stderr)
            result_type = "error"
            return output_path, output_text, result_type
        # ok
        else:
            output_text += stdout.stdout
            f.write(stdout.stdout)
            result_type = "ok"
            return output_path, output_text, result_type


def extract_chat_loop_result_from_filename(filename: str) -> str:
    """
    extract the latest chat loop result from filename, the format is here:
        filename = "chat_loop_{count}_{uuid.uuid4()}_gpt-4_XXXX.txt"

    for given filename, return the model name as f'gpt-4_{count}'
    """
    # extract the count
    count = filename.split("_")[2]
    # extract the model name
    if "gpt-4" in filename:
        model = "gpt-4"
    elif "gpt-3.5-turbo" in filename:
        model = "gpt-3.5-turbo"
    return f"{model}_{count}"


def check_filename_extract_model_info(filename: str) -> Tuple[str, bool, str]:
    """
    extract information from filename defined by @takaria0 in `save_prompt_and_answer_with_modelname` function
    """
    # filename = f"question_and_answer/{prefix}_{modelname}_token_{max_tokens}_temperature_{temperature}_{current_datetime}_prompt_{prompt_ver}.txt"

    if "finetuned" in filename:
        finetuned = True
    else:
        finetuned = False

    # extract prompt_ver
    if "prompt" in filename:
        # include v1 and v1.1 (dot)
        # filename = f"question_and_answer/{prefix}_{modelname}_token_{max_tokens}_temperature_{temperature}_{current_datetime}_prompt_v4.1.txt"
        prompt_ver = filename.split("_")[-1].split(".txt")[0]
    else:
        prompt_ver = "v1"

    # extract chat loop case
    if "chat_loop" in filename:
        return extract_chat_loop_result_from_filename(filename), finetuned, prompt_ver

    # extract model name
    model_list = ["ada", "code-davinci-002", "finetuned-davinci", "text-davinci-003", "chatgpt", "gpt-3.5-turbo", "gpt-4"]
    for model in model_list:
        if model in filename:
            return model, finetuned, prompt_ver

    return "", False, "v1"


def decode_to_python_script(res) -> List[str]:
    return [val.text for val in res.choices]


def save_prompt_and_answer_with_modelname(prefix, prompt, answer, modelname, temperature, max_tokens, prompt_ver: str = "v1") -> str:
    """
    Save GPT prompt and answer to a file with a separator so that we can extract the text and model info later
    """
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"question_and_answer/{prefix}_{modelname}_token_{max_tokens}_temperature_{temperature}_{current_datetime}_prompt_{prompt_ver}.txt"
    with open(filename, "w") as f:
        # write as txt
        f.write(f"prompt:*************************\n {prompt}\n")
        f.write(f"answer:*************************\n")
        if isinstance(answer, list):
            for ans in answer:
                f.write(f"{ans}\n\n\n:*************************\n\n\n")
        else:
            f.write(f"{answer}\n\n\n:*************************\n\n\n")
        return filename


def init_df_eval(dataset_path: str) -> pd.DataFrame:
    """
    Initialize the dataframe for evaluation
    Basically, store all the filepaths in the dataset.

    This will be then used to run opentrons_simulate and get the validation results.
    After that, we can use the dataframe to do the analysis and visualization.
    """

    files = glob.glob(dataset_path + "/*.txt")
    sorted_files = sorted(files, key=os.path.getmtime)
    df_eval = pd.DataFrame()
    for file in sorted_files:
        # Note that these are just default values and will be updated
        df_eval = df_eval.append(
            {
                "model": "",
                "finetuned": False,
                "prompt_ver": "v1",
                "opentrons_simulate_result": "",
                "opentrons_simulate_result_last_line": "",
                "opentrons_simulate_result_raw_text": "",
                "opentrons_simulate_result_file_path": "",
                "prompt_answer_file_path": file,
                "python_script_file_path": "",
            },
            ignore_index=True,
        )
    return df_eval
