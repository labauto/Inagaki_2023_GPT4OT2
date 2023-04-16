# Import required modules
from opentrons import protocol_api

# Set up the protocol based on the selected robot
metadata = {
    'protocolName': 'Immunostaining of hMSC Cells for Lysosome Labeling',
    'author': 'Your Name',
    'description': 'A protocol for preparing immunostained hMSC cells to visualize lysosomes using the Opentrons robot',
    'apiLevel': '2.0',
}
protocol = protocol_api.ProtocolContext(metadata=metadata)

# Define experiment inputs and outputs
plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
tips_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)

# Define reagents and antibodies
media = '200ul of DMEM/10% FBS'
PBS = '200ul of 1x PBS'
fixative = '200ul of 4%PFA in PBS (pH 7.4)'
Triton_X_100 = '200ul of 0.2% Triton X-100'
blocking_solution = '200ul of 10% donkey serum in PBS'
primary_antibody = '200ul of anti-Lamp1 antibody'
secondary_antibody = '200ul of fluorescent secondary antibody'

# Define the pipetting steps for the experiment
def immunostaining():
    # Add fixative and incubate
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(fixative, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '5 minutes')

    # Wash cells with PBS
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(PBS, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '5 minutes')

    # Fix and permeabilize cells with Triton X-100
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(Triton_X_100, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '15 minutes')

    # Wash cells with PBS
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(PBS, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '5 minutes')

    # Block cells with blocking solution
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(blocking_solution, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '30 minutes')

    # Incubate cells with primary antibody
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(primary_antibody, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '60 minutes')

    # Wash cells with PBS
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(PBS, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '5 minutes')

    # Incubate cells with secondary antibody
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(secondary_antibody, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
    protocol.incubate(plate, 'room temperature', '60 minutes')

    # Wash cells with PBS
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(PBS, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()

    # Add media to each well
    for well in plate.wells():
        pipette = protocol.pick_up_tip(tips_300.wells()[0])
        pipette.aspirate(media, rate=0.15)
        pipette.dispense(well.bottom(2))
        pipette.drop_tip()
  
    protocol.comment('Immunostaining of hMSC cells for lysosome labeling is complete!')
    
# Call function
immunostaining()
