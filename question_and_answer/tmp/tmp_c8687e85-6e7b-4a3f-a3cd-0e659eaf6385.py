from opentrons import protocol_api

metadata = {'protocolName': 'hMSC Spheroid Formation'}

def run(protocol: protocol_api.ProtocolContext):
    scale_factor = 0.5
    
    # Load Labware
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '7')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '10')
    plate_96_well = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '4')

    # Load Pipettes
    p300 = protocol.load_instrument('p300_multi_gen2', mount='right', tip_racks=[tiprack_200])

    # Distribute Medium to 96-Well plate
    # Perform OS- condition first
    p300.pick_up_tip()
    for i in range(96):
    	if not p300.has_tip:
    		p300.pick_up_tip()
    	p300.transfer(100 / scale_factor, reservoir.wells()[0], plate_96_well.wells()[i], new_tip='never')
    	if i == 95:
    		p300.drop_tip()
    # Perform OS+ condition
    p300.pick_up_tip()
    for i in range(96):
    	if not p300.has_tip:
    		p300.pick_up_tip()
    	p300.transfer(100 / scale_factor, reservoir.wells()[1], plate_96_well.wells()[i], new_tip='never')
    	if i == 95:
    		p300.drop_tip()

    # Add supplements to OS+ wells
    p300.pick_up_tip()
    for i in range(96):
        if not p300.has_tip:
            p300.pick_up_tip()
        if i == 0:
            p300.aspirate(1/scale_factor, reservoir.wells()[3])
        if i == 95:
            p300.aspirate(1/scale_factor, reservoir.wells()[4])
        p300.dispense(0.1/scale_factor, plate_96_well.wells()[i])
        p300.mix(2, 50/scale_factor)
        if i == 0:
            p300.aspirate(1/scale_factor, reservoir.wells()[5])
        if i == 95:
            p300.aspirate(1/scale_factor, reservoir.wells()[6])
        p300.dispense(1/scale_factor, plate_96_well.wells()[i])
        p300.mix(2, 50 / scale_factor)
        if i == 95:
            p300.drop_tip()
	
	# Add cells to OS- and OS+ wells
	# Perform OS- condition first
	p300.pick_up_tip()
	for i in range(96):
		if not p300.has_tip:
		    p300.pick_up_tip()
		p300.transfer(100 / scale_factor, reservoir.wells()[2], plate_96_well.wells()[i], new_tip='never')
		if i == 95:
			p300.drop_tip()
	# Perform OS+ condition
	p300.pick_up_tip()
	for i in range(96):
		if not p300.has_tip:
		    p300.pick_up_tip()
		p300.transfer(100 / scale_factor, reservoir.wells()[2], plate_96_well.wells()[i+96], new_tip='never')
		if i == 95:
			p300.drop_tip()

