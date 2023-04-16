# Import the necessary Opentrons modules
from opentrons import protocol_api

# Define the protocol function
def run(protocol: protocol_api.ProtocolContext):

    # Define deck layout
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    opentrons_tube_rack_15_1 = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical',
                                                     '6')
    opentrons_tube_rack_15_2 = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical',
                                                     '7')
    opentrons_tube_rack_10 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',
                                                   '10')
    heater_shaker_module = protocol.load_module('magdeck', '4')
    heater_shaker = heater_shaker_module.load_labware('corning_96_wellplate_360ul_flat')

    # Define pipettes
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul',
                                                                                    slot) for slot in ['2', '3']])

    p200 = protocol.load_instrument('p300_multi', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul',
                                                                                   slot) for slot in ['5', '8']])

    # Add 60ul of cell suspension to the wells of the 96 well plate
    p1000.pick_up_tip()
    for well in plate_96_well.rows_by_name()['A'][5:8]:
        p1000.aspirate(60, opentrons_tube_rack_15_1['A1'])
        p1000.dispense(60, well)
    p1000.drop_tip()

    # Add media to control wells
    for well in plate_96_well.rows_by_name()['A'][0:3]:
        p1000.pick_up_tip()
        p1000.aspirate(60, opentrons_tube_rack_15_1['D1'])
        p1000.dispense(60, well)
        p1000.drop_tip()

    # Prepare drug dilutions and add to 96 well plates
    initial_tube = opentrons_tube_rack_15_2['A1']
    p300.pick_up_tip()
    for tube_column in opentrons_tube_rack_15_2.columns()[0:6]:
        for tube in tube_column:
            if tube == initial_tube:
                p300.aspirate(35, initial_tube)
            else:
                p300.aspirate(35/4, opentrons_tube_rack_15_2[tube])
            p300.dispense(35/4, opentrons_tube_rack_15_2[tube.next_on_deck])
            p300.mix(3, 200)
    p300.drop_tip()

    diluent_tube = opentrons_tube_rack_15_2['B1']
    p300.pick_up_tip()
    for i, tube_column in enumerate(opentrons_tube_rack_15_2.columns()[6:]):
        for j, tube in enumerate(tube_column):
            if j % 2 == 0:
                dilution = diluent_tube
            else:
                dilution = tube_image = opentrons_tube_rack_15_2.columns()[6 + j - 1][i]

            p300.aspirate(35/4, diluent_tube)
            p300.aspirate(35/4, tube)
            p300.dispense(35/2, dilution)
            p300.mix(3, 200)
            p300.aspirate(35/2, diluent_tube)
            p300.dispense(35/4, tube.next_on_deck)
            p300.mix(3, 200)

    concentrations = [
        '1mM',
        '100microM',
        '10microM',
        '1microM',
        '100nM',
        '50nM',
    ]

    dilutions = [
        ['1.56nM', '3.12nM', '6.24nM', '12.52nM', '25nM', '50nM'],
        ['100nM', '200nM', '400nM', '800nM', '1600nM', '2000nM'],
    ]

    for i, dilution_column in enumerate(dilutions):
        for j, dilution in enumerate(dilution_column):
            row = plate_96_well.rows_by_name()[chr(ord('D') + i)]
            well = row[j * 3]
            p300.pick_up_tip()
            for k in range(3):
                if k == 0:
                    drug_concentration = opentrons_tube_rack_15_2['A1']
                else:
                    drug_concentration = row[j * 3 + k - 1]
                p300.aspirate(100, diluent_tube)
                p300.dispense(100, well[k])
                p300.aspirate(50, drug_concentration)
                p300.dispense(50, well[k])
                p300.mix(3, 200)
                p300.aspirate(50, diluent_tube)
                p300.dispense(50, well[k].next_on_row())
                p300.mix(3, 200)

            p300.drop_tip()

    # Add CellTox Green reagent
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_20ul',
                                                                               slot) for slot in ['9', '11']])
    cell_tox_green_tube = opentrons_tube_rack_10['B2']
    p20.pick_up_tip()
    for row in plate_96_well.rows():
        if row[0] == plate_96_well['D4']:
            break
        for well in row:
            p20.aspirate(15, cell_tox_green_tube)
            p20.dispense(15, well)

    p20.drop_tip()

    heater_shaker_module.set_temperature(ambient_temperature)
    heater_shaker_module.start_magnetic_module()
    heater_shaker_module.engage()

    protocol.delay(minutes=1)

    # Start shaking plate
    heater_shaker.start_orbital_shaking(500)

    protocol.delay(minutes=2)

    # Incubate for 15 min at room temperature
    protocol.delay(minutes=15)

    # Read fluorescence
    protocol.comment('Reading fluorescence...')
    # ...

    # Add Cell Titer Glo 2.0 reagent
    cell_titer_glo_tube = opentrons_tube_rack_10['B1']
    p300.pick_up_tip()
    for row in plate_96_well.rows():
        if row[0] == plate_96_well['D4']:
            break
        for well in row:
            p300.aspirate(80, cell_titer_glo_tube)
            p300.dispense(80, well)

    p300.drop_tip()

    # Start shaking plate
    heater_shaker.start_orbital_shaking(500)

    protocol.delay(minutes=2)

    # Incubate for 10 min at room temperature
    protocol.delay(minutes=10)

    # Read luminescence
    protocol.comment('Reading luminescence...')
    # ...
