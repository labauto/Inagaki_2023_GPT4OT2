from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware and pipettes
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    falcon_tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    pipette_p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Set reagents location
    pbs = falcon_tuberack.wells_by_name()['A1']
    trypsin = falcon_tuberack.wells_by_name()['B1']
    dmem = falcon_tuberack.wells_by_name()['C1']

    # Protocol Steps
    # Step 1: Wash the 6 well plate with 5 cycles of 1mL PBS(-)
    for well in plate_6_well.wells():
        pipette_p1000.pick_up_tip()
        for i in range(5):
            pipette_p1000.aspirate(1000, pbs)
            pipette_p1000.dispense(1000, well)
        pipette_p1000.drop_tip()

    # Step 2: Add 1mL trypsin solution (0.25%) to each well and wait for 5 minutes
    for well in plate_6_well.wells():
        pipette_p1000.transfer(1000, trypsin, well)
         
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in plate_6_well.wells():
        pipette_p1000.transfer(1000, dmem, well)
    
    # Step 4: Finish the experiment
    protocol.comment('Experiment completed!')
