from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC spheroid culture',
    'author': 'Your name here!',
    'description': 'A protocol to culture hMSC spheroids',
    'apiLevel': '2.0'
}

# Define the run function
def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    plate_96_osminus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_96_osplus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    trough = protocol.load_labware('usascientific_12_reservoir_22ml', '3')

    # Load pipettes
    pipette_200 = protocol.load_instrument('p300_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '4')])

    # Define functions to transfer liquids
    def transfer_dmem_osminus(volume, dest):
        pipette_200.transfer(volume, trough['A1'].bottom(4), dest)

    def transfer_dmem_osplus(volume, dest):
        pipette_200.transfer(volume, trough['A2'].bottom(4), dest)

    def transfer_supplements(volume, dest):
        pipette_200.pick_up_tip()
        pipette_200.aspirate(volume, trough['A3'].bottom(4))
        pipette_200.dispense(volume, dest)
        pipette_200.mix(3, volume, dest)
        pipette_200.drop_tip()

    def transfer_cells(volume, dest):
        pipette_200.transfer(volume, trough['A4'].bottom(4), dest)

    # Transfer DMEM to wells in 96 well plates (OS- and OS+)
    wells_osminus = plate_96_osminus.rows()[0]
    wells_osplus = plate_96_osplus.rows()[0]
    for well in wells_osminus:
        transfer_dmem_osminus(100, well)
    for well in wells_osplus:
        transfer_dmem_osplus(100, well)

    # Add supplements to wells in the OS+ plate
    for well in wells_osplus:
        transfer_supplements(2, well)

    # Transfer cells to both plates
    for well in wells_osminus:
        transfer_cells(100, well)
    for well in wells_osplus:
        transfer_cells(100, well)

    # Done!
    protocol.comment('Protocol complete.')

