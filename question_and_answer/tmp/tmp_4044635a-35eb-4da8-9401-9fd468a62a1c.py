from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
}

def run(protocol: protocol_api.ProtocolContext) -> None:

    # Load labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tempdeck = protocol.load_module('Temperature Module', '3')
    cooled_96_well_plate = tempdeck.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    pipette_8_channels = protocol.load_instrument('p300_multi', 'left')
    tips_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '2')

    
    # Reagents
    lysis_buffer = cooled_96_well_plate.wells_by_name()["A1"]
    cell_culture_wells = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']
    cells = [six_well_plate.wells_by_name()[well] for well in cell_culture_wells]

    # Protocol steps
    tempdeck.set_temperature(4)

    # Pipette tip
    pipette_8_channels.pick_up_tip(tips_20ul.well("A1"))

    for well in cells:
        # Aspirate and mix cells
        pipette_8_channels.aspirate(100, well.bottom(z=1))
        pipette_8_channels.mix(3, 100, well)

        # Transfer cells to lysis buffer
        pipette_8_channels.dispense(100, lysis_buffer)
        pipette_8_channels.blow_out(lysis_buffer.top())

    # Drop pipette tip
    pipette_8_channels.drop_tip(tips_20ul.well("A1"))

