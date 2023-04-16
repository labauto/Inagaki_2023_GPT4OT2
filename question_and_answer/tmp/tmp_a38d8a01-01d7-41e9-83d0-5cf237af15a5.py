metadata = {
    'protocolName': 'Immunostained iPS cells',
    'author': 'Your name here',
    'description': 'Preparing immunostained iPS cells to visualize lysosomes',
    'apiLevel': '2.10'
}

def run(imaging_cycle: int = 3):
    
    # module import
    from opentrons import protocol_api 
    from opentrons.types import Point
    
    # api instantiation
    protocol = protocol_api.ProtocolContext()
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 4)
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])

    # reagents
    buffer = plate[1]
    primary_antibody = plate[2]
    secondary_antibody = plate[3]
    stain = plate[4]
    
    # distribute buffer
    p20.distribute(10, buffer, [well.top() for well in plate.rows()[0]], disposal_volume=2)
    
    # perform washing step
    for cycle in range(imaging_cycle):
        protocol.comment(f'Performing washing cycle #{cycle+1}')
        wash_wells = plate.rows()[0][1:3]
        p20.transfer(10, wash_wells[0], wash_wells[1], new_tip='always', disposal_volume=2)
        p20.transfer(10, wash_wells[1], wash_wells[0], new_tip='always', disposal_volume=2)
    
    # perform blocking
    protocol.comment('Adding primary antibody')
    p20.transfer(5, primary_antibody, plate.rows()[0][0], new_tip='always', disposal_volume=2)
    
    p20.transfer(5, buffer, plate.rows()[0][0], mix_before=(5,2), new_tip='always', disposal_volume=2)
    protocol.comment('Adding secondary antibody')
    p20.transfer(5, secondary_antibody, plate.rows()[0][0], new_tip='always', disposal_volume=2)
    
    p20.transfer(5, buffer, plate.rows()[0][0], mix_before=(5,2), new_tip='always', disposal_volume=2)
    protocol.comment('Adding lysosome stain')
    p20.transfer(5, stain, plate.rows()[0][0], new_tip='always', disposal_volume=2)

run()
