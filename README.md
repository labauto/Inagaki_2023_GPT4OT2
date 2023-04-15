# LabCode

The official source code for calling OpenAP API and validating the generated Python scripts used in "**_GPT-4 generates robotic scripts from goal-oriented instructions in biological laboratory automation_**".

## Description

- Experimenting GPT capability on Laboratory Automation.
- The core of the repository is the conversational text data stored in `/question_and_answer/*.txt`.
  - Then, with `evaluate.ipynb`, you can create plots & tables.
  - If you would like to add more conversational data, try running `call_multiple_model.py` and the new conversations will be saved at `/question_and_answer/*.txt`.

## Folder structure

### Scripts

- `config.py`
  - Prompts are defined here.
- `call_multiple_model.py`
  - Open and edit `prompt_ver='v1'` as you like, and run `python3 call_multiple_model.py` and it'll save new conversations with GPT to `/question_and_answer/*.txt`
- `evaluate.ipynb`
  - Run the cells in the notebook and you'll see some figures and tables in the notebook. It will run the Python scripts that are extracted from ChatGPT conversations with `opentrons_simulate` and store the result to pandas DataFrame. Then, plot the error count (or success) in bar plot. Each conversation has unique `uuid()` so that one can connect the conversations later.
- `utils.py`
  - Utility functions to evaluate conversation with GPT using `opentrons_simulate` and etc.

### Data

- `/question_and_answer/*.txt`

  - Raw conversational text between user and GPT, separated by `prompt:*************************` and `answer:*************************`

- `/question_and_answer/tmp/*.py`
  - Extracted Python scripts from ChatGPT's answer

## How to run the scripts

### Validate the generated Python scripts

1. Open `evaluate.ipynb` and run the cells from top to bottom.
2. A pandas dataframe `df_eval` will be populated with the prompts, answer, and the Python error (or success).
3. You can use the dataframe to analyze, and visualize the results.

### Add more conversational data by calling OpenAI API

1. Add your OpenAI `API_SECRET` to `config.py`
2. Install dependencies by running `pip install -r requirements.txt`
3. Add your prompts in a dictionary `PROMPT_LIST` at `config.py`.
4. Edit `main` function in `call_multiple_models.py` to specify number of api calls (`n_calls`) and prompt to use.
5. Run `python3 call_multiple_models.py` and wait for the process to finish. It might take from a few minutes to a few hours depends on `n_calls`.
