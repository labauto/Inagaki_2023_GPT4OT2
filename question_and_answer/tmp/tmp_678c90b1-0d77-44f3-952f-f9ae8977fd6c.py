# Import Opentrons module and API key
from opentrons import simulate
metadata = {'apiLevel': '2.8'}
protocol = simulate.get_protocol_api('2.8')

# Define 96-well plate and 6-well plate locations
well_plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
well_plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
culture_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

# Define tip racks for the pipettes
tiprack_10 = protocol.load_labware('opentrons_96_filtertiprack_10ul', '5')
tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '6')

# Define pipettes
p10 = protocol.load_instrument('p10_single', mount='left', tip_racks=[tiprack_10])
p200 = protocol.load_instrument('p300_multi', mount='right', tip_racks=[tiprack_200])

# Transfer medium (DMEM) to each well of the 96-well plate for OS(-)
p200.transfer(100, culture_plate.wells()[0], well_plate_os_minus.rows()[0], new_tip='always')

# Transfer medium (DMEM high glucose) to each well of the 96-well plate for OS(+)
p200.transfer(100, culture_plate.wells()[0], well_plate_os_plus.rows()[0], new_tip='always')

# Add osteoinduction supplements to each well of the 96-well plate for OS(+)
supplement_locations_os_plus = well_plate_os_plus.rows()[0]
p10.distribute(0.1, supplement_locations_os_plus, supplement_locations_os_plus, disposal_vol=0, new_tip='always')
p10.distribute(1, supplement_locations_os_plus, supplement_locations_os_plus, disposal_vol=0, new_tip='always')
p10.distribute(1, supplement_locations_os_plus, supplement_locations_os_plus, disposal_vol=0, new_tip='always')

# Transfer hMSC cells to each well of the 96-well plate for OS(-)
p200.transfer(100, culture_plate.wells()[1], well_plate_os_minus.rows()[0], new_tip='always')

# Transfer hMSC cells to each well of the 96-well plate for OS(+)
p200.transfer(100, culture_plate.wells()[1], well_plate_os_plus.rows()[0], new_tip='always')
