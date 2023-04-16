metadata = {
    'protocolName': 'Immunostaining of hMSC cells for lysosomes',
    'author': 'Your Name Here',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes.',
    'apiLevel': '2.10'
}

from opentrons import protocol_api

# create protocol
protocol = protocol_api.ProtocolContext()

# define labware
plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

tiprack_1 = protocol.load_labware('opentrons_96_tiprack_10ul', '2')
tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

# define pipettes
p10_single = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_1])
p300_single = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])

# define reagents
wash_buffer = plate.rows()[0][0]
blocking_buffer = plate.rows()[0][1]
primary_antibody = plate.rows()[0][2]
secondary_antibody = plate.rows()[0][3]
mounting_medium = plate.rows()[0][4]

# perform immunostaining
def immunostaining():
    # distribute 50ul wash buffer to each well
    p300_single.pick_up_tip()
    for well in plate:
        p300_single.aspirate(50, wash_buffer)
        p300_single.dispense(50, well)
    p300_single.drop_tip()
    
    # incubate for 5 minutes
    protocol.delay(minutes=5)
    
    # remove wash buffer
    for well in plate:
        p300_single.aspirate(100, well)
        p300_single.dispense(100, protocol.fixed_trash)
    
    # distribute 100ul blocking buffer to each well
    p300_single.pick_up_tip()
    for well in plate:
        p300_single.aspirate(100, blocking_buffer)
        p300_single.dispense(100, well)
    p300_single.drop_tip()
    
    # incubate for 30 minutes
    protocol.delay(minutes=30)
    
    # remove blocking buffer
    for well in plate:
        p300_single.aspirate(100, well)
        p300_single.dispense(100, protocol.fixed_trash)
    
    # distribute 50ul primary antibody to each well
    p10_single.pick_up_tip()
    for well in plate:
        p10_single.aspirate(50, primary_antibody)
        p10_single.dispense(50, well)
    p10_single.drop_tip()
    
    # incubate for 1 hour
    protocol.delay(minutes=60)
    
    # remove primary antibody
    for well in plate:
        p300_single.aspirate(100, well)
        p300_single.dispense(100, protocol.fixed_trash)
    
    # distribute 50ul secondary antibody to each well
    p10_single.pick_up_tip()
    for well in plate:
        p10_single.aspirate(50, secondary_antibody)
        p10_single.dispense(50, well)
    p10_single.drop_tip()
    
    # incubate for 1 hour
    protocol.delay(minutes=60)
    
    # remove secondary antibody
    for well in plate:
        p300_single.aspirate(100, well)
        p300_single.dispense(100, protocol.fixed_trash)
    
    # distribute 50ul mounting medium to each well
    p10_single.pick_up_tip()
    for well in plate:
        p10_single.aspirate(50, mounting_medium)
        p10_single.dispense(50, well)
    p10_single.drop_tip()
    
    # incubate for 10 minutes
    protocol.delay(minutes=10)
    
    # remove mounting medium
    for well in plate:
        p300_single.aspirate(100, well)
        p300_single.dispense(100, protocol.fixed_trash)

immunostaining()
