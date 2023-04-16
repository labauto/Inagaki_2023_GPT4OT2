# Import Opentrons modules
from opentrons import protocol_api

# Create a protocol object
metadata = {
    'protocolName': 'Immunostained hMSC cells to visualize E-Cadherin',
    'author': 'Your Name',
    'description': 'Prepare immunostained hMSC cells to visualize E-Cadherin',
    'apiLevel': '2.10'
}

# Set up protocol using customized created function
def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    # Load tip rack and pipettes
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_10ul', '2')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    p10 = protocol.load_instrument('p10_single', 'left', tip_racks=[tiprack_1])
    p300 = protocol.load_instrument('p300_multi', 'right', tip_racks=[tiprack_2])

    # Define reagents
    antibody = plate['A1']
    blocking_buffer = plate['B1']
    wash_buffer = plate['C1']
    secondary_antibody = plate['D1']

    # Define cells
    cells = [well for well in plate.rows()[0][2:]]

    # Perform immunostaining
    p300.transfer(300, blocking_buffer, cells, new_tip='once')
    p300.transfer(300, wash_buffer, cells, new_tip='once')
    p10.pick_up_tip()
    for cell in cells:
        p10.transfer(2, antibody, cell, mix_after=(3, 10), new_tip='never')
        p10.transfer(8, wash_buffer, cell, mix_after=(3, 10), new_tip='never')
        p10.transfer(2, secondary_antibody, cell, mix_after=(3, 10), new_tip='never')
        p10.transfer(8, wash_buffer, cell, mix_after=(3, 10), new_tip='never')
        p10.transfer(10, wash_buffer, cell, mix_after=(3, 10), new_tip='never')
    p10.drop_tip()
