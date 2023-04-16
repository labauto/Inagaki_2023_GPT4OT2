from opentrons import labware, instruments

# Load the labware
plate_96_OSminus = labware.load('96-flat', '1')
plate_96_OSplus = labware.load('96-flat', '2')
plate_6 = labware.load('6-well-plate', '3')

# Define the pipettes
p1000 = instruments.P1000_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-1000ul', '4')])
p10 = instruments.P10_Single(mount='right', tip_racks=[labware.load('opentrons-tiprack-10ul', '5')])

# Transfer DMEM to 96-well plate (OS-)
p1000.pick_up_tip()
for well in plate_96_OSminus.wells():
    p1000.transfer(100, plate_6.wells('A1'), well, new_tip='never')
p1000.drop_tip()

# Transfer DMEM high glucose to 96-well plate (OS+)
p1000.pick_up_tip()
for well in plate_96_OSplus.wells():
    p1000.transfer(100, plate_6.wells('A2'), well, new_tip='never')
p1000.drop_tip()

# Add OS+ supplements to 96-well plate (OS+)
p10.pick_up_tip()
for well in plate_96_OSplus.wells():
    p10.transfer(0.1, plate_6.wells('B1'), well, new_tip='never')
    p10.transfer(1, plate_6.wells('C1'), well, new_tip='never')
    p10.transfer(1, plate_6.wells('D1'), well, new_tip='never')
p10.drop_tip()

# Transfer hMSC cells to 96-well plate (OS-)
p1000.pick_up_tip()
for well in plate_96_OSminus.wells():
    p1000.transfer(100, plate_6.wells('E1'), well, new_tip='never')
p1000.drop_tip()

# Transfer hMSC cells to 96-well plate (OS+)
p1000.pick_up_tip()
for well in plate_96_OSplus.wells():
    p1000.transfer(100, plate_6.wells('F1'), well, new_tip='never')
p1000.drop_tip()

# End
print('Experiment is completed')
