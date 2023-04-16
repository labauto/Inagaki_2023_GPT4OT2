from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Cell medium exchange',
    'author': 'Your Name Here',
    'description': 'Exchanging iPS cell culture medium using PBS(-) and D-MEM in a 6 well plate',
    'apiLevel': '2.5'
}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # instruments
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])

    # reagent setup
    PBS = protocol.load_labware('nest_12_reservoir_15ml', '4')
    PBS_well = PBS['A1']
    DMEM = protocol.load_labware('nest_1_reservoir_195ml', '3')
    DMEM_well = DMEM.wells()[0]

    # define locations
    # seed your cells in well A1 of the 6 well plate with chemical # or IPSC cells
    cells = plate.wells_by_name()['A1']
   
    # Define volume of PBS and DMEM
    pbs_vol = 150
    dmem_vol = 300

    # pipette loading
    p300.pick_up_tip()

    # distribute PBS over cells
    p300.aspirate(pbs_vol, PBS_well)
    p300.dispense(pbs_vol, cells)

    # mix PBS with cells
    p300.mix(5, pbs_vol, cells)

    # remove PBS
    p300.aspirate(pbs_vol, cells)

    # distribute DMEM over cells
    p300.aspirate(dmem_vol, DMEM_well)
    p300.dispense(dmem_vol, cells)

    # mix DMEM with cells
    p300.mix(5, dmem_vol, cells)

    # remove DMEM
    p300.aspirate(dmem_vol, cells)

    p300.drop_tip()
