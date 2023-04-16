metadata = {
    "protocolName": "Viability and cytotoxicity assay of A549 cells treated with Thapsigargin",
    "author": "Your Name Here",
    "apiLevel": "2.0"
}

from opentrons import protocol_api

# Create a protocol class
class MyProtocol(protocol_api.Protocol):
    def run(self):
        # Clean the robot before starting
        self.comment("Cleaning the robot with 70% ethanol and turning on the HEPA filter.")
        self.delay(minutes=60)
        
        # Seeding A549 cells
        self.comment("Preparing to seed A549 cells.")
        countess = self.load_labware('thermofisher_countess', '1')
        plate = self.load_labware('corning_96_wellplate_360ul_flat', '2')
        tube_rack_1 = self.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '3')
        plate_2 = self.load_labware('corning_96_wellplate_360ul_flat', '4')
        
        # Take a cell count using the automated Countess 3 machine
        self.comment("Taking a cell count using the automated Countess 3 machine.")
        countess.dispense_media(media_volume=300)
        countess.load_sample('A549 cells', 'cells')
        cell_count = countess.get_cell_count()
        cell_number = 8000
        cell_volume = (cell_number / cell_count) * 10000
        cell_volume_in_ul = round(cell_volume / 1000, 2)
        
        # Adjust the cell volume in 10% Ham’s F12K medium and dispense in tubes
        self.comment("Adjusting the cell volume and dispensing in tubes.")
        diluent = 'f12k_10pc'
        cells = 'a549_cells'
        medium = 'f12k_90pc'
        for tube in tube_rack_1.wells()[:10]:
            tube.transfer(cell_volume_in_ul, cells)
            tube.transfer(225, medium)
        
        # Adding medium in control wells
        self.comment("Adding medium in control wells.")
        negative_control_indices = ['A5', 'B5', 'C5']
        for well in negative_control_indices:
            plate_2[well].transfer(60, medium)
            
        # Adding drug dilutions and additions
        self.comment("Preparing and adding drug dilutions.")
        tube_rack_2 = self.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '5')
        a1_tube = tube_rack_2['A1']
        concentrations = [1000000, 100000, 10000, 1000, 100, 50, 10] # in nM
        rows = ['D', 'E', 'F']
        columns = ['1', '2', '3', '4', '5', '6']
        for i, concentration in enumerate(concentrations):
            tube_rack_2[rows[i]][columns[0]].transfer(
                    50, diluent).mix(3)
            a1_tube.transfer(25, diluent).mix(3)
            tube_rack_2[rows[i]][columns[0]].transfer(
                    25, a1_tube).mix(3)
            tube_rack_2[rows[i]][columns[1]].transfer(
                    25, tube_rack_2[rows[i]][columns[0]]).mix(3)
            tube_rack_2[rows[i]][columns[2]].transfer(
                    25, tube_rack_2[rows[i]][columns[1]]).mix(3)
            tube_rack_2[rows[i]][columns[3]].transfer(
                    25, tube_rack_2[rows[i]][columns[2]]).mix(3)
            tube_rack_2[rows[i]][columns[4]].transfer(
                    25, tube_rack_2[rows[i]][columns[3]]).mix(3)
            tube_rack_2[rows[i]][columns[5]].transfer(
                    25, tube_rack_2[rows[i]][columns[4]]).mix(3)
            
        self.comment("Preparing and adding 2x drug dilutions.")
        for row in rows:
            for i, column in enumerate(columns):
                if i==0 or i==2 or i==4:
                    plate_2[row+column].transfer(
                            100, medium)
                    tube = tube_rack_2[row][column]
                    tube.transfer(100, diluent).mix(3)
                else:
                    tube = tube_rack_2[row][column]
                    tube.transfer(100, plate_2[row+columns[i-1]])
                    tube.mix(3)
        
        self.comment("Adding 1x drug concentration to wells in 96 well plate.")
        for i, column in enumerate(columns):
            if i==0:
                pass
            else:
                column_wells = [
                    row+column for row in ['A', 'B', 'C', 'D', 'E', 'F']
                ]
                tube_rack_2[rows[i-1]][column].transfer(
                    50


:*************************


