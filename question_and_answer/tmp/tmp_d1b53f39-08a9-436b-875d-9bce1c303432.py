from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Viability and Cytotoxicity Measurement',
    'author': 'Your Name Here',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line',
    'apiLevel': '2.10'
}

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    plate = protocol.load_labware('96_well_plate', '1')
    tiprack_200 = [
        protocol.load_labware('opentrons_96_tiprack_200ul', str(slot))
        for slot in range(2, 7)
    ]
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '7')
    res_tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '8')

    # Load instruments
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=tiprack_200)
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])
    
    # Add cells to plate
    cell_count = int(input('Enter cell count: '))
    cell_vol = 60 # microliters
    cell_conc = cell_count / cell_vol
    if cell_conc > 1.2e6:
        raise ValueError('Cell concentration too high')
    
    p300.pick_up_tip()
    for well in plate.wells():
        p300.transfer(cell_vol, cell_conc * 10, well.top(2), new_tip='never')
    p300.drop_tip()

    # Add drug solutions to plate
    drug_concs = {
        'A1': 1e-3,
        'A2': 1e-4,
        'A3': 1e-5,
        'A4': 1e-6,
        'A5': 1e-7,
        'A6': 5e-8,
        'B1': 1e-8
    }

    drug_concentrations = {
        'C1': 1.56e-9,
        'C2': 3.12e-9,
        'C3': 6.24e-9,
        'C4': 1.252e-8,
        'C5': 2.5e-8,
        'C6': 5e-8,
        'D1': 1e-8,
        'D2': 2e-8,
        'D3': 4e-8,
        'D4': 8e-8,
        'D5': 1.6e-7,
        'D6': 2e-7
    }
    
    # Add negative control
    p300.pick_up_tip()
    for well in plate.rows()[0][:3]:
        p300.transfer(100, res_tube_rack.wells_by_name()['A5'].bottom(3), well.top(2), new_tip='never')
    p300.drop_tip()

    # Add drug solutions, perform dilutions and add to plate
    for diluent_well, stock, dilutions in zip(plate.rows()[0][4:], drug_concs.items(), drug_concentrations.items()):
        drug_well = res_tube_rack.wells_by_name()[stock[0]]
        p20.transfer(35, drug_well.bottom(1), drug_well.bottom(3), new_tip='always')

        for dilution, next_dilution in zip(dilutions[1:], dilutions[1:][1:]+['']):
            dilution_well = res_tube_rack.wells_by_name()[dilution[0]]
           


:*************************


