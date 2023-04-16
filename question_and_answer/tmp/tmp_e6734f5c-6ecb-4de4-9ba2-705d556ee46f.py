def change_medium(mag_height):
    '''
    Function to change medium of cells, i.e. to remove media with PBS,
    then add fresh media with 5 mL of Trypsin solution, leave it for 5
    minutes and then add media to the dish.
    
    Inputs:
    mag_height: hours before setting magnetic beads, numeric
    cells_plate: well with least number of beads*

    *: This is calculated till this step, include it if you want to do that later.

    Modified from protocol: Magnetic beads - Staining
    '''
    # Load reusable labware
    if 'Reacti-Therm Plus Heating Module' not in robot.get_installed_modules():
        raise Exception('Please install Reacti-Therm Plus Heating Module first')
    reacti_block = labware.load('reacti_thermplus_block', slot='1')
    p300rack = labware.load('opentrons_96_tiprack_300ul', slot='2')
    trough_1 = labware.load('trough-12row', slot='3')
    trough_2 = labware.load('trough-12row', slot='4')
    trough_3 = labware.load('trough-12row', slot='5')
    trough_4 = labware.load('trough-12row', slot='6')
    pcr_plate = labware.load('biorad_96_wellplate_200ul_pcr', slot='10')
    tube_3 = labware.load('opentrons_24_tuberack_nest_1.5ml_snapcap', slot='12')

    # Fixed labware
    dilution_plate = labware.load('biorad_96_wellplate_200ul_pcr', '7', share=True)
    waste_tube = labware.load('opentrons_24_tuberack_nest_1.5ml_snapcap', '11', share=True)
    waste = waste_tube['A2'].bottom(3)

    # Liquid transfer settings
    # mag_height = 2

    tip_vol = 300
    wtvol = 1800
    incvol = 220

    # Tip composition settings
    tip_300 = p300rack['A'].top()

    # Pipetting setup
    p300 = instruments.P300_Single(mount="left", tip_racks=[p300rack])

    # Protocol Steps Begins: need 3 ml of 0.25% Trypsin in 50 ml tube
    # Wash with PBS(-)
    tips_needed = len(pcr_plate.columns()) * 10
    if len(p300rack.rows()) < tips_needed / 8 + 1:
        raise Exception('Please add more tipracks to slot 2')
    if len(dilution_plate.columns()) < tips_needed / 8 + 1:
        raise Exception('Please add dilution plate to 7')
    p300.pick_up_tip(tip_300)
    for col in pcr_plate.columns():
        p300.aspirate((60*wtvol + 20*wtvol)/tip_vol,p300.current_volume)
        for i in range(2*12):
            p300.aspirate(60*wtvol/tip_vol, trough_1.wells()[i].bottom(wtvol/tip_vol+2))
            p300.dispense(60*wtvol/tip_vol, col.top(-wtvol/tip_vol-1))
            # Return media to original well
            p300.aspirate(60*wtvol/tip_vol, col.top(-wtvol/tip_vol-5))
            p300.dispense(60*wtvol/tip_vol, trough_1.wells()[i].bottom(mag_height*wtvol/tip_vol+2))
        # Remove media in 90 mm plate
        p300.dispense(wtvol*(10+1)/tip_vol, waste)
    p300.drop_tip()

    # Add media first
    tips_needed = 2
    if len(p300rack.rows()) < tips_needed / 8 + 1:
        raise Exception('Please add more tipracks to slot 2')
    for i in range(tips_needed):
        p300.pick_up_tip(tip_300)
        p300.aspirate((200*wtvol + 10*wtvol)/tip_vol,p300.current_volume_.magnitude)
        for j in range(2):
            p300.aspirate(incvol*wtvol/tip_vol, tube_3.wells()[0].bottom(wtvol/tip_vol+2))
            p300.dispense(incvol*wtvol/tip_vol, pcr_plate.wells()[i].top(-wtvol/tip_vol-1))
            p300.aspirate(incvol*wtvol/tip_vol, pcr_plate.wells()[i].top(-wtvol/tip_vol-5))
            p300.dispense(incvol*wtvol/tip_vol, tube_3.wells()[0].bottom(wtvol/tip_vol+2))
        p300.dispense(30*wtvol/tip_vol, waste)
        p300.drop_tip()

    # Add trypsin now
    if robot.is_simulating():
        return
    Protocol.pause_comment('Leave at 37 degrees for 3 mins')
    for i in range(3):
        reacti_block.set_temperature(37,wait_time=60)

    tips_needed = 2
    if len(p300rack.rows()) < tips_needed / 8 + 1:
        raise Exception('Please add more tipracks to slot 2')
    for i in range(tips_needed):
        p300.pick_up_tip(tip_300)
        p300.aspirate((40*wtvol + 5*wtvol)/tip_vol,p300.current_volume_.magnitude)
        for j in range(1):
            p300.aspirate(wtvol/tip_vol, tube_3.wells()[0].bottom(wtvol/tip_vol+2))
            p300.dispense(720*wtvol/tip_vol, pcr_plate.wells()[i].bottom(wtvol/tip_vol+2))
            p300.aspirate(380*wtvol/tip_vol, pcr_plate.wells()[i].bottom(-wtvol/tip_vol-5))
            p300.dispense(380*wtvol/tip_vol, tube_3.wells()[0].bottom(wtvol/tip_vol+2))
        p300.drop_tip()
    Protocol.pause_comment('Leave at 37 degrees for 5 mins')
    for i in range(3):
        reacti_block.set_temperature(37,wait_time=60)

    # Add fresh media
    for i in range(tips_needed):
        p300.pick_up_tip(tip_300)
        p300.aspirate((200*wtvol + 10*wtvol)/tip_vol,p300.current_volume_.magnitude)
        for j in range(2):
            p300.aspirate(incvol*wtvol/tip_vol, tube_3.wells()[0].bottom(wtvol/tip_vol+2))
            p300.dispense(incvol*wtvol/tip_vol, pcr_plate.wells()[i].top(-wtvol/tip_vol-1))
           


:*************************


