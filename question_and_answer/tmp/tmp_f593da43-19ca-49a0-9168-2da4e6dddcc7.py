from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Experiment',
    'author': 'Your Name',
}

def transfer_medium(protocol: protocol_api.ProtocolContext, source_well, dest_wells, volume):
    p300 = protocol.load_instrument('p300_single', 'left')
    for well in dest_wells:
        p300.transfer(volume, source_well, well)

def transfer_supplements(protocol: protocol_api.ProtocolContext, sources, dest_wells, volumes):
    p10 = protocol.load_instrument('p10_single', 'right')
    for i, supplement in enumerate(sources):
        for well in dest_wells:
            p10.transfer(volumes[i], supplement, well)

def transfer_cells(protocol: protocol_api.ProtocolContext, cell_source, dest_wells, volume):
    p300 = protocol.load_instrument('p300_single', 'left')
    for well in dest_wells:
        p300.transfer(volume, cell_source, well)

def run(protocol: protocol_api.ProtocolContext):
    # Load Labware
    dmem = protocol.load_labware('gyros', '1').wells_by_name()['A1']
    dmem_high = protocol.load_labware('neo', '2').wells_by_name()['A1']
    supplements = protocol.load_labware('corning', '3').wells_by_name()
    dexamethasone, ascorbic_acid, beta_gp = supplements['A1'], supplements['A2'], supplements['A3']
    cell_source = protocol.load_labware('nunc', '4').wells_by_name()['A1']
    os_minus = protocol.load_labware('greiner_96_wellplate', '5').wells()
    os_plus = protocol.load_labware('greiner_96_wellplate', '6').wells()

    # Step 1 & 2: Transfer media
    transfer_medium(protocol, dmem, os_minus, 100)
    transfer_medium(protocol, dmem_high, os_plus, 100)

    # Step 3: Add supplements
    transfer_supplements(protocol, [dexamethasone, ascorbic_acid, beta_gp], os_plus, [0.1, 1, 1])

    # Step 4 & 5: Transfer cells
    transfer_cells(protocol, cell_source, os_minus, 100)
    transfer_cells(protocol, cell_source, os_plus, 100)
