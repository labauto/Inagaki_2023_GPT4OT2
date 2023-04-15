OPENAI_TOKEN = "***API_SECRET here***"

STOP_PROMPT = "\n\n###\n\n"
STOP_COMPLETION = "\nEND\n"

TOKEN_LIMIT = 2000

PROMPT_DESC = {
    "v1": "simple cell culture medium exchange",
    "v2": "simple cell culture medium exchange",

    "v2.cell2": "simple cell culture medium exchange",
    "v2.medium2": "simple cell culture medium exchange",
    "v2.cell2.medium2": "simple cell culture medium exchange",
    "v2-B": "simple cell culture medium exchange",
    "v2-B.cell2": "simple cell culture medium exchange",
    "v2-B.target2": "simple cell culture medium exchange",
    "v2-B.cell2.target2": "simple cell culture medium exchange",

    "v3": "complicated cell viability and cytotoxicity assay",
    "v4": "complicated cell viability and cytotoxicity assay",
}

PROMPT_LIST = {
    # simple cell culture medium exchange
    # long prompt
    "v1": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a script that does the following experiment?

Protocol Steps:
1. Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
2. After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
3. Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
4. Finish the experiment.

Possible Labware and Pipettes (Note that you don't need to trust these items, you can use any labware and pipette you want):
1. `opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical`
2. `p1000_single`
3. `corning_6_wellplate_16.8ml_flat`

When writing scripts, be aware of the following:
1. Do not aspirate more than pipette's max volume. For example, if you want to aspirate 2000 µL with a p1000_single, you need to split it into two commands.
2. Check the number of tips you use to avoid running out of tips.
3. when load_labware('name', slot), you can't declare the same slot twice, you need to use different slots for different labware.

{STOP_PROMPT}
""",
    # simple cell culture medium exchange
    # short prompt
    "v2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Exchanging hMSC cell culture medium using PBS(-) and D-MEM.
The cell is cultured in 6 well plate.
{STOP_PROMPT}
""",
    "v2.cell2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Exchanging iPS cell culture medium using PBS(-) and D-MEM.
The cell is cultured in 6 well plate.
{STOP_PROMPT}
    """,
    "v2.medium2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Exchanging hMSC cell culture medium using PBS(-) and SCM130.
The cell is cultured in 6 well plate.
{STOP_PROMPT}
""",
    "v2.cell2.medium2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Exchanging iPS cell culture medium using PBS(-) and SCM130.
The cell is cultured in 6 well plate.
{STOP_PROMPT}
    """,
    # cell: hMSC, iPS
    #target: lysosomes, E-Cadherin
    "v2-B": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Prepare immunostained hMSC cells to visualize lysosomes.
The cell is cultured in 6 well plate.
    """,
    "v2-B.cell2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Prepare immunostained iPS cells to visualize lysosomes.
The cell is cultured in 6 well plate.
    """,
    "v2-B.target2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Prepare immunostained hMSC cells to visualize E-Cadherin.
The cell is cultured in 6 well plate.
    """,
    "v2-B.cell2.target2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Prepare immunostained iPS cells to visualize E-Cadherin.
The cell is cultured in 6 well plate.
    """,
    # complicated cell viability and cytotoxicity assay
    # long prompt
    "v3": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin Seeding A549 cells and addition of various concentrations of Thapsigargin on the second day after the cells have adhered to the 96 well TC plate. On the first day of plating and the second day when the drug additions are to take place, follow the steps below- Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter at low fan speed for about an hour before seeding the cells on 96 well plate. Continue to keep the HEPA filter turned on during the duration of setting up the robot with the respective labware, dilutions of the drug (thapsigargin)on the second day and addition of the drug on to the 96 well plate

1. Take a 24–48 hours old T-75 flask of A549 cells. Take a cell count using the automated Countess 3 machine (Thermofisher Scientific) after treating the cells with Tryple Express enzyme and dislodging the adherent cells.

2. 8000 cells are to be seeded in each well of the 96 well plate. Adjust the cell volume in 10% Ham’s F12K medium in such a way that 60 microL of cells contain the cell number mentioned above.

3. The cell suspension was then dispensed in ten 1.5mL snap-capped tubes and placed in Slot 6 in the tube rack(225microL).

4. The medium was added in wells A5 to C5 as negative control

5. On the second day, roughly after 12 to 16 hours of seeding, the drug dilutions and additions are completed.

6. The first tube A1 in Slot 7 contains 35microL of 1mM Thapsigargin.

7. Next, prepare dilutions of various concentrations of thapsigargin in 10% Ham’s F12K medium (4X concentrations) after preparing the initial stocks ranging from 10nM to 100microM. The molar concentrations of stocks in tubes in positions are - A1 1mM, A2 100microM, A3 10microM, A4 1microM, A5 100nM, A6 50nM and B1 10nM.

8. The 4X concentrations of thapsigargin are prepared in tubes C1 to C6 and D1 to D6 with the following concentrations in the tubes C1 1.56nM, C2 3.12nM, C3 6.24nM, C4 12.52nM, C5 25nM, C6 50nM, D1 100nM, D2 200nM, D3 400nM, D4 800nM D5 1600nM and D6 2000nM

9. For both the initial stocks and the 4X working concentrations, the Ham’s F12 K diluent in added to respective tubes. Then the thapsigargin is added to the tubes and for each dilution, the mix is first pipetted 3-4 times before aspirating the required volume of thapsigargin and transferring to the next adjacent tube to get the required concentration. Once the 4X concentrations are prepared, prepare 2X concentrations of the drug. First, 100microL of medium is added to tubes C1, C3, C5 and D1 to D6 in Slot 6. Next 100microL of 4X concentration of thapsigargin is transferred from tubes in Slot7 to tubes in Slot 6 to result in 2X concentration. For each concentration, mix the drug several times by aspirating and dispensing in the same tube. Add the equal volume of 2X thapsigargin to each well of 96 well plate in triplicate for one concentration in which cells are seeded. This will result in 1X concentration of the drug used for the study. Continue adding column-wise the increasing concentrations of thapsigargin. Namely A1, B1, C1 of 96 well plate contains control cells. D1, E1 and F1 contains 0.39nM concentration of thapsigargin treated cells. The wells in D4, E4 and F4 contains cells with 500nM thapsigargin concentration. The wells from A5 to C5 contain medium without any cells (medium control). After 72 hours of drug treatment, carry out the following steps.

10. Pick up 20microL tip from Slot 10. Transfer 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack with Falcon 4X50 mL, 6X15mL Conical-Rack to A1 of 96 well plate placed on the Heater Shaker. Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4, A5 to C5.

11. After the addition of the reagent, set the Heater Shaker to orbital shaking for 2 minutes at 500 rpm.

12. After the orbital shaking of the heater shaker is complete, incubate the plate at RT for 15 min.

13. Remove the plate from the heater shaker and read the fluorescence at 485 nm excitation and 520 nm emission using the Biotek microplate reader.

14. Place the plate back on the heater shaker and start with additions for the cell viability assay.

15. Pick up 200microL tip from Slot 4. Aspirate 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube rack and dispense it into A1 well of the 96 well white TC plate on Heater Shaker module. Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4 and A5 to C5.

16. Once the reagent addition is complete, set the Heater shaker to orbital shaking at 500 rpm for 2 minutes. Incubate at RT for 10 minutes.

17. Remove the plate from heater shaker and read the plate for luminescence using the Biotek microplate reader.

{STOP_PROMPT}
    """,
    "v4": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

We are cultureing hMSC cells (2,500 cells/100 µl) with DMEM in 6 well plates, and we want to make hMSC spheroids (2,500 cells) in 96 well plates with two different conditions, 1) With osteoinduction supplements (OS+) and 2) Without osteoinduction supplements (OS-). For osteoinduction supplements, we use Dexamethasone, Ascorbic acid, and beta-glycerophosphate.


For OS(-)
- use 100 µl medium (DMEM) each well
For OS(+)
- use 100 µl medium (DMEM high glucose) each well and add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well.

Write a Python script that does the following:
- Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
- Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
- Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
- Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
- Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
- End

{STOP_PROMPT}
    """,
    "v1.1": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a script that does the following experiment?

Protocol Steps:
1. Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
2. After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
3. Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
4. Finish the experiment.

Possible Labware and Pipettes (Note that you don't need to trust these items, you can use any labware and pipette you want):
1. `opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical`
2. `p1000_single`
3. `corning_6_wellplate_16.8ml_flat`

When writing scripts, be aware of the following:
1. Do not aspirate more than pipette's max volume. For example, if you want to aspirate 2000 µL with a p1000_single, you need to split it into two commands.
2. Check the number of tips you use to avoid running out of tips.
3. when load_labware('name', slot), you can't declare the same slot twice, you need to use different slots for different labware.

Make sure that if the code is long, split the code into multiple tiny functions and use it later in the main function. Ideally, split the experiment into multiple steps, and for each step, write a function that does the step. And then, call the function in the main function.

{STOP_PROMPT}
""",
    #
    "v2.1": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Exchanging hMSC cell culture medium using PBS(-) and D-MEM.
The cell is cultured in 6 well plate.

Make sure that if the code is long, split the code into multiple tiny functions and use it later in the main function. Ideally, split the experiment into multiple steps, and for each step, write a function that does the step. And then, call the function in the main function.
{STOP_PROMPT}
""",
    "v3.1": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin Seeding A549 cells and addition of various concentrations of Thapsigargin on the second day after the cells have adhered to the 96 well TC plate. On the first day of plating and the second day when the drug additions are to take place, follow the steps below- Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter at low fan speed for about an hour before seeding the cells on 96 well plate. Continue to keep the HEPA filter turned on during the duration of setting up the robot with the respective labware, dilutions of the drug (thapsigargin)on the second day and addition of the drug on to the 96 well plate

1. Take a 24–48 hours old T-75 flask of A549 cells. Take a cell count using the automated Countess 3 machine (Thermofisher Scientific) after treating the cells with Tryple Express enzyme and dislodging the adherent cells.

2. 8000 cells are to be seeded in each well of the 96 well plate. Adjust the cell volume in 10% Ham’s F12K medium in such a way that 60 microL of cells contain the cell number mentioned above.

3. The cell suspension was then dispensed in ten 1.5mL snap-capped tubes and placed in Slot 6 in the tube rack(225microL).

4. The medium was added in wells A5 to C5 as negative control

5. On the second day, roughly after 12 to 16 hours of seeding, the drug dilutions and additions are completed.

6. The first tube A1 in Slot 7 contains 35microL of 1mM Thapsigargin.

7. Next, prepare dilutions of various concentrations of thapsigargin in 10% Ham’s F12K medium (4X concentrations) after preparing the initial stocks ranging from 10nM to 100microM. The molar concentrations of stocks in tubes in positions are - A1 1mM, A2 100microM, A3 10microM, A4 1microM, A5 100nM, A6 50nM and B1 10nM.

8. The 4X concentrations of thapsigargin are prepared in tubes C1 to C6 and D1 to D6 with the following concentrations in the tubes C1 1.56nM, C2 3.12nM, C3 6.24nM, C4 12.52nM, C5 25nM, C6 50nM, D1 100nM, D2 200nM, D3 400nM, D4 800nM D5 1600nM and D6 2000nM

9. For both the initial stocks and the 4X working concentrations, the Ham’s F12 K diluent in added to respective tubes. Then the thapsigargin is added to the tubes and for each dilution, the mix is first pipetted 3-4 times before aspirating the required volume of thapsigargin and transferring to the next adjacent tube to get the required concentration. Once the 4X concentrations are prepared, prepare 2X concentrations of the drug. First, 100microL of medium is added to tubes C1, C3, C5 and D1 to D6 in Slot 6. Next 100microL of 4X concentration of thapsigargin is transferred from tubes in Slot7 to tubes in Slot 6 to result in 2X concentration. For each concentration, mix the drug several times by aspirating and dispensing in the same tube. Add the equal volume of 2X thapsigargin to each well of 96 well plate in triplicate for one concentration in which cells are seeded. This will result in 1X concentration of the drug used for the study. Continue adding column-wise the increasing concentrations of thapsigargin. Namely A1, B1, C1 of 96 well plate contains control cells. D1, E1 and F1 contains 0.39nM concentration of thapsigargin treated cells. The wells in D4, E4 and F4 contains cells with 500nM thapsigargin concentration. The wells from A5 to C5 contain medium without any cells (medium control). After 72 hours of drug treatment, carry out the following steps.

10. Pick up 20microL tip from Slot 10. Transfer 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack with Falcon 4X50 mL, 6X15mL Conical-Rack to A1 of 96 well plate placed on the Heater Shaker. Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4, A5 to C5.

11. After the addition of the reagent, set the Heater Shaker to orbital shaking for 2 minutes at 500 rpm.

12. After the orbital shaking of the heater shaker is complete, incubate the plate at RT for 15 min.

13. Remove the plate from the heater shaker and read the fluorescence at 485 nm excitation and 520 nm emission using the Biotek microplate reader.

14. Place the plate back on the heater shaker and start with additions for the cell viability assay.

15. Pick up 200microL tip from Slot 4. Aspirate 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube rack and dispense it into A1 well of the 96 well white TC plate on Heater Shaker module. Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4 and A5 to C5.

16. Once the reagent addition is complete, set the Heater shaker to orbital shaking at 500 rpm for 2 minutes. Incubate at RT for 10 minutes.

17. Remove the plate from heater shaker and read the plate for luminescence using the Biotek microplate reader.

Make sure that if the code is long, split the code into multiple tiny functions and use it later in the main function. Ideally, split the experiment into multiple steps, and for each step, write a function that does the step. And then, call the function in the main function.

{STOP_PROMPT}
    """,
    "v4.1": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a Python script that does the following experiment?

We are cultureing hMSC cells (2,500 cells/100 µl) with DMEM in 6 well plates, and we want to make hMSC spheroids (2,500 cells) in 96 well plates with two different conditions, 1) With osteoinduction supplements (OS+) and 2) Without osteoinduction supplements (OS-). For osteoinduction supplements, we use Dexamethasone, Ascorbic acid, and beta-glycerophosphate.


For OS(-)
- use 100 µl medium (DMEM) each well
For OS(+)
- use 100 µl medium (DMEM high glucose) each well and add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well.

Write a Python script that does the following:
- Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
- Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
- Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
- Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
- Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
- End

Make sure that if the code is long, split the code into multiple tiny functions and use it later in the main function. Ideally, split the experiment into multiple steps, and for each step, write a function that does the step. And then, call the function in the main function.

{STOP_PROMPT}
    """,
    "v4.2": f"""
In your first answer, only answer the function names and it’s comments. Then, from next conversation, populate the logic of the function one by one.

E.g.
	User:
        Write this Python script?
	GPT:
        Here is the function names and comments
        ```python
        def step_A():
            # This function does something
            pass

        def step_B():
            # This function does something
            pass

        def step_C():
            # This function does something
            pass
        ```
	User:
        Implement the function `step_A`
	GPT:
        Here is the function `step_A`
        ```python
        def step_A(source, dest):
            pipette.transfer(100, source, dest)
        ```
    User:
        Implement the function `step_B`
    GPT:
        Here is the function `step_B`
        ```python
        def step_B(source, dest):
            pipette.transfer(100, source, dest)
        ```
    User:
        Implement the function `step_C`
    GPT:
        Here is the function `step_C`
        ```python
        def step_C(source, dest):
            pipette.transfer(100, source, dest)
        ```
    User:
        Implement the main function
    GPT:
        Here is the main function
        ```python
        def run():
            source = labware.load('opentrons-tuberack-2ml-eppendorf', '1')
            dest = labware.load('96-flat', '2')
            step_A(source, dest)
            step_B(source, dest)
            step_C(source, dest)
        ```
    User:
        Run the script



    """,
}
