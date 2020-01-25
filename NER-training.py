import spacy

#TODO:
    ##CREATE OUR OWN NAMED ENTITIES - subloc, watbod, chem, titles, units

ENT1 = "SUBLOC"
ENT2 = "BODWAT"
ENT3 = "CHEM"
ENT4 = "TITLE"
ENT5 = "UNIT"

#MIX IN EXAMPLES OF RECOGNIZED TYPES (ON TOP OF THE NEW ONES)
    #don't worry about the order, the training process shuffles I think
#MIX IN SENTENCES THAT CONTAIN NONE OF THESE ENTITIES AND TELL THE MODEL THAT
TRAIN_DATA = [
    #EXAMPLE FORMAT
    #("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
##CITIES------------------------------------- (LOC)

##DATES-------------------------------------- (DATE)

##LOCATIONS (streets) --------------------------------------

##BODIES OF WATER ---------------------------------------------

##CHEMICALS-----------------------------------------

##ORGANIZTIONS------------------------------------- (ORG)

##OFFICIAL TITLES?-------------------------------------

##UNITS--------------------------------------------------
]
