import opentrons.execute
from opentrons import protocol_api

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')  # 300ul tiprack
    pbs_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')  # PBS(-) plate
    dmem_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')  # D-MEM plate
    cell_plate = protocol.load_labware('nest_6_wellplate_20ml_flat', '1')  # 6-well cell culture plate

    # Pipettes
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack_300])

    # Variables
    volume_pbs = 200  # volume of PBS to aspirate
    volume_dmem = 200  # volume of D-MEM to aspirate
    mix_iterations = 3  # number of mix iterations

    # Protocol
    for well_idx in range(6):
        p300.pick_up_tip()

        # Aspirate PBS
        p300.aspirate(volume_pbs, pbs_plate.wells()[well_idx])
        p300.dispense(volume_pbs, cell_plate.wells()[well_idx].bottom(10))
        p300.mix(mix_iterations, volume_pbs / 2, cell_plate.wells()[well_idx].bottom(10))
        p300.blow_out(cell_plate.wells()[well_idx].top())

        # Aspirate cell solution
        p300.aspirate(volume_pbs, cell_plate.wells()[well_idx].bottom(10))
        p300.dispense(volume_pbs, pbs_plate.wells()[well_idx].top())
        p300.blow_out(pbs_plate.wells()[well_idx].top())

        # Aspirate D-MEM
        p300.aspirate(volume_dmem, dmem_plate.wells()[well_idx])
        p300.dispense(volume_dmem, cell_plate.wells()[well_idx].bottom(10))
        p300.mix(mix_iterations, volume_dmem / 2, cell_plate.wells()[well_idx].bottom(10))
        p300.blow_out(cell_plate.wells()[well_idx].top())

        p300.drop_tip()

    protocol.comment("Protocol complete!")


# Execute the protocol
protocol = opentrons.execute.get_protocol_api('2.11')
run(protocol)
