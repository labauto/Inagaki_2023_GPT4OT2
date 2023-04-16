# Import necessary modules
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Viability and Cytotoxicity of A549 Cells with Thapsigargin',
    'author': 'Your Name',
    'description': 'Opentrons protocol for measuring viability and cytotoxicity of A549 cells treated with Thapsigargin',
    'apiLevel': '2.11'
}

# Define function to run protocol
def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    snapcap_tube_rack = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '6')
    plate_96_well_treated = protocol.load_labware('corning_96_wellplate_360ul_flat', '9')

    # Define pipettes
    pipette50 = protocol.load_instrument('p50_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_20ul', '10')])

    # Define reagent volume variables
    cytotox_vol = 15
    viab_vol = 80

    # Define reagents
    cytotox_reagent = snapcap_tube_rack['B2']
    viab_reagent = snapcap_tube_rack['B1']

    # Define negative control wells
    neg_ctrl = plate_96_well.rows_by_name()['A'][4:7]

    # Define drug dilution tubes
    drug_dilutions = snapcap_tube_rack.rows_by_name()['C'][0:6] + snapcap_tube_rack.rows_by_name()['D'][0:6]

    # Define drug concentration variables
    drug_1x_conc = 1
    dilution_conc = 4

    # Define drug concentration dictionary
    drug_conc_dict = {
        'A1': 1000,
        'A2': 100,
        'A3': 10,
        'A4': 1,
        'A5': 0.1,
        'A6': 0.05,
        'B1': 0.01,
        'B2': 0.02,
        'B3': 0.04,
        'B4': 0.08,
        'B5': 0.16,
        'B6': 0.2
        }

    # Define drug dilution
    for i, well in enumerate(drug_dilutions):
        if i == 0:
            pipette50.transfer(35, snapcap_tube_rack['A1'], well.top(), new_tip='always')
        else:
            pipette50.transfer(35, snapcap_tube_rack.rows_by_name()['A'][i], well.top(), new_tip='always')
        mix_loc = well.bottom().move(types.Point(x=0, y=0, z=-2))
        pipette50.mix(3, 35, mix_loc)
        pipette50.aspirate(35, well).dispense(35, mix_loc)

    # Define drug working concentration
    for key, value in drug_conc_dict.items():
        source = drug_dilutions[int(key[1])-1]
        dest = [x for x in plate_96_well.columns_by_name()[key[0]] if x.index == int(key[1])][0]
        if value == drug_1x_conc:
            pipette50.transfer(20, source.bottom(2), dest.bottom(2), mix_after=(2,20))
        else:
            dilution_factor = int(value/dilution_conc)
            for _ in range(dilution_factor):
                pipette50.mix(3, dilution_conc, source.bottom(2))
                pipette50.transfer(dilution_conc, source.bottom(2), source.bottom(6))
            pipette50.transfer(20, source.bottom(6), dest.bottom(2), mix_after=(2,20))

    # Perform seeding
    pipette50


:*************************


