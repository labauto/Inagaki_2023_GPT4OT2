# Import Opentrons modules
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Immunostaining of hMSC Cells to Visualize Lysosomes',
    'author': 'Your Name <your.email@example.com>',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes using Opentrons machine',
    'apiLevel': '2.5'
}

# Define a Protocol Class
class ImmunostainingProtocol(protocol_api.Protocol):
    def run(self,):
        # Define tip racks
        tip_racks_1000ul = [self.load_labware('opentrons_96_tiprack_1000ul', slot) for slot in ['7']]

        # Define Labware
        plate = self.load_labware('corning_6_wellplate_16.8ml_flat', '4')
        reservoir = self.load_labware('nest_12_reservoir_15ml', '5')
        wash_buffer = reservoir.columns()[0][1]
        paraformaldehyde = reservoir.columns()[0][2]

        # Define a Pipette
        p1000 = self.load_instrument('p1000_single_gen2', 'right', tip_racks=tip_racks_1000ul)

        # Define operation parameters
        mixing_volume = 1000  # aspirate/dispense volume
        number_of_washes = 3

        # Preparing Fixative
        p1000.pick_up_tip()
        p1000.aspirate(1000, paraformaldehyde)
        p1000.dispense(1000, plate[0])
        p1000.mix(10, mixing_volume, plate[0])
        p1000.drop_tip()

        # Preparing Wash Buffer
        for i in range(number_of_washes):
            p1000.pick_up_tip()
            p1000.aspirate(1000, wash_buffer)
            p1000.dispense(1000, plate[0])
            p1000.mix(10, mixing_volume, plate[0])
            p1000.aspirate(1000, plate[0])
            p1000.drop_tip()
