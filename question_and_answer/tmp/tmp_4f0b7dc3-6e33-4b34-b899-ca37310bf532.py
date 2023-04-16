
# import necessary libraries
import opentrons
from opentrons import containers, instruments

# create labware
six_well_plate = containers.create('6-well', grid=(2, 3), spacing=(20, 15), depth=15)

# create pipette
pipette = instruments.P300_Single(mount='left', tip_racks=[])

# aspirate media from well 1
pipette.aspirate(volume=300, location=six_well_plate.wells('A1'))

# transfer media to wells 2-3
pipette.distribute(volume=200, dest=six_well_plate.wells('A2', 'A3'), disposal_volume=50)

# aspirate cells from well 1 and transfer to well 2
pipette.aspirate(volume=10, location=six_well_plate.wells('A1'))
pipette.dispense(volume=10, location=six_well_plate.wells('A2'))

# aspirate media from well 2 and transfer to well 3
pipette.aspirate(volume=200, location=six_well_plate.wells('A2'))
pipette.dispense(volume=200, location=six_well_plate.wells('A3'))

# aspirate media from well 3 and transfer to 1mL tube
pipette.aspirate(volume=300, location=six_well_plate.wells('A3'))
tube = containers.create('tube-1.5ml', grid=(1,1), spacing=(20,20), depth=20)
pipette.dispense(volume=300, location=tube.wells('A1'))

# add 5µL of the lysosomal staining solution to the tube
pipette.aspirate(volume=5, location=tube.wells('A1'))
pipette.dispense(volume=5, location=tube.wells('A1'))

# mix the solution
pipette.mix(volume=10, location=tube.wells('A1'))

# aspirate the solution from the tube and transfer to well 3
pipette.aspirate(volume=10, location=tube.wells('A1'))
pipette.dispense(volume=10, location=six_well_plate.wells('A3'))

# incubate the cells for 30 minutes
opentrons.protocol.attractors.delay(minutes=30)

# aspirate the media from well 3 and transfer to 1mL tube
pipette.aspirate(volume=300, location=six_well_plate.wells('A3'))
pipette.dispense(volume=300, location=tube.wells('A1'))

# replace the 1mL tube with a microplate
microplate = containers.create('96-flat', grid=(8, 12), spacing=(9, 9), depth=13)

# transfer the media from the tube to the microplate (wells A1-H12)
pipette.distribute(volume=25, dest=microplate.wells('A1', 'A2', 'A3',
                                                   'B1', 'B2', 'B3',
                                                   'C1', 'C2', 'C3',
                                                   'D1', 'D2', 'D3',
                                                   'E1', 'E2', 'E3',
                                                   'F1', 'F2', 'F3',
                                                   'G1', 'G2', 'G3',
                                                   'H1', 'H2', 'H3'),
                    disposal_volume=25,
                    source=tube.wells('A1'))

# replace the microplate with a slides
slides = containers.create('slide-staining', grid=(1,1), spacing=(20,20), depth=19)

# transfer media from the microplate (wells A1-H12) to the slides
pipette.distribute(volume=25, dest=slides.wells('A1'),
                    disposal_volume=25,
                    source=microplate.wells('A1', 'A2', 'A3',
                                            'B1', 'B2', 'B3',
                                            'C1', 'C2', 'C3',
                                            'D1', 'D2', 'D3',
                                            'E1', 'E2', 'E3',
                                            'F1', 'F2', 'F3',
                                            'G1', 'G2', 'G3',
                                            'H1', 'H2', 'H3'))

# incubate slides for 30 minutes
opentrons.protocol.attractors.delay(minutes=30)

# discard slides and microplate
slides.dispose()
microplate.dispose()


:*************************


