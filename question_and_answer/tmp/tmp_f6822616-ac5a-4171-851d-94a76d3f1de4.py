from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Protocol',
    'author': 'Your Name',
    'description': 'Automated protocol for washing, trypsinization and media change in 96-well plate',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    
    # Load pipettes
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '3')])
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '6')])
    
    # Define reagents
    pbs = tuberack['A1']
    trypsin = tuberack['A2']
    dmem = tuberack['A3']
    
    # Define functions
    def wash_well(well):
        for _ in range(5):
            p300.pick_up_tip()
            p300.aspirate(100, pbs)
            p300.dispense(100, well)
            p300.blow_out()
            p300.drop_tip()

    # Define protocol steps
    # Step 1: Wash wells with PBS
    for row in plate.rows():
        for well in row:
            wash_well(well)
    
    # Step 2: Add trypsin to wells and wait 5 minutes
    p1000.pick_up_tip()
    for row in plate.rows():
        for well in row:
            p1000.aspirate(100, trypsin)
            p1000.dispense(100, well)
    p1000.drop_tip()
    protocol.delay(minutes=5)
    
    # Step 3: Add DMEM to wells
    for row in plate.rows():
        for well in row:
            p300.pick_up_tip()
            p300.aspirate(300, dmem)
            p300.dispense(300, well)
            p300.blow_out()
            p300.drop_tip()
    
    # Step 4: Finish the experiment
    protocol.comment('Experiment is finished')
