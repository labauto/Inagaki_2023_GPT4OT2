from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'hMSC Spheroid Culture',
    'author': 'Your Name Here',
    'description': 'This protocol automates the culture of hMSC spheroids',
    'apiLevel': '2.2'
}

# set up the deck on the robot
def deck_setup(protocol):
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', '2')
    plate_96_osminus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    plate_96_osplus = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')
    trough = protocol.load_labware('nest_12_reservoir_15ml', '5')

    return tiprack_200, tiprack_10, plate_96_osminus, plate_96_osplus, trough

# transfer DMEM to each well of the OS- plate
def transfer_dmem_osminus(protocol, plate, pipette):

    for row in plate.rows():
        pipette.transfer(100, trough['A1'], row, new_tip='always')


# transfer DMEM high glucose and supplements to each well of the OS+ plate
def transfer_media_osplus(protocol, plate, pipette):

    dexam = trough['A2']
    ascor = trough['A3']
    bgp = trough['A4']

    for row in plate.rows():
        pipette.transfer(100, trough['A1'], row, new_tip='always') # DMEM High Glucose
        pipette.transfer(0.1, dexam, row, new_tip='always') # Dexamethasone
        pipette.transfer(1, ascor, row, new_tip='always') # Ascorbic acid
        pipette.transfer(1, bgp, row, new_tip='always') # beta-Glycerophosphate


# transfer hMSC cells to each well of the plates
def transfer_cells(protocol, plate_osminus, plate_osplus, pipette):

    cell_plate = protocol.load_labware('corning_6_wellplate_16.32ml_flat', '6')

    cell_well = cell_plate['A1']
    for row_osminus, row_osplus in zip(plate_osminus.rows(), plate_osplus.rows()):
        pipette.transfer(100, cell_well, row_osminus, new_tip='always')
        pipette.transfer(100, cell_well, row_osplus, new_tip='always')


# main function
def run(protocol):
    # setup deck and pipettes
    tiprack_200, tiprack_10, plate_96_osminus, plate_96_osplus, trough = deck_setup(protocol)

    pipette_200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200])
    pipette_10 = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_10])

    # transfer DMEM to each well of the OS- plate
    transfer_dmem_osminus(protocol, plate_96_osminus, pipette_200)

    # transfer DMEM high glucose and supplements to each well of the OS+ plate
    transfer_media_osplus(protocol, plate_96_osplus, pipette_200)

    # transfer hMSC cells to each well of the plates
    transfer_cells(protocol, plate_96_osminus, plate_96_osplus, pipette_10)

