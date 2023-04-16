from opentrons import protocol_api

metadata = {'apiLevel': '2.9'}

def run(protocol: protocol_api.ProtocolContext):
    # Define labware
    pcr_strip_96_well = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '1')
    tipracks_10 = [
        protocol.load_labware('opentrons_96_tiprack_10ul', str(slot))
        for slot in range(2, 5)
    ]
    tipracks_200 = [
        protocol.load_labware('opentrons_96_tiprack_200ul', str(slot))
        for slot in range(5, 8)
    ]
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '8')
    tempdeck = protocol.load_module('tempdeck', '9')
    temp_plate = tempdeck.load_labware('corning_96_wellplate_360ul_flat')

    # Define pipettes
    p10_single = protocol.load_instrument('p10_single', 'left', tip_racks=tipracks_10)
    p300_single = protocol.load_instrument('p300_single', 'right', tip_racks=tipracks_200)

    # Define reagents
    celltox_reagent = temp_plate['A1']
    celltiter_reagent = temp_plate['B1']

    # Define volumes
    celltox_vol = 15
    celltiter_vol = 80
    cell_susp_vol = 60
    medium_vol = 100

    # Define concentrations
    initial_concs = [1000, 100, 10, 1, 0.1, 0.05, 0.01]
    dilutions = {
        'C': [1.56, 3.12, 6.24, 12.52, 25, 50],
        'D': [100, 200, 400, 800, 1600, 2000],
    }

    # Mix cells
    p10_single.pick_up_tip()
    for index in range(10):
        well = pcr_strip_96_well['A{}'.format(index+1)]
        p10_single.transfer(cell_susp_vol, well, pcr_strip_96_well['H{}'.format(index+1)], new_tip='never')
    p10_single.drop_tip()

    # Add medium to negative control wells
    p10_single.pick_up_tip()
    for col in range(3):
        p10_single.transfer(medium_vol, pcr_strip_96_well['A5'], plate_96_well['{}5'.format(chr(65+col))], new_tip='never')
    p10_single.drop_tip()

    # Prepare and distribute dilutions of Thapsigargin into 1.5mL snap-cap tubes
    for index, conc in enumerate(initial_concs):
        stock_tube = temp_plate['C{}'.format(index+1)]
        p300_single.pick_up_tip()
        p300_single.mix(3, 120, stock_tube)
        p300_single.aspirate(medium_vol, stock_tube)
        p300_single.dispense(medium_vol, stock_tube)

        if conc == 0.1:
            dilution_vol = 40
        else:
            dilution_vol = 20
        for row in ['C', 'D']:
            for col_index, dilute_conc in enumerate(dilutions[row]):
                dilute_vol = dilution_vol / dilute_conc
                source = temp_plate['{}{}'.format(row, index+1)]
                dest = temp_plate['{}{}'.format(row, col_index+1)]
                p300_single.pick_up_tip()
                p300_single.mix(3, 120, source)
                p300_single.aspirate(dilute_vol, source)
                p300_single.dispense(dilute_vol, dest)
                p300_single.mix(3, 120, dest)
                p300_single.drop_tip()

    # Add drug to plate
    p300_single.pick_up_tip()
    for col in range(7):
        concs = [initial_concs[col]] + dilutions[chr(67+col)]
        for row, conc in enumerate(concs, start=1):
            if conc == 0:
                p300_single.transfer(medium_vol, pcr_strip_96_well['A5'], plate_96_well['{}{}'.format(chr(65+col), row+4)], new_tip='never')
            else:
                source = temp_plate['{}{}'.format(chr(67+col), concs.index(conc)+1)]
                p300_single.aspirate(2*concentration, source)
                p300_single.dispense(medium_vol, plate_96_well['{}{}'.format(chr(65+col), row+4)])
                p300_single.mix(5, 60, plate_96_well['{}{}'.format(chr(65+col), row+4)])
    p300_single.drop_tip()

    # Wait 72 hours
    protocol.comment('Incubate plate for 72 hours in a humidified CO2 incubator')

    # CellTox Green assay
    for col in range(2):
        p10_single.pick_up_tip()
        for row in range(8):
            dest = plate_96_well['{}{}'.format(chr(65+col), row+1)]
            if row == 3:
                continue
            p10_single.transfer(celltox_vol, celltox_reagent, dest, new_tip='never')
        p10_single.drop_tip()

        protocol.comment('Orbital shaking for 2 minutes at 500 rpm')
        protocol.delay(minutes=2)

        protocol.comment('Incubate for 15 minutes at room temperature')
        protocol.delay(minutes=15)

        p300_single.pick_up_tip()
        for row in range(8):
            dest = plate_96_well['{}{}'.format(chr(65+col), row+1)]
            if row == 3:
                continue
            p300_single.aspirate(celltox_vol, dest)
            p300_single.dispense(celltox_vol, temp_plate['C{}'.format(row+1)])
        p300_single.drop_tip()

        protocol.comment('Read fluorescence at 485/520nm')

    # CellTiter-Glo assay
    p300_single.pick_up_tip()
    for col in range(7):
        for row in range(5):
            dest = plate_96_well['{}{}'.format(chr(65+col), row+1)]
            if row == 3:
                continue
            p300_single.transfer(celltiter_vol, celltiter_reagent, dest, new_tip='never')
        p300_single.mix(5, 60, well)
    p300_single.drop_tip()

    protocol.comment('Orbital shaking for 2 minutes at 500 rpm')
    protocol.delay(minutes=2)

    protocol.comment('Incubate for 10 minutes at room temperature')
    protocol.delay(minutes=10)

    p300_single.pick_up_tip()
    for col in range(7):
        for row in range(5):
            dest = plate_96_well['{}{}'.format(chr(65+col), row+1)]
            if row == 3:
                continue
            p300_single.aspirate(celltiter_vol, dest)
            p300_single.dispense(celltiter_vol, temp_plate['D{}'.format(row+1)])
    p300_single.drop_tip()

    protocol.comment('Read luminescence')
