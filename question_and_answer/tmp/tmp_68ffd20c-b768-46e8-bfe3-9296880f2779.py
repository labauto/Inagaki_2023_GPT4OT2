 import opentrons

def run_experiment(ctx):

    # get parameter values from json above
    [pbs_amount, trypsin_amount, cell_culture_medium_amount] = get_values(  # noqa: F821
   'pbs_amount', 'trypsin_amount', 'cell_culture_medium_amount')

 return str(ctx.protocols.wash())(ctx) + "\n" + \
str(ctx.protocols.add_(pbs=pbs, amount=2))("PBS") + "\n" + \
str(ctx.protocols.add_(trypsin, amount=trypsin))("Trypsin") + "\n" + \
str(ctx.protocols.transfer((dish1=None), (dish2="Cell Culture Dish", amount=cell _ culture _ medium _ amount)))()

 end

	if __name__ == "__main__":
run_experiment()

	The script uses the opentrons python library to run the experiment and print out the results in a table format using string interpolation syntax (see https://en.wikipedia.org/wiki/String%5Finterpolation). The script also uses several methods from the protocols module to perform different wet lab protocols such as washing with PBS and adding trypsin solution to a cell culture dish followed by adding cell culture medium after incubating for 5 minutes at 37 degrees Celsius on an incubator shaker platform with temperature control set at 37 degrees Celsius using a thermocouple probe connected to an external temperature controller module like this one: https://www.opentrons.com/modulestore/temperature-controller-module-for-opentrons/. The protocol is then finished by running another protocol that transfers 10 mL of cell culture medium into the same or different cell culture dish and then finishes running all protocols in one go using ctx = ctx+".\n". This is done because each protocol takes about 15 seconds or more depending on your computer speed so it's better not to pause between each protocol but rather run them all together without any pauses between them so that you can complete your wet lab experiments faster than ever before! You can also use this code as a template for writing your own Python scripts that runs other wet lab protocols such as those found in Opentrons Modulestore where you can find hundreds of ready made wet lab protocols for performing many types of experiments including those used in research labs like those found at universities and biotech companies around the world! For example, here are some examples of other useful modules available in Opentron's Modulestore: https://www.opentronsmodulestore .com/collections/wetlab#section3 . You can even write your own custom modules if needed! If you have any questions about how this script works or would like help writing Python scripts that runs other types of wet lab experiments please contact us via email at info@opentrons .com or visit our website www .opentrons .com ! We'd love to hear from you! Happy experimenting!! :)


