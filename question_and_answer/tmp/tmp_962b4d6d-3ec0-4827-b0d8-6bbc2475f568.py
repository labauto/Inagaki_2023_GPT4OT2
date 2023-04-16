from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Your Name <your.email@example.com>',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tip_rack_200 = protocol.load_labware("opentrons_96_tiprack_1000ul", location="1")
    pbs_reservoir = protocol.load_labware("nest_12_reservoir_15ml", location="2")
    dmem_reservoir = protocol.load_labware("nest_12_reservoir_15ml", location="3")
    six_well_plate = protocol.load_labware("corning_6_wellplate_16.8ml_flat", location="4")

    # Pipettes
    p1000 = protocol.load_instrument("p1000_single_gen2", mount="right", tip_racks=[tip_rack_200])

    # Locations
    pbs_ch = pbs_reservoir.wells()[0] # You can change the well in the reservoir if not well 0
    dmem_ch = dmem_reservoir.wells()[0] # You can change the well in the reservoir if not well 0
    wells = six_well_plate.wells()

    # Aspirating and dispensing PBS(-)
    for well in wells:
        p1000.pick_up_tip()
        p1000.aspirate(900, pbs_ch) # Aspirate required volume of PBS(-)
        p1000.dispense(900, well) # Dispense PBS(-) to corresponding well
        p1000.mix(3, 900, well) # Mix PBS(-) 3 times in the well
        p1000.aspirate(900, well) # Aspirate the mixed solution
        p1000.dispense(900, pbs_ch) # Dispense the solution back to the reservoir
        p1000.drop_tip()

    # Aspirating and dispensing D-MEM
    for well in wells:
        p1000.pick_up_tip()
        p1000.aspirate(900, dmem_ch) # Aspirate required volume of D-MEM
        p1000.dispense(900, well) # Dispense D-MEM in the corresponding well
        p1000.drop_tip()
