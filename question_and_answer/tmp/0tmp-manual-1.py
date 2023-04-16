from opentrons import protocol_api

metadata = {
    "protocolName": "hMSC Cell Culture Medium Exchange",
    "author": "Your Name <youremail@example.com>",
    "description": "An example protocol for exchanging hMSC cell culture medium with PBS(-) and D-MEM",
    "apiLevel": "2.7",
}


def transfer_dmem(dest_plate):
    """
    Transfer DMEM medium to each well of the destination plate.
    """
    pipette.transfer(100, dmem, dest_plate.wells(), new_tip="always")


def transfer_osteo_supps(dest_plate):
    """
    Transfer Dexamethasone, Ascorbic acid, and beta-glycerophosphate
    supplements to each well of the destination plate.
    """
    pipette.transfer((0.1, 1, 1), osteo_supps, dest_plate.wells(), new_tip="always")


def transfer_cells(source_plate, dest_plate):
    """
    Transfer hMSC cells to each well of the destination plate.
    """
    pipette.transfer(100, source_plate.wells(), dest_plate.wells(), new_tip="always")


def run(protocol: protocol_api.ProtocolContext):
    """
    Run the complete hMSC spheroid culture experiment.
    """
    # Load labware and pipettes
    source_plate = protocol_api.labware.load("opentrons_24_tuberack_nest_1.5ml_snapcap", "1", "source plate")
    os_minus_plate = protocol_api.labware.load("corning_96_wellplate_360ul_flat", "2", "OS- plate")
    os_plus_plate = protocol_api.labware.load("corning_96_wellplate_360ul_flat", "3", "OS+ plate")
    tiprack_10ul = protocol_api.labware.load("opentrons_96_tiprack_10ul", "4", "10µl tiprack")

    pipette = protocol_api.pipette.P300_Single(
        mount="right", tip_racks=[tiprack_10ul], aspirate_flow_rate=150, dispense_flow_rate=150, tip_length=51, aspirate_offset=2
    )

    # Define DMEM medium and osteo supplements
    dmem = source_plate["A1"]
    osteo_supps = source_plate["A2":"A4"]

    # Transfer DMEM to OS- and DMEM high glucose + osteo supplements to OS+ plate
    transfer_dmem(os_minus_plate)
    transfer_osteo_supps(os_plus_plate)

    # Transfer hMSC cells to both plates
    transfer_cells(source_plate, os_minus_plate)
    transfer_cells(source_plate, os_plus_plate)
