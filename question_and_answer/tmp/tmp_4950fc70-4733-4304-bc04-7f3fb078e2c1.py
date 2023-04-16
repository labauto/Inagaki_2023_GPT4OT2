from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Assistant',
    'description': 'Automated medium exchange using Opentrons',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware and Pipettes
    def setup():

        plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
        pbs_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 2)['A1']
        dmem_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 2)['B1']
        tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)

        pipette = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack])

        return plate, pbs_tube, dmem_tube, pipette

    # Remove cell culture medium
    def remove_old_medium(plate, pipette):
        for well in plate.wells():
            pipette.pick_up_tip()
            pipette.transfer(2000, well, well, new_tip='never')
            pipette.drop_tip()

    # Add PBS(-) to wash cells
    def wash_cells(plate, pbs_tube, pipette):
        for well in plate.wells():
            pipette.pick_up_tip()
            pipette.transfer(2000, pbs_tube, well, new_tip='never')
            pipette.drop_tip()

    # Add D-MEM
    def add_dmem(plate, dmem_tube, pipette):
        for well in plate.wells():
            pipette.pick_up_tip()
            pipette.transfer(2000, dmem_tube, well, new_tip='never')
            pipette.drop_tip()

    # Main function
    plate, pbs_tube, dmem_tube, pipette = setup()
    remove_old_medium(plate, pipette)
    wash_cells(plate, pbs_tube, pipette)
    add_dmem(plate, dmem_tube, pipette)
