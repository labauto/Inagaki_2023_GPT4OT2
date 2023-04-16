from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Protocol',
    'author': 'Your Name',
    'description': 'A protocol for washing and trypsinizing cell cultures',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    dish = protocol.load_labware('corning_90mm_cell_culture_dish', 1)
    pbs_tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)

    # Load pipettes
    p300 = protocol.load_instrument('p300_single', 'left')
    p1000 = protocol.load_instrument('p1000_single', 'right')

    # Define locations
    pbs_well = pbs_tuberack.wells_by_name()['A1']
    trypsin_volume = 3000  # ul
    dmem_volume = 10000  # ul

    # Wash cell culture dish with PBS
    for i in range(5):
        p300.pick_up_tip()
        p300.aspirate(2000, pbs_well)
        p300.dispense(2000, dish)
        p300.mix(3, 2000, dish)
        p300.drop_tip()

    # Add trypsin solution and wait for 5 minutes
    p1000.pick_up_tip()
    p1000.aspirate(trypsin_volume, pbs_well)
    p1000.dispense(trypsin_volume, dish)
    p1000.mix(3, trypsin_volume, dish)
    protocol.delay(minutes=5)
    p1000.drop_tip()

    # Add cell culture medium
    p1000.pick_up_tip()
    p1000.aspirate(dmem_volume, pbs_well)
    p1000.dispense(dmem_volume, dish)
    p1000.mix(3, dmem_volume, dish)
    p1000.drop_tip()

    # Finish experiment
    protocol.comment('Experiment finished!')
