import opentrons

start_time = datetime.datetime.now()
three_ml_tb = [opentrons.load_module('name_of_your_tube_mill').load_channel(1),
opentrons.load_module('name_of_your_tube_rack').load_channel(4)]
two_ml_tube = [opentrons.load_module('name_of_your_tube_rack').load_channel(2)]
pbs = opentrons.load_module("dunecoengineering_96_reservoir_15ml").load_channel(1)
dest = opentrons.load_module("hapiware_24_cell_culture_dish", 5)
trypsin = pbs.load_module("hapiware_96_tuberack_5ml").load_channel(1)
cell_medium = pbs.load_module("hapiware_96_tuberack_5ml").load_channel(3)

def pick_up():
 trypsin.flow_rate.aspirate = 100
 trypsin.flow_rate.dispense = 25

def replace_medium():
 dest.culture_medium.top().bottom().remove().insert(3.0,
cell.ME112 medium)


def finalize(e):
 print(e)

def protocol(steps):

metadata = {
    'Author': 'Steve oh',
    'Title': 'Cell Protocol Sample',
    'Description': 'Cell protocol sample',
    'Protocol Steps': steps
    }


protocol = [
    [pick_up()],
    [replace_medium()],
    [finalize()]
    ]


extensions = [
    [
        "on_deck"
       ]
    ]

def run(ctx):
    ctx.comment('''
   --- STARTING THE PROTOCOL ---
   ''')
    for s, d, f in protocol:
        ctx.comment('''
   --- STEP {}: {} ---
   '''.format(s, d))
        ctx.delay(seconds=10)
        d.set_volume(3.0)
    ctx.comment('''
   --- FINAL STEP: PERFORM BIAS ----
   ''')
    for e in extensions:
        ctx.comment('''
   --- FINAL STEP {}: {} -----
    '''.format(e, f))
    ctx.comment('''
    --- ENDING THE PROTOCOL ---
   ''')
   

run(protocol)

END

end

Depending on your experimental requirements, you can automate your entire experiment in a few hours.





:*************************


import lxml.html
from opentrons.protocol_api. import python_api

def run ( protocol ):

def definition_block ():
 """Creating definition block"""
 return {
    'description': 'Cell medium change',
    'protocol_description': '''Can you please write a Python script or
opentrons job that runs the wet experiment for me?''',
    'steps': definition_block().get_children()
}

def run_script ():
    # print('''OUTPUT''')
    print ( '' '''')
    print ( '' '''' )
    print ( '' '' )
    print ( '' '''')
    print ( '' '''')
    print ( '' '' )
    return run(definition_block())



function definitions = {
    'wash': '2',
    'down': '5',
    'up': '2', 
    'epsin': '0.25%',
    'cell_med_dm': '10 ml',
    'start_block': 'begin'
    }



def execute_function ( *args ):
    """
    Decorator to execute function
    """

    def decorate ( func ):

        @wraps ( func )
        def wrapper (*args , **kw ):

            if isinstance ( args [ 0 ], int ):

                start = int ( args [ 0 ]) - 1
            else :

                 start = args [ 0 ]

            if not protocol . is_in_progress ():
                 try :
                protocol . set_block ( start + wrap ( func ))
            except :
            protocol . error ( '''Oopss!!! Please enter the right block number
before running the experiment again''')
        protocol . pause ()

    if definition_block () in protocol . blocks :
        protocol . call_extensions ( protocol . blocks [ definition_block ()])

    def definition_block_metadata ():
        return {
            'description': 'cell medium change',
            'steps': definition_block().get_children()
        }



def run_script ( interface ):
    try :
        from opentrons.dal import py2exe
        except :
            sys . exit ( 'python2.7 OR python2.6.14 must be installed!' )
        exec ( py2exe . build ( run_script ,
                           'console_scripts' ,
                          'pkg_resources' ))

The definitions are passed as decorator arguments. I will let you run them in the protocol



def cellmed_change ( time ):
    """
    Step definitions (party tricks - 1)
    """
    d = definitions . copy ()
    def return_days_old ():
        d = d + {}
        r = start_block + '''for five minutes'''
        return r + ''' into the 50 ml tube. Then, use 2 ml of PBS(-) for
the five-minute wash'''
    d [ 'cell_wash'] = return_days_old ()
    r = run_script ( cellmed_change )  # ----^

    d [ 'begin'] = start_block
    return d



def cellmed_change ( **kwargs ):
    """
    Step definitions (party tricks - 2)
    """
    print ( kwargs )

    # print('''OUTPUT''')
    print ( '' '''')
    print ( '' '''' )
    print ( '' '' )
    print ( '' '''')
    print ( '' '''' )
    print ( '' '''')
    print ( '' '' )
    return [ protocol . call_function ( cellmed_change . func_name , *
            args ) for cellmed_change in kwargs . get ( 'cellmed_change' , [])]

Before running the experiment, run the cells-medium-change script using the wetware
interactor. That's it.

The protocol will ask for variables to enter the experiment (the script will request a )




:*************************


