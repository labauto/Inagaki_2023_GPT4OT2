from opentrons import labware, instruments

# define labware
plate_96_flat = labware.load('96-flat', '2')
plate_6_TC = labware.load('6-well-plate-tc', '5')

# define pipette
pipette = instruments.P300_Multi()

# transfer medium to OS(-) and OS(+) plates
pipette.pick_up_tip()
for plate in [plate_96_flat.wells()[:48], plate_96_flat.wells()[48:]]:
    pipette.transfer(100, plate_6_TC.wells('A1'), plate, new_tip='never')
pipette.drop_tip()

# add supplements to OS(+) plate
dex = 0.1  # µL
aa = 1  # µL
bgp = 1  # µL

pipette.pick_up_tip()
for well in plate_96_flat.wells()[48:]:
    pipette.transfer(dex, plate_6_TC.wells('C1'), well, new_tip='never')
    pipette.transfer(aa, plate_6_TC.wells('C2'), well, new_tip='never')
    pipette.transfer(bgp, plate_6_TC.wells('C3'), well, new_tip='never')
pipette.drop_tip()

# transfer cells to OS(-) and OS(+) plates
pipette.pick_up_tip()
for plate in [plate_96_flat.wells()[:48], plate_96_flat.wells()[48:]]:
    pipette.transfer(100, plate_6_TC.wells('B1'), plate, new_tip='never')
pipette.drop_tip()

print("Protocol complete!")  
