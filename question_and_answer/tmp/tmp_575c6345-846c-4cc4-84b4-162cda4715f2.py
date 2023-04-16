
def setup_robot():
    """Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter at low fan speed for about an hour before seeding the cells on 96 well plate."""
    #Clearing the robot with ethanol 
    print("Robot is being cleared with 70% ethanol")
  
    #Turn on the HEPA filter 
    print("HEPA filter is being turned on at low fan speed for about an hour")
    
    
def seeding_cells():
    """Seeding A549 cells and addition of various concentrations of Thapsigargin on the second day after the cells have adhered to the 96 well TC plate."""
    #Taking a cell count 
    print("Taking a cell count using the automated Countess 3 machine")
  
    #Seeding 8000 cells in each well 
    print("Seeding 8000cells in each well of the 96 well plate")
  
    #Adding medium to wells A5 to C5 
    print("Adding 10% Ham’s F12K medium in wells A5 to C5 as negative control")
  
    #Adding thapsigargin stock 
    print("Adding 35microL of 1mM Thapsigargin in tube A1 in Slot 7")
  
    #Preparing dilutions of thapsigargin 
    print("Preparing dilutions of various concentrations of thapsigargin in 10% Ham’s F12K medium")
    

def thapsigargin_additions():
    """On the second day, roughly after 12 to 16 hours of seeding, the drug dilutions and additions are completed."""
    #Preparing 4X concentrations of thapsigargin 
    print("Preparing 4X concentrations of thapsigargin in tubes C1 to C6 and D1 to D6")
  
    #Preparing 2X concentrations of thapsigargin 
    print("Preparing 2X concentrations of thapsigargin in tubes C1 to C6 and D1 to D6")
  
    #Adding thapsigargin to each well of 96 well plate 
    print("Adding thapsigargin to each well of 96 well plate in triplicate")
    
    
def cell_viability_assay():
    """After 72 hours of drug treatment, carry out the following steps."""
    #Adding CellTox Green reagent to the 96 well plate 
    print("Adding 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack with Falcon 4X50 mL, 6X15mL Conical-Rack to A1 of 96 well plate placed on the Heater Shaker")
  
    #Orbital shaking of the heater shaker 
    print("Setting the Heater Shaker to orbital shaking for 2 minutes at 500 rpm")
  
    #Incubation at RT
    print("Incubating the plate at RT for 15 min")
  
    #Reading fluorescence at 485 nm excitation and 520 nm emission 
    print("Reading the fluorescence at 485 nm excitation and 520 nm emission using the Biotek microplate reader")
  
    #Adding Cell Titer Glo 2.0 reagent 
    print("Adding 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube rack and dispensing it into A1 well of the 96 well white TC plate on Heater Shaker module")
  
    #Orbital shaking of the heater shaker 
    print("Setting the Heater shaker to orbital shaking at 500 rpm for 2 minutes")
  
    #Incubation at RT
    print("Incubating at RT for 10 minutes")
  
    #Reading the plate for luminescence 
    print("Reading the plate for luminescence using the Biotek microplate reader")
    

def main():
    setup_robot()
    seeding_cells()
    thapsigargin_additions()
    cell_viability_assay()
    
    
if __name__ == "__main__":
    main()


:*************************


