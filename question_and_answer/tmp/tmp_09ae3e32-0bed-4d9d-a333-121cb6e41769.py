
#Script
from opentrons import protocol_api

#Step 1: Build Protocol Api
metadata = {

'apiLevel': '2.0',
}

protocol = protocol_api.ProtocolContext(metadata=metadata)

#Step 2: Create Pipettes
pipette_left = protocol.load_instrument('p300_multi', 'left', tip_racks=[])
pipette_right = protocol.load_instrument('p300_multi', 'right', tip_racks=[])

#Step 3: Transfer medium (DMEM) to each well of 96 well plate (OS-)
well_plate_96_OS_minus = protocol.load_labware('96-flat', slot='1') 
pipette_left.transfer(100, 
                      protocol.load_labware('trough-12row', slot='2').wells()[0],
                      well_plate_96_OS_minus.wells(),
                      new_tip='always')

#Step 4: Transfer medium (DMEM high glucose) to each well of 96 well plate (OS+)
well_plate_96_OS_plus = protocol.load_labware('96-flat', slot='3') 
pipette_left.transfer(100, 
                      protocol.load_labware('trough-12row', slot='4').wells()[1],
                      well_plate_96_OS_plus.wells(),
                      new_tip='always')

#Step 5: Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
pipette_right.transfer(0.1,
                       protocol.load_labware('trough-12row', slot='5').wells()[2],
                       well_plate_96_OS_plus.wells(),
                       mix_after=True,
                       new_tip='always')
pipette_right.transfer(1,
                       protocol.load_labware('trough-12row', slot='5').wells()[3],
                       well_plate_96_OS_plus.wells(),
                       mix_after=True,
                       new_tip='always')
pipette_right.transfer(1,
                       protocol.load_labware('trough-12row', slot='5').wells()[4],
                       well_plate_96_OS_plus.wells(),
                       mix_after=True,
                       new_tip='always')

#Step 6: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-) and (OS+)
well_plate_hMSC = protocol.load_labware('96-flat', slot='6')
pipette_left.transfer(100,
                      well_plate_hMSC.wells()[:48],
                      well_plate_96_OS_minus.wells(),
                      new_tip='always')
pipette_left.transfer(100,
                      well_plate_hMSC.wells()[48:],
                      well_plate_96_OS_plus.wells(),
                      new_tip='always')

#End
protocol.home()
protocol.pause()


:*************************


