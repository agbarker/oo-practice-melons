############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk_melon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk_melon.add_pairing("mint")
    all_melon_types.append(musk_melon)

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing("poscuitto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    #get melon name

    #get melon pairing(s)  (for loop?)

    #format printing
    for melon in melon_types:
        name = melon.name
        print name + " pairs with"

        pairings = melon.pairings


        for pairing in pairings:
            print "- " + pairing


    # return None

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #create empty dictionary

    #for each melon in melon list, create keys, set value to code melon[i][0]
    melon_codes = {}

    for melon in melon_types:
        melon_codes[melon.code] = melon

    return melon_codes

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



class Melon(object):
    """A species of melon at a melon farm."""

    def __init__(self, type, shape_rating, color_rating, field, harvester):
        """Initialize a melon."""
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

        # Fill in the rest

    def is_sellable(melon, rating = 5):
        """Returns True or False if melon is sellable"""

        if melon.shape_rating > rating and melon.color_rating > rating and field != 3:
            return True




melons = make_melon_types()

print_pairing_info(melons)

print make_melon_type_lookup(melons)