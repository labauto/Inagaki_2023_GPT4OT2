from opentrons import simulate
import json

protocol_string = '''
{
  "labware": {
    "wellplate": ["corning_6_wellplate_16.8ml_flat", [1, 0]],
    "pbs_tube_rack": ["opentrons_6_tuberack_falcon_50ml_conical", [3, 0]],
    "dmem_tube_rack": ["opentrons_6_tuberack_falcon_50ml_conical", [4, 0]],
    "waste_rack": ["agilent_1_reservoir_290ml", [2, 0]],
    "tip_rack": ["opentrons_96_tiprack_1000ul", [10, 0]]
  },
  "pipettes": {
    "left_pipette": {
      "type": "p1000_single",
      "mount": "left"
    },
    "right_pipette": {
      "type": "p300_single",
      "mount": "right"
    }
  },
  "procedure": [
    {
      "type": "Wells",
      "id": "A1"
    }
  ]
}
'''

protocol_data = json.loads(protocol_string)
metadata = {'apiLevel': '2.9'}
protocol = simulate.get_protocol_api(metadata["apiLevel"])

# Load labware
wellplate = protocol.load_labware(*protocol_data['labware']['wellplate'])
pbs_tube_rack = protocol.load_labware(
    *protocol_data['labware']['pbs_tube_rack']
)
dmem_tube_rack = protocol.load_labware(
    *protocol_data['labware']['dmem_tube_rack']
)
waste_rack = protocol.load_labware(*protocol_data['labware']['waste_rack'])
tip_rack = protocol.load_labware(*protocol_data['labware']['tip_rack'])

# Load pipettes
left_pipette_data = protocol_data['pipettes']['left_pipette']
left_pipette = protocol.load_instrument(
    left_pipette_data['type'], left_pipette_data['mount'], tip_racks=[tip_rack]
)

right_pipette_data = protocol_data['pipettes']['right_pipette']
right_pipette = protocol.load_instrument(
    right_pipette_data['type'], right_pipette_data['mount']
)

# Protocol steps
for step in protocol_data['procedure']:
    if step["type"] == "Wells":
        well = wellplate.wells_by_name()[step["id"]]
        
        # Aspirate 3ml of cell culture medium into waste
        left_pipette.pick_up_tip()
        left_pipette.aspirate(3000, well.bottom(1))
        left_pipette.dispense(3000, waste_rack.wells()[0].top())
        left_pipette.blow_out()

        # Wash the well with 3ml of PBS(-)
        left_pipette.aspirate(3000, pbs_tube_rack.wells_by_name()['A1'].bottom(1))
        left_pipette.dispense(2000, well.top())
        left_pipette.blow_out()
        left_pipette.aspirate(1000, waste_rack.wells()[0].top())
        left_pipette.dispense(1000, well.top())
        left_pipette.blow_out()

        # Replace the medium with 3ml of D-MEM
        left_pipette.aspirate(3000, dmem_tube_rack.wells_by_name()['A1'].bottom(1))
        left_pipette.dispense(3000, well.top())

        # Dispose of the tips and reset the pipette
        left_pipette.drop_tip()
        left_pipette.reset_tip_origin()

protocol.home()  # Return the robot to the home position
print('Simulation complete!')  # (Optional) Print a completion message
