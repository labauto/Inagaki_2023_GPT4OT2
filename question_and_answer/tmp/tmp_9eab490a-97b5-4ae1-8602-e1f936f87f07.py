import asyncio
from opentrons import protocol_api, hardware_control

async def main():
    # Define the protocol for the experiment
    def protocol(ctx: protocol_api.ProtocolContext):
        # Labware
        six_well_plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '3')
        tiprack_1000 = ctx.load_labware('opentrons_96_tiprack_1000ul', '4')
        reagent_tuberack = ctx.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '1')

        # Pipettes
        p1000 = ctx.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

        # Reagents
        pbs_minus = reagent_tuberack.wells_by_name()['A1']
        dmem = reagent_tuberack.wells_by_name()['B1']

        # Define volumes
        pbs_minus_volume = 1000
        dmem_volume = 1000

        # Define well positions for A, B, and C rows
        wells_a = six_well_plate.wells('A1', 'A2', 'A3')
        wells_b = six_well_plate.wells('B1', 'B2', 'B3')

        # Aspirate PBS(-) and dispense into wells A1, A2, A3
        for well in wells_a:
            p1000.pick_up_tip()
            p1000.aspirate(pbs_minus_volume, pbs_minus)
            p1000.dispense(pbs_minus_volume, well)
            p1000.drop_tip()

        # Aspirate D-MEM and dispense into wells B1, B2, B3
        for well in wells_b:
            p1000.pick_up_tip()
            p1000.aspirate(dmem_volume, dmem)
            p1000.dispense(dmem_volume, well)
            p1000.drop_tip()

    # Start the protocol on the Opentrons robot
    ctx = await hardware_control.API.build_hardware_controller(force=True)
    ctx.connect(port=None)
    loaded_protocol = asyncio.run(protocol_api.backend.ProtocolContents.build(protocol))

    execution_data = loaded_protocol.to_dict()

    await protocol_api.API.pre_engine(plan_data, ctx._backend)
    await protocol_api.API.engine(plan_data, ctx._backend)

if __name__ == '__main__':
    asyncio.create_task(main())
    asyncio.get_event_loop().run_forever()
