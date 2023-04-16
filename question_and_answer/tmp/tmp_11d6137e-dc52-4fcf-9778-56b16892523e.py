import opentrons

metadata = {
    'protocolName': 'Cell Culture',
    'author': 'Sak <sak@opentrons.com>',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.9'
}


def run(ctx):

    [protocolName, height, width, depth, tube_type,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           


:*************************


import opentrons

metadata = {
    'protocolName': 'In Vitro Cell Culture',
    'author': 'Rami Farawi <rami.farawi@opentrons.com>',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.9'
}


def run(ctx):

    [protocolName, height_mm, width_mm, depth_mm,
        num_col_mm, num_row_mm, vol_mm_per_col, vol_mm_per_row] = get_values(  # noqa: F821
        "protocolName", "height_mm", "width_mm", "depth_mm",
            "num_col_mm", "num_row_mm", "vol_mm_per_col",
            "vol_mm_per_row")

    height_mm = int(height_mm)
    width_mm = int(width_mm)
    depth_mm = int(depth_mm)
    num_col_mm = int(num_col_mm)
    num_row_mm = int(num_row_mm)
    vol_mm_per_col = float(vol_mm_per_col)
    vol_mm_per_row = float(vol_mm_per_row)

    # load module
    from opentrons.module.labware.vortex import Vortex
    from opentrons.module.labware.pcr import PCR_96_wellplate
    from opentrons.module.labware.nest import Nest_96_wellplate
    from opentrons.module.labware.flatbed import Flatbed_96_wellplate
    from opentrons.module.labware.eppendorf.eppendorf_96_wellplate import
        Eppendorf_96_wellplate
    from opentrons.module.labware.eppendorf.eppendorf_1_tube_rack import
        Eppendorf_1_tube_rack
    from opentrons.module.labware.safelock.safelock_96_vial import Safelock_96_vial
    from opentrons.module.labware.safelock.safelock_1_tube_rack import
        Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_2_aluminum_tubes
    from opentrons.module.labware.pcr import PCR_96_wellplate_2
    from opentrons.module.labware.flatbed import Flatbed_96_pcr_plate
    from opentrons.module.labware.flatbed import Flatbed_96_wellplate_2
    from opentrons.module.labware.eppendorf import Eppendorf_96_pcr_plate
    from opentrons.module.labware.eppendorf import Eppendorf_96_wellplate_2
    from opentrons.module.labware.nest import Nest_96_aluminum_tubes
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.pcr import PCR_96_pcr_plate
    from opentrons.module.labware.flatbed import Flatbed_96_aluminum_tubes
    from opentrons.module.labware.eppendorf import Eppendorf_1_tube_rack
    from opentrons.module.labware.safelock import Safelock_96_vial
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_2_aluminum_tubes
    from opentrons.module.labware.pcr import PCR_96_pcr_plate_2
    from opentrons.module.labware.flatbed import Flatbed_96_wellplate_2
    from opentrons.module.labware.eppendorf import Eppendorf_96_wellplate_2
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_96_aluminum_tubes
    from opentrons.module.labware.flatbed import Flatbed_96_aluminum_tubes
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_2_aluminum_tubes
    from opentrons.module.labware.pcr import PCR_96_pcr_plate_2
    from opentrons.module.labware.flatbed import Flatbed_96_wellplate_2
    from opentrons.module.labware.eppendorf import Eppendorf_96_wellplate_2
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_96_aluminum_tubes
    from opentrons.module.labware.flatbed import Flatbed_96_aluminum_tubes
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_2_aluminum_tubes
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_96_aluminum_tubes
    from opentrons.module.labware.flatbed import Flatbed_96_aluminum_tubes
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_2_aluminum_tubes
    from opentrons.module.labware.safelock import Safelock_96_vial_2
    from opentrons.module.labware.safelock import Safelock_1_tube_rack
    from opentrons.module.labware.nest import Nest_96_aluminum_tubes
    from opentrons.module.labware.flat


:*************************


