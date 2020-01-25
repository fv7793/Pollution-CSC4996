import spacy

#TODO:
    ##CREATE OUR OWN NAMED ENTITIES - subloc, watbod, chem, titles, units

ENT1 = "SUBLOC"
ENT2 = "BODWAT"
ENT3 = "CHEM"
ENT4 = "TITLE"
ENT5 = "UNIT"
ENT6 = "LOC"
ENT7 = "DATE"
ENT8 = "ORG"

#MIX IN EXAMPLES OF RECOGNIZED TYPES (ON TOP OF THE NEW ONES)
    #don't worry about the order, the training process shuffles I think
#MIX IN SENTENCES THAT CONTAIN NONE OF THESE ENTITIES AND TELL THE MODEL THAT
TRAIN_DATA = [
    #EXAMPLE FORMAT
    #("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
    
##CITIES------------------------------------- (LOC)
("Detroit residents and environmental groups are outraged over the handling of a potential uranium spill from a long-contaminated riverbank that collapsed into the Detroit River two days before Thanksgiving.", {"entities": [(0, 7, "LOC")]}),
("The Michigan Department of Environmental Quality found perfluoroalkyl and polyfluoroalkyl substances, known as PFAS, in water in New Baltimore, Mount Clemens and Ira Township, MLive reported.", {"entities": [(127, 140, "LOC"),(142, 155, "LOC"),(160, 172,"LOC")]}),
("Testing of private drinking wells near an airport southeast of Grand Rapids has found chemical contaminants after a report identified the airport's extensive use of toxic firefighting foam.", {"entities": [(62, 74, "LOC")]}),
("For more than 20 years, the Michigan town of Lapeer sent leftover sludge from its sewage treatment plant to area farms, supplying them with high-quality, free fertilizer while avoiding the expense of disposal elsewhere. ", {"entities": [(44, 50, "LOC")]}),
("The Livonia woman is one of many residents receiving testing by Ford to track pollution from the groundwater under the neighborhood, pollution that has sifted over from below the nearby Ford Transmission Plant at 36200 Plymouth Road.", {"entities": [(3, 10, "LOC")]}),
("Marie Gilreath has had enough of the testing in her Alden Village home.", {"entities": [(51, 65, "LOC")]}),
("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(137, 143, "LOC")]}),
("State pollution fighters just found a new worry at the site of hazardous waste nicknamed “green slime” in Madison Heights — and they were rushing Friday night to Detroit to property owned by the same polluter.", {"entities": [(105, 120, "LOC"),(161, 168, "LOC")]}),
("In Detroit, state environmental officials were on the way Friday night to a property that Sayers owned in Detroit, after Detroit firefighters identified potentially hazardous liquids at the location: 5900 Commonwealth St.", {"entities": [(2, 9, "LOC"),(105, 112, "LOC"),(120, 127, "LOC")]}),

##DATES-------------------------------------- (DATE)
("Detroit residents and environmental groups are outraged over the handling of a potential uranium spill from a long-contaminated riverbank that collapsed into the Detroit River two days before Thanksgiving.", {"entities": [(177, 205, "DATE")]}),
("The department issued letters March 2 alerting residents to the presence of the substances, which have been used in non-stick cookware, stain resistant fabrics and firefighting foams.", {"entities": [(29, 36, "DATE")]}),
("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(42, 48, "DATE")]}),
("In April, Lansing Township dropped the assessed value of Cupples’ home to zero, noting that the site was “contaminated property; levels exceed accepted levels.", {"entities": [(2, 7, "DATE")]}),
("A Department of Public Works crew's equipment may be the source of an oily sheen found in the Plumbrook Drain Jan. 17.", {"entities": [(109, 116, "DATE")]}),
("Interim City Manager and City Attorney David Gillam said he does not want to scare people, but that they should take seriously the public advisory about lead levels in the city’s water issued Oct. 29.", {"entities": [(191, 198, "DATE")]}),

##LOCATIONS (streets) -------------------------------------- (SUBLOC)
("The property at 5851 W. Jefferson was previously owned by Revere Copper and Brass, which was subcontracted in the 1940s to take part in the Manhattan Project, an undertaking to produce the first nuclear weapons.", {"entities": [(24, 33, "SUBLOC")]}),
("There are few signs left of the GM plants straddling Saginaw Road in Lansing Township.", {"entities": [(52, 64, "SUBLOC")]}),
("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(159, 173, "SUBLOC")]}),
("Toxic metals like mercury, chromium and lead are confirmed at high levels in the groundwater and sediment in the adjacent Rogue River, including at the spot where people regularly launch canoes and kayaks alongside the heavily-used White Pine Trail.", {"entities": [(130, 146, "SUBLOC")]}),
("In Detroit, state environmental officials were on the way Friday night to a property that Sayers owned in Detroit, after Detroit firefighters identified potentially hazardous liquids at the location: 5900 Commonwealth St.", {"entities": [(104, 119, "SUBLOC")]}),

##BODIES OF WATER --------------------------------------------- (BODWAT)
("Masse is worried the collapse could have contaminated the Detroit River and connecting waterways.", {"entities": [(57, 70, "BODWAT")]}),
("Submerged cables that carried electricity between Michigan's two peninsulas were shut down after leaking about 550 gallons of coolant fluid into the waterway that connects Lake Huron and Lake Michigan, officials said Tuesday.", {"entities": [(170, 180, "BODWAT"),(185, 198, "BODWAT")]}),
 ("It was too early to know what ecological damage might have been done in the Straits of Mackinac, said Joe Haas, district supervisor for the Michigan Department of Environmental Quality.", {"entities": [(75, 94, "BODWAT")]}),
 ("U.S. Rep. Rashida Tlaib (D-Detroit) released the following statement regarding the collapse of a contaminated site into the Detroit River near a water intake site", {"entities": [(123, 136, "BODWAT")]}),
 ("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(170, 183, "BODWAT")]}),
 ("Heavy rains last week caused roughly 11 million gallons of sewage and storm water to pour into the Grand and Red Cedar rivers.", {"entities": [(98, 123, "BODWAT")]}),
 ("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(330, 345, "BODWAT")]}),
 ("In the Rogue River, a surface water sample next to the site tested at 1,200-ppt for the individual PFAS compound PFOS, which was once the key ingredient in Scotchgard.", {"entities": [(6, 17, "BODWAT")]}),

##CHEMICALS----------------------------------------- (CHEM)
("Detroit residents and environmental groups are outraged over the handling of a potential uranium spill from a long-contaminated riverbank that collapsed into the Detroit River two days before Thanksgiving.", {"entities": [(88, 95, "CHEM")]}),
("The Michigan Department of Environmental Quality found perfluoroalkyl and polyfluoroalkyl substances, known as PFAS, in water in New Baltimore, Mount Clemens and Ira Township, MLive reported.", {"entities": [(54, 68, "CHEM"),(73, 88, "CHEM")]}),
("The company, which services Kalamazoo, Grand Rapids and Portage, found perfluorinated chemicals in four wells. The chemicals are often found in the firefighting foam.", {"entities": [(71, 94, "CHEM")]}),
("Submerged cables that carried electricity between Michigan's two peninsulas were shut down after leaking about 550 gallons of coolant fluid into the waterway that connects Lake Huron and Lake Michigan, officials said Tuesday.", {"entities": [(126, 138, "CHEM")]}),
("The fluid is a mineral-based synthetic oil used for insulation that can be harmful if released into the environment, said Jackie Olson, spokeswoman for American Transmission Co., which operates the cables.", {"entities": [(15, 41, "CHEM")]}),
("Testing has found elevated PFAS levels in just one field where the sludge was spread, but farmers have lost an economical fertilizer source and hope more contamination doesn't turn up.", {"entities": [(26, 30, "CHEM")]}),
("Scientists are finding mercury levels rising in large Great Lakes fish such as walleye and lake trout.", {"entities": [(22, 29, "CHEM")]}),
("Thanks to a concerned citizen, we were able to catch this flow of petroleum before the bulk of it made it to Lake St. Clair,” Macomb County Public Works Commissioner Candice Miller said in a press release.", {"entities": [(65, 74, "CHEM")]}),
("Chromium-6, a carcinogen, became well-known nationally after environmental activist Erin Brockovich discovered it in tap water in Hinkley, California in the 1990s.", {"entities": [(0, 9, "CHEM")]}),
("They proposed removing the pollution by injecting air into the water to encourage bacteria to gobble up the 1,4-dioxane, the pollutant lurking underground.", {"entities": [(107, 118, "CHEM")]}),
("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(34, 48, "CHEM")]}),
("Under the topsoil at the 15-acre site where Wolverine World Wide spent a hundred years using vast amounts of chemicals to convert animal hides into leather, high levels of volatile contaminants like vinyl chloride and trichloroethylene can be found.", {"entities": [(198, 212, "CHEM"),(217, 234, "CHEM")]}),
("Toxic metals like mercury, chromium and lead are confirmed at high levels in the groundwater and sediment in the adjacent Rogue River, including at the spot where people regularly launch canoes and kayaks alongside the heavily-used White Pine Trail.", {"entities": [(17, 24, "CHEM"),(26, 34, "CHEM"),(39, 43, "CHEM")]}),

##ORGANIZTIONS------------------------------------- (ORG)

("Sierra Club environmental organizer Justin Onwenu said in a news release." , {"entities": [(0, 11, "ORG")]}),
("Plainfield Township, the Saginaw-Midland Corp., Huron Shores Regional Water Authority system in Tawas, Ann Arbor, Grayling and the village of Sparta have also detected PFAS in their water.", {"entities": [(24, 44, "ORG"),(47, 91, "ORG")]}),
("WOOD-TV reports that Gordon Water Systems tested 20 wells at homes near the Gerald R. Ford International Airport in Kent County.", {"entities": [(20, 40, "ORG")]}),
("American Transmission Co. said the fluid can be harmful if released into the environment", {"entities": [(0, 23, "ORG")]}),
("The fluid is a mineral-based synthetic oil used for insulation that can be harmful if released into the environment, said Jackie Olson, spokeswoman for American Transmission Co., which operates the cables.", {"entities": [(151, 175, "ORG")]}),
("If you want to destroy agriculture in Michigan, start talking about, 'Hey, it could be contaminated with PFAS,' said Laura Campbell, agricultural ecology manager for the Michigan Farm Bureau.", {"entities": [(169, 189, "ORG")]}),
("Among them was Lapeer Plating & Plastics, the automotive chrome manufacturer that caused the Lapeer contamination.", {"entities": [(14, 39, "ORG")]}),
("My office has been in contact with the EPA’s Region 5 office as well as the Michigan Department of Environment, Great Lakes, and Energy", {"entities": [(38, 59, "ORG"),(74, 134, "ORG")]}),
("Detroit Bulk Storage and Revere Dock LLC have put their own profits ahead of the public’s well-being by not following processes that protect public health and our environment.", {"entities": [(0, 19, "ORG"),(24, 39, "ORG")]}),
("The mercury levels are not surpassing U.S. Environmental Protection Agency thresholds", {"entities": [(37, 73, "ORG")]}),
("Scientists only have hypotheses regarding why this is occurring. The trend of warming Great Lakes could be a factor, said Shane De Solla, an ecotoxicologist with Environment Canada and co-author on the recent study.", {"entities": [(161, 179, "ORG")]}),
("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(0, 37, "ORG")]}),
("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(126, 147, "ORG"),(170, 214, "ORG")]}),
("Crews from the Macomb County Public Works Office reportedly spent the day taking steps to “contain and absorb” the substance by setting up booms, or floating barriers.", {"entities": [(14, 47, "ORG")]}),
("The city of Sterling Heights is investigating whether the heavy machinery malfunctioned causing the discharge of hydraulic fluid and is fully cooperating with the MCPWO,” the statement reads.", {"entities": [(162, 167, "ORG")]}),

##OFFICIAL TITLES?------------------------------------- (TITLE)
("Sierra Club environmental organizer Justin Onwenu said in a news release." , {"entities": [(11, 34, "TITLE")]}),
("Last year, Gov. Rick Snyder announced that the state is committed to spending more than $23 million to combat PFAS contamination.", {"entities": [(10, 13, "TITLE")]}),
("Airport officials say they're investigating the contaminants but have no immediate plans to test neighboring wells.", {"entities": [(0, 16, "TITLE)]}),
("The fluid is a mineral-based synthetic oil used for insulation that can be harmful if released into the environment, said Jackie Olson, spokeswoman for American Transmission Co., which operates the cables.", {"entities": [(151, 175, "TITLE")]}),
("'We will continue to investigate the cause of the incident, determine any necessary remediation efforts and continue communicating with the appropriate regulatory agencies,' COO Mark Davis said.", {"entities": [(172, 175, "TITLE")]}),
("U.S. Rep. Rashida Tlaib (D-Detroit) released the following statement regarding the collapse of a contaminated site into the Detroit River near a water intake site", {"entities": [(0, 7, "TITLE")]}),
("Scientists only have hypotheses regarding why this is occurring. The trend of warming Great Lakes could be a factor, said Shane De Solla, an ecotoxicologist with Environment Canada and co-author on the recent study.", {"entities": [(141, 155, "TITLE")]}),
("Thanks to a concerned citizen, we were able to catch this flow of petroleum before the bulk of it made it to Lake St. Clair,” Macomb County Public Works Commissioner Candice Miller said in a press release.", {"entities": [(153, 164, "TITLE")]}),
("Bill Brunner, plant engineer at Lansing's waste water treatment facility, said during heavy rainfall, the combined water and sewer pipes cannot carry any more water and excess is channeled into the rivers.", {"entities": [(14, 27, "TITLE")]}),
("Pablo Valentin, an EPA remedial project manager for the site, said the meeting was a way to update residents on testing at the Rosemary Street site.", {"entities": [(23, 46, "TITLE")]}),
("'They’re well known because they're one of the few places that has taken this issue head-on,' said David Adamson, Principal Engineer with GSI Environmental in Houston, Texas.", {"entities": [(114, 131, "TITLE")]}),
("Kalamazoo County Environmental Health Director Vern Johnson said a survey of the area revealed there are no groundwater wells in use.", {"entities": [(17, 45, "TITLE")]}),

##UNITS-------------------------------------------------- (UNIT)

("Hundreds of gallons of coolant leaked into Lake Huron and Lake Michigan waterway", {"entities": [(11, 18, "UNIT")]}),
("Submerged cables that carried electricity between Michigan's two peninsulas were shut down after leaking about 550 gallons of coolant fluid into the waterway that connects Lake Huron and Lake Michigan, officials said Tuesday.", {"entities": [(115, 121, "UNIT")]}),
("About half of the 7 million tons generated annually in the U.S. is applied to farm fields and other lands, the Environmental Protection Agency says.", {"entities": [(28, 31, "UNIT")]}),
("Scientists are finding mercury levels rising in large Great Lakes fish such as walleye and lake trout.", {"entities": [(31, 36, "UNIT")]}),
("The EPA has found mercury in water has the potential to cause kidney damage from short-term exposures at levels above the maximum contaminant level of just 0.002 parts per million.", {"entities": [(162, 178, "UNIT")]}),
("The office estimated “between 75 and 100 gallons of petroleum entered the drain, causing containment booms to be put in place.", {"entities": [(41, 47, "UNIT")]}),
("Heavy rains last week caused roughly 11 million gallons of sewage and storm water to pour into the Grand and Red Cedar rivers.", {"entities": [(48, 54, "UNIT")]}),
("More than 10 million gallons poured into the Grand River and roughly 470,000 gallons into the Red Cedar River.", {"entities": [(22, 28, "UNIT")]}),
("Johnson said the latest results taken from monitoring wells found between 2 ppb and 4 ppb.", {"entities": [(76, 78, "UNIT")]}),
("Nearby, soil under a paved area between the existing Wolverine shoe depot store and the trail is contaminated by lead between 2.5 million and 11 million-ppb.", {"entities": [(145, 155, "UNIT")]})
