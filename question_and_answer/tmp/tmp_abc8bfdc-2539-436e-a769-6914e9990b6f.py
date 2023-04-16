from opentrons.protocol_api.labware import ModuleGeometry
from opentrons.hardware_control.types import APIVersion


class HeaterShakerModuleGeometry(ModuleGeometry):
    def __init__(
            self,
            api_level: APIVersion,
    ) -> None:
        super().__init__(
            'heaterShakerModuleV1',
            api_level,
            5
        )
from .heater_shaker_module import HeaterShakerModuleGeometry
elif model.lower() == 'heatershakermodulev1':
    return HeaterShakerModuleGeometry(APIVersion(2, 0))
from opentrons import protocol_api

def run(protocol: protocol_api.ProtocolContext):
    # Custom labware
    custom_tube_rack = 'custom_tube_rack'
    custom_96well_plate = 'custom_96_well_plate'
    positions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']

    metadata = {'apiLevel': '2.9'}

    # Define labware
    tip_rack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tip_rack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)

    tube_rack = protocol.load_labware(custom_tube_rack, 6)
    rxn_plate = protocol.load_labware(custom_96well_plate, 9)

    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack_20])
    right_pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack_200])

    # Custom module geometry
    heater_shaker = protocol.load_module('heaterShakerModuleV1', 5)
