
# Import necessary Opentrons libraries
from opentrons import protocol_api

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
  
  # Load necessary labware
  plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
  plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
  reagent_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
  source_plate = protocol.load_labware('corning_6_wellplate_16.84ml_flat', '4')
  
  # Define functions for each step of the experiment
  def add_dmso(well, volume):
      pipette.transfer(volume, source_plate['A1'], well, mix_before=(3, volume//2), new_tip='always')

  def add_supplements(well, volume):
      pipette.transfer(volume, reagent_plate['A1'], well, mix_before=(3, volume//2), new_tip='always')

  def add_cells(well, volume):
      pipette.transfer(volume, source_plate['B1'], well, mix_before=(3, volume//2), new_tip='always')

  # Define pipettes and volume amounts
  pipette = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '5')])
  medium_volume = 100
  supplement_volume = {'Dex': 0.1, 'AA': 1, 'BGP': 1}
  cell_volume = 100

  # Add medium to all wells on OS- and OS+ plates
  for plate in [plate_os_minus, plate_os_plus]:
      for well in plate.wells():
          add_dmso(well, medium_volume)

  # Add supplements to OS+ plate
  for well, volume in zip(plate_os_plus.wells(), supplement_volume.values()):
      add_supplements(well, volume)

  # Add cells to all wells on OS- and OS+ plates
  for plate in [plate_os_minus, plate_os_plus]:
      for well in plate.wells():
          add_cells(well, cell_volume)

  # End of protocol
  protocol.comment("Experiment complete!")
