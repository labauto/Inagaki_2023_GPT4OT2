from opentrons import simulate, containers, instruments

# Define containers
tip_rack_20ul = containers.load('tiprack-20ul', '10')
tip_rack_200ul = containers.load('tiprack-200ul', '11')
plate_96_well = containers.load('96-PCR-flat', '1')
tubes_15ml = containers.load('tube-rack-15_50ml', '6')
tubes_50ml = containers.load('tube-rack-15_50ml', '7')
plate_TCA = containers.load('96-PCR-tall', '2')

# Define instruments
p20 = instruments.P20_Single(mount='left', tip_racks=[tip_rack_20ul])
p200 = instruments.P300_Single(mount='right', tip_racks=[tip_rack_200ul])

# Define function for adding cells to wells
def add_cells(volume):
    cells = 8000
    p200.transfer(volume, tubes_15ml.wells('A1'), tubes_15ml.wells('A2'))
    p200.transfer(volume, tubes_15ml.wells('A2'), tubes_15ml.wells('A3'))
    p200.transfer(volume, tubes_15ml.wells('A3'), tubes_15ml.wells('A4'))
    p200.transfer(volume, tubes_15ml.wells('A4'), tubes_15ml.wells('A5'))
    p200.transfer(volume, tubes_15ml.wells('A5'), tubes_15ml.wells('A6'))
    p200.transfer(volume, tubes_15ml.wells('A6'), tubes_15ml.wells('B1'))
    p200.transfer(volume, tubes_15ml.wells('B1'), plate_96_well.wells('A1', 'A2', 'A3', 'B2', 'B3', 'C1', 'C2', 'C3'))

# Define function for adding drug dilutions to wells
def add_drug(volume):
    p20.transfer(35, tubes_15ml.wells('A1'), tubes_15ml.wells('A2'))
    concs_4x = [100, 10, 1, 0.1, 0.01, 0.005]
    concs_D = [10, 20, 40, 80, 160, 200]
    for i in range(len(concs_4x)):
        p20.transfer(volume, tubes_50ml.wells('C1'), tubes_50ml.wells('C' + str(i+2)))
        p20.transfer(volume, tubes_50ml.wells('D1'), tubes_50ml.wells('D' + str(i+2)))
        p20.mix(4, volume, tubes_50ml.wells('C' + str(i+2)), tubes_50ml.wells('D' + str(i+2)))
        p20.transfer(volume, tubes_50ml.wells('C' + str(i+2)), tubes_50ml.wells('B' + str(i+2)))
        p20.transfer(volume, tubes_50ml.wells('D' + str(i+2)), tubes_50ml.wells('B' + str(i+2)))
        p20.mix(4, volume, tubes_50ml.wells('B' + str(i+2)))
        for j in range(3):
            p200.transfer(volume, tubes_50ml.wells('B' + str(i+2)), plate_96_well.wells(chr(65+j) + str(i+1)))

# Define function for adding CellTox Green reagent to wells
def add_CellTox_Green(volume):
    p20.transfer(15, tubes_15ml.wells('B2'), plate_96_well.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6'))

# Define function for adding Cell Titer Glo 2.0 reagent to wells
def add_Cell_Titer_Glo(volume):
    p200.transfer(80, tubes_15ml.wells('B1'), plate_TCA.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6'))

# Define simulation environment
protocol = simulate.get_protocol_api('2.10')

# Set up simulation environment
protocol.home()
protocol.comment('Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter at low fan speed for about an hour before seeding the cells')
add_cells(60)
protocol.comment('Add medium in wells A5 to C5 as negative control')
p200.transfer(100, tubes_15ml.wells('A1'), plate_96_well.wells('A5', 'B5', 'C5'))
protocol.comment('Prepare drug dilutions')
add_drug(5)
protocol.pause('After drug dilution is complete, proceed when ready.')
add_CellTox_Green(15)
protocol.comment('Shake the plate at 500 RPM for 2 minutes.')
protocol.plate_shake('true', minutes=2, speed='500rpm', mode='orbital', radius='2mm')
protocol.comment('Incubate the plate at RT (room temperature) for 15 minutes.')
protocol.incubate(300, 'room-temperature')
protocol.comment('Remove the plate from heater shaker and read the fluorescence at 485nm excitation and 520nm emission using Biotek microplate reader.')
protocol.pause('After fluorescence reading is complete, proceed when ready.')
add_Cell_Titer_Glo(80)
protocol.comment('Shake the plate at 500 RPM for 2 minutes.')
protocol.plate_shake('true', minutes=2, speed='500rpm', mode='orbital', radius='2mm')
protocol.comment('Incubate the plate at RT for 10 minutes.')
protocol.incubate(600, 'room-temperature')
protocol.comment('Remove the plate from heater shaker and read the plate for luminescence using Biotek microplate reader.')
