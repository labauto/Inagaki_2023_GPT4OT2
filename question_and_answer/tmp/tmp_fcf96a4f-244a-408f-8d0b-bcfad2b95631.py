from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.9'
}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):

    # function to transfer 100 µl of medium to each well
    def transfer_medium(volume, source, dest):
        pipette.transfer(volume, source, dest, new_tip='always')
    
    # function to add supplements to the OS+ wells
    def add_supplements():
        pipette.pick_up_tip()
        for well in os_plus_wells:
            pipette.aspirate(0.1, dex)
            pipette.dispense(0.1, well)
            pipette.aspirate(1, aa)
            pipette.dispense(1, well)
            pipette.aspirate(1, bgp)
            pipette.dispense(1, well)
        pipette.drop_tip()

    # create and set pipette
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', slot) for slot in ['1', '4']])
    pipette.flow_rate.aspirate = 25
    pipette.flow_rate.dispense = 50

    # load labwares
    cell_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2', 'cell plate')
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3', 'OS- plate')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5', 'OS+ plate')
    
    # get the target wells
    os_minus_wells = [well for well in os_minus_plate.wells() if well.has_empty_tip]
    os_plus_wells = [well for well in os_plus_plate.wells() if well.has_empty_tip]

    # get the reagents
    dex = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', '6', 'Dex').wells()[0]
    aa = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', '7', 'AA').wells()[0]
    bgp = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', '8', 'BGP').wells()[0]

    # transfer medium to the OS- wells
    transfer_medium(100, cell_plate.wells(), os_minus_wells)
    
    # transfer medium to the OS+ wells and add supplements
    transfer_medium(100, cell_plate.wells(), os_plus_wells)
    add_supplements()

    # transfer cells to the plates
    transfer_medium(100, cell_plate.wells(), os_minus_wells + os_plus_wells)
