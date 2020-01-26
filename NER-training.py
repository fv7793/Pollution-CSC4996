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
#TD1: Potential uranium spill in Detroit River alarms residents, environmental groups
("Detroit residents and environmental groups are outraged over the handling of a potential uranium spill from a long-contaminated riverbank that collapsed into the Detroit River two days before Thanksgiving.", {"entities": [(0, 7, "LOC")]}),
#TD2: Toxic chemicals found in New Baltimore, Mount Clemens, Ira Township drinking water
("The Michigan Department of Environmental Quality found perfluoroalkyl and polyfluoroalkyl substances, known as PFAS, in water in New Baltimore, Mount Clemens and Ira Township, MLive reported.", {"entities": [(127, 140, "LOC"),(142, 155, "LOC"),(160, 172,"LOC")]}),
#TD3: Testing finds contaminated wells near Grand Rapids-area airport
("Testing of private drinking wells near an airport southeast of Grand Rapids has found chemical contaminants after a report identified the airport's extensive use of toxic firefighting foam.", {"entities": [(62, 74, "LOC")]}),
#TD5: Concerns grow over tainted sewage sludge spread on Lapeer croplands
("For more than 20 years, the Michigan town of Lapeer sent leftover sludge from its sewage treatment plant to area farms, supplying them with high-quality, free fertilizer while avoiding the expense of disposal elsewhere. ", {"entities": [(44, 50, "LOC")]}),
#TD6: Alden Village residents still seeking help from Ford on polluted groundwater
("The Livonia woman is one of many residents receiving testing by Ford to track pollution from the groundwater under the neighborhood, pollution that has sifted over from below the nearby Ford Transmission Plant at 36200 Plymouth Road.", {"entities": [(3, 10, "LOC")]}),
#TD6: Alden Village residents still seeking help from Ford on polluted groundwater
("Marie Gilreath has had enough of the testing in her Alden Village home.", {"entities": [(51, 65, "LOC")]}),
#TD9: Officials search for source of petroleum leak into relief drain, Clinton River
("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(137, 143, "LOC")]}),
#T21: Green ooze case worsens as PFAS shown in water at site
("State pollution fighters just found a new worry at the site of hazardous waste nicknamed “green slime” in Madison Heights — and they were rushing Friday night to Detroit to property owned by the same polluter.", {"entities": [(105, 120, "LOC"),(161, 168, "LOC")]}),
#T21: Green ooze case worsens as PFAS shown in water at site
("In Detroit, state environmental officials were on the way Friday night to a property that Sayers owned in Detroit, after Detroit firefighters identified potentially hazardous liquids at the location: 5900 Commonwealth St.", {"entities": [(2, 9, "LOC"),(105, 112, "LOC"),(120, 127, "LOC")]}),

##DATES-------------------------------------- (DATE)
#TD1: Potential uranium spill in Detroit River alarms residents, environmental groups
("Detroit residents and environmental groups are outraged over the handling of a potential uranium spill from a long-contaminated riverbank that collapsed into the Detroit River two days before Thanksgiving.", {"entities": [(177, 205, "DATE")]}),
#TD2: Toxic chemicals found in New Baltimore, Mount Clemens, Ira Township drinking water
("The department issued letters March 2 alerting residents to the presence of the substances, which have been used in non-stick cookware, stain resistant fabrics and firefighting foams.", {"entities": [(29, 36, "DATE")]}),
#TD9: Officials search for source of petroleum leak into relief drain, Clinton River
("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(42, 48, "DATE")]}),
#TD11: EPA: Benzene contamination in Lansing Twp. not from our site
("In April, Lansing Township dropped the assessed value of Cupples’ home to zero, noting that the site was “contaminated property; levels exceed accepted levels.", {"entities": [(2, 7, "DATE")]}),
#TD17: Officials investigate Plumbrook Drain oil report
("A Department of Public Works crew's equipment may be the source of an oily sheen found in the Plumbrook Drain Jan. 17.", {"entities": [(109, 116, "DATE")]}),
#TD18: Royal Oak warns residents of 'action level' lead in water
("Interim City Manager and City Attorney David Gillam said he does not want to scare people, but that they should take seriously the public advisory about lead levels in the city’s water issued Oct. 29.", {"entities": [(191, 198, "DATE")]}),

##LOCATIONS (streets) -------------------------------------- (SUBLOC)
#TD1: Potential uranium spill in Detroit River alarms residents, environmental groups
("The property at 5851 W. Jefferson was previously owned by Revere Copper and Brass, which was subcontracted in the 1940s to take part in the Manhattan Project, an undertaking to produce the first nuclear weapons.", {"entities": [(24, 33, "SUBLOC")]}),
#T12: RACER Trust proposes fix for dioxane pollution in Lansing Township
("There are few signs left of the GM plants straddling Saginaw Road in Lansing Township.", {"entities": [(52, 64, "SUBLOC")]}),
#T13: Contamination plume leaves manufacturing property in Kalamazoo Township
("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(159, 173, "SUBLOC")]}),
#T15: Toxic pollution at Wolverine tannery is extensive, new report shows
("Toxic metals like mercury, chromium and lead are confirmed at high levels in the groundwater and sediment in the adjacent Rogue River, including at the spot where people regularly launch canoes and kayaks alongside the heavily-used White Pine Trail.", {"entities": [(130, 146, "SUBLOC")]}),
#TD21: Green ooze case worsens as PFAS shown in water at site
("In Detroit, state environmental officials were on the way Friday night to a property that Sayers owned in Detroit, after Detroit firefighters identified potentially hazardous liquids at the location: 5900 Commonwealth St.", {"entities": [(104, 119, "SUBLOC")]}),

##BODIES OF WATER --------------------------------------------- (BODWAT)
#TD1: Potential uranium spill in Detroit River alarms residents, environmental groups
("Masse is worried the collapse could have contaminated the Detroit River and connecting waterways.", {"entities": [(57, 70, "BODWAT")]}),
#TD4: Synthetic coolant leaks from power cables in Michigan waters
("Submerged cables that carried electricity between Michigan's two peninsulas were shut down after leaking about 550 gallons of coolant fluid into the waterway that connects Lake Huron and Lake Michigan, officials said Tuesday.", {"entities": [(170, 180, "BODWAT"),(185, 198, "BODWAT")]}),
#TD4: Synthetic coolant leaks from power cables in Michigan waters
 ("It was too early to know what ecological damage might have been done in the Straits of Mackinac, said Joe Haas, district supervisor for the Michigan Department of Environmental Quality.", {"entities": [(75, 94, "BODWAT")]}),
 #TD7: Tlaib statement on Revere Copper site collapse into Detroit River
 ("U.S. Rep. Rashida Tlaib (D-Detroit) released the following statement regarding the collapse of a contaminated site into the Detroit River near a water intake site", {"entities": [(123, 136, "BODWAT")]}),
 #TD9: Officials search for source of petroleum leak into relief drain, Clinton River
 ("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(170, 183, "BODWAT")]}),
 #TD10: 38 million gallons of sewage, storm water spilled into Grand and Red Cedar rivers this month
 ("Heavy rains last week caused roughly 11 million gallons of sewage and storm water to pour into the Grand and Red Cedar rivers.", {"entities": [(98, 123, "BODWAT")]}),
 #T13: Contamination plume leaves manufacturing property in Kalamazoo Township
 ("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(330, 345, "BODWAT")]}),
 #T15: Toxic pollution at Wolverine tannery is extensive, new report shows
 ("In the Rogue River, a surface water sample next to the site tested at 1,200-ppt for the individual PFAS compound PFOS, which was once the key ingredient in Scotchgard.", {"entities": [(6, 17, "BODWAT")]}),

##CHEMICALS----------------------------------------- (CHEM)
#TD1: Potential uranium spill in Detroit River alarms residents, environmental groups
("Detroit residents and environmental groups are outraged over the handling of a potential uranium spill from a long-contaminated riverbank that collapsed into the Detroit River two days before Thanksgiving.", {"entities": [(88, 95, "CHEM")]}),
#TD2: Toxic chemicals found in New Baltimore, Mount Clemens, Ira Township drinking water
("The Michigan Department of Environmental Quality found perfluoroalkyl and polyfluoroalkyl substances, known as PFAS, in water in New Baltimore, Mount Clemens and Ira Township, MLive reported.", {"entities": [(54, 68, "CHEM"),(73, 88, "CHEM")]}),
#TD3: Testing finds contaminated wells near Grand Rapids-area airport
("The company, which services Kalamazoo, Grand Rapids and Portage, found perfluorinated chemicals in four wells. The chemicals are often found in the firefighting foam.", {"entities": [(71, 94, "CHEM")]}),
#TD4: Synthetic coolant leaks from power cables in Michigan waters
("Submerged cables that carried electricity between Michigan's two peninsulas were shut down after leaking about 550 gallons of coolant fluid into the waterway that connects Lake Huron and Lake Michigan, officials said Tuesday.", {"entities": [(126, 138, "CHEM")]}),
#TD4: Synthetic coolant leaks from power cables in Michigan waters
("The fluid is a mineral-based synthetic oil used for insulation that can be harmful if released into the environment, said Jackie Olson, spokeswoman for American Transmission Co., which operates the cables.", {"entities": [(15, 41, "CHEM")]}),
#TD5: Concerns grow over tainted sewage sludge spread on Lapeer croplands
("Testing has found elevated PFAS levels in just one field where the sludge was spread, but farmers have lost an economical fertilizer source and hope more contamination doesn't turn up.", {"entities": [(26, 30, "CHEM")]}),
#TD8: Odd mercury spike found in Great Lakes fish
("Scientists are finding mercury levels rising in large Great Lakes fish such as walleye and lake trout.", {"entities": [(22, 29, "CHEM")]}),
#TD9: Officials search for source of petroleum leak into relief drain, Clinton River
("Thanks to a concerned citizen, we were able to catch this flow of petroleum before the bulk of it made it to Lake St. Clair,” Macomb County Public Works Commissioner Candice Miller said in a press release.", {"entities": [(65, 74, "CHEM")]}),
#TD11: EPA: Benzene contamination in Lansing Twp. not from our site
("Chromium-6, a carcinogen, became well-known nationally after environmental activist Erin Brockovich discovered it in tap water in Hinkley, California in the 1990s.", {"entities": [(0, 9, "CHEM")]}),
#TD12: RACER Trust proposes fix for dioxane pollution in Lansing Township
("They proposed removing the pollution by injecting air into the water to encourage bacteria to gobble up the 1,4-dioxane, the pollutant lurking underground.", {"entities": [(107, 118, "CHEM")]}),
#TD13: Contamination plume leaves manufacturing property in Kalamazoo Township
("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(34, 48, "CHEM")]}),
#TD15: Toxic pollution at Wolverine tannery is extensive, new report shows
("Under the topsoil at the 15-acre site where Wolverine World Wide spent a hundred years using vast amounts of chemicals to convert animal hides into leather, high levels of volatile contaminants like vinyl chloride and trichloroethylene can be found.", {"entities": [(198, 212, "CHEM"),(217, 234, "CHEM")]}),
#TD15: Toxic pollution at Wolverine tannery is extensive, new report shows
("Toxic metals like mercury, chromium and lead are confirmed at high levels in the groundwater and sediment in the adjacent Rogue River, including at the spot where people regularly launch canoes and kayaks alongside the heavily-used White Pine Trail.", {"entities": [(17, 24, "CHEM"),(26, 34, "CHEM"),(39, 43, "CHEM")]}),

##ORGANIZTIONS------------------------------------- (ORG)
#TD1: Potential uranium spill in Detroit River alarms residents, environmental groups
("Sierra Club environmental organizer Justin Onwenu said in a news release." , {"entities": [(0, 11, "ORG")]}),
#TD2: Toxic chemicals found in New Baltimore, Mount Clemens, Ira Township drinking water
("Plainfield Township, the Saginaw-Midland Corp., Huron Shores Regional Water Authority system in Tawas, Ann Arbor, Grayling and the village of Sparta have also detected PFAS in their water.", {"entities": [(24, 44, "ORG"),(47, 91, "ORG")]}),
#TD3: Testing finds contaminated wells near Grand Rapids-area airport
("WOOD-TV reports that Gordon Water Systems tested 20 wells at homes near the Gerald R. Ford International Airport in Kent County.", {"entities": [(20, 40, "ORG")]}),
#TD4: Synthetic coolant leaks from power cables in Michigan waters
("American Transmission Co. said the fluid can be harmful if released into the environment", {"entities": [(0, 23, "ORG")]}),
#TD5: Concerns grow over tainted sewage sludge spread on Lapeer croplands
("The fluid is a mineral-based synthetic oil used for insulation that can be harmful if released into the environment, said Jackie Olson, spokeswoman for American Transmission Co., which operates the cables.", {"entities": [(151, 175, "ORG")]}),
#TD5: Concerns grow over tainted sewage sludge spread on Lapeer croplands
("If you want to destroy agriculture in Michigan, start talking about, 'Hey, it could be contaminated with PFAS,' said Laura Campbell, agricultural ecology manager for the Michigan Farm Bureau.", {"entities": [(169, 189, "ORG")]}),
#TD5: Concerns grow over tainted sewage sludge spread on Lapeer croplands
("Among them was Lapeer Plating & Plastics, the automotive chrome manufacturer that caused the Lapeer contamination.", {"entities": [(14, 39, "ORG")]}),
#TD7: Tlaib statement on Revere Copper site collapse into Detroit River
("My office has been in contact with the EPA’s Region 5 office as well as the Michigan Department of Environment, Great Lakes, and Energy", {"entities": [(38, 59, "ORG"),(74, 134, "ORG")]}),
#TD7: Tlaib statement on Revere Copper site collapse into Detroit River
("Detroit Bulk Storage and Revere Dock LLC have put their own profits ahead of the public’s well-being by not following processes that protect public health and our environment.", {"entities": [(0, 19, "ORG"),(24, 39, "ORG")]}),
#TD8: Odd mercury spike found in Great Lakes fish
("The mercury levels are not surpassing U.S. Environmental Protection Agency thresholds", {"entities": [(37, 73, "ORG")]}),
#TD8: Odd mercury spike found in Great Lakes fish
("Scientists only have hypotheses regarding why this is occurring. The trend of warming Great Lakes could be a factor, said Shane De Solla, an ecotoxicologist with Environment Canada and co-author on the recent study.", {"entities": [(161, 179, "ORG")]}),
#TD9: Officials search for source of petroleum leak into relief drain, Clinton River
("The Macomb County Public Works Office said Jan. 4 that the search for the source of a petroleum spill into the Schoenherr Relief Drain in Warren, and subsequently into the Clinton River, is still ongoing.", {"entities": [(0, 37, "ORG")]}),
#TD13: Contamination plume leaves manufacturing property in Kalamazoo Township
("An existing contamination plume of vinyl chloride caused from historic releases of material has migrated off property owned by Borroughs Corporation at 3002 N. Burdick St. The Kalamazoo County Board of Commissioners will consider creating a groundwater use restriction zone around nine parcels between North Burdick Street and the Kalamazoo River to block the use of groundwater wells.", {"entities": [(126, 147, "ORG"),(170, 214, "ORG")]}),
#TD17: Officials investigate Plumbrook Drain oil report
("Crews from the Macomb County Public Works Office reportedly spent the day taking steps to “contain and absorb” the substance by setting up booms, or floating barriers.", {"entities": [(14, 47, "ORG")]}),
#TD17: Officials investigate Plumbrook Drain oil report
("The city of Sterling Heights is investigating whether the heavy machinery malfunctioned causing the discharge of hydraulic fluid and is fully cooperating with the MCPWO,” the statement reads.", {"entities": [(162, 167, "ORG")]}),

##OFFICIAL TITLES?------------------------------------- (TITLE)
#TD1: Potential uranium spill in Detroit River alarms residents, environmental groups
("Sierra Club environmental organizer Justin Onwenu said in a news release." , {"entities": [(11, 34, "TITLE")]}),
#TD2: Toxic chemicals found in New Baltimore, Mount Clemens, Ira Township drinking water
("Last year, Gov. Rick Snyder announced that the state is committed to spending more than $23 million to combat PFAS contamination.", {"entities": [(10, 13, "TITLE")]}),
#TD3: 3. Testing finds contaminated wells near Grand Rapids-area airport 
("Airport officials say they're investigating the contaminants but have no immediate plans to test neighboring wells.", {"entities": [(0, 16, "TITLE)]}),
#TD5: Concerns grow over tainted sewage sludge spread on Lapeer croplands
("The fluid is a mineral-based synthetic oil used for insulation that can be harmful if released into the environment, said Jackie Olson, spokeswoman for American Transmission Co., which operates the cables.", {"entities": [(151, 175, "TITLE")]}),
#TD4: Synthetic coolant leaks from power cables in Michigan waters
("'We will continue to investigate the cause of the incident, determine any necessary remediation efforts and continue communicating with the appropriate regulatory agencies,' COO Mark Davis said.", {"entities": [(172, 175, "TITLE")]}),
#TD7: Tlaib statement on Revere Copper site collapse into Detroit River 
("U.S. Rep. Rashida Tlaib (D-Detroit) released the following statement regarding the collapse of a contaminated site into the Detroit River near a water intake site", {"entities": [(0, 7, "TITLE")]}),
#TD8: Odd mercury spike found in Great Lakes fish
("Scientists only have hypotheses regarding why this is occurring. The trend of warming Great Lakes could be a factor, said Shane De Solla, an ecotoxicologist with Environment Canada and co-author on the recent study.", {"entities": [(141, 155, "TITLE")]}),
#TD9: Officials search for source of petroleum leak into relief drain, Clinton River
("Thanks to a concerned citizen, we were able to catch this flow of petroleum before the bulk of it made it to Lake St. Clair,” Macomb County Public Works Commissioner Candice Miller said in a press release.", {"entities": [(153, 164, "TITLE")]}),
#TD10: 38 million gallons of sewage, storm water spilled into Grand and Red Cedar rivers this month
("Bill Brunner, plant engineer at Lansing's waste water treatment facility, said during heavy rainfall, the combined water and sewer pipes cannot carry any more water and excess is channeled into the rivers.", {"entities": [(14, 27, "TITLE")]}),
#TD11: EPA: Benzene contamination in Lansing Twp. not from our site
("Pablo Valentin, an EPA remedial project manager for the site, said the meeting was a way to update residents on testing at the Rosemary Street site.", {"entities": [(23, 46, "TITLE")]}),
#TD12: RACER Trust proposes fix for dioxane pollution in Lansing Township
("'They’re well known because they're one of the few places that has taken this issue head-on,' said David Adamson, Principal Engineer with GSI Environmental in Houston, Texas.", {"entities": [(114, 131, "TITLE")]}),
#TD13: Contamination plume leaves manufacturing property in Kalamazoo Township
("Kalamazoo County Environmental Health Director Vern Johnson said a survey of the area revealed there are no groundwater wells in use.", {"entities": [(17, 45, "TITLE")]}),

##UNITS-------------------------------------------------- (UNIT)
#TD4: Synthetic coolant leaks from power cables in Michigan waters
("Hundreds of gallons of coolant leaked into Lake Huron and Lake Michigan waterway", {"entities": [(11, 18, "UNIT")]}),
#TD4: Synthetic coolant leaks from power cables in Michigan waters
("Submerged cables that carried electricity between Michigan's two peninsulas were shut down after leaking about 550 gallons of coolant fluid into the waterway that connects Lake Huron and Lake Michigan, officials said Tuesday.", {"entities": [(115, 121, "UNIT")]}),
#TD5: Concerns grow over tainted sewage sludge spread on Lapeer croplands
("About half of the 7 million tons generated annually in the U.S. is applied to farm fields and other lands, the Environmental Protection Agency says.", {"entities": [(28, 31, "UNIT")]}),
#TD8: Odd mercury spike found in Great Lakes fish
("Scientists are finding mercury levels rising in large Great Lakes fish such as walleye and lake trout.", {"entities": [(31, 36, "UNIT")]}),
#TD8: Odd mercury spike found in Great Lakes fish
("The EPA has found mercury in water has the potential to cause kidney damage from short-term exposures at levels above the maximum contaminant level of just 0.002 parts per million.", {"entities": [(162, 178, "UNIT")]}),
#TD9: Officials search for source of petroleum leak into relief drain, Clinton River
("The office estimated “between 75 and 100 gallons of petroleum entered the drain, causing containment booms to be put in place.", {"entities": [(41, 47, "UNIT")]}),
#TD10: 38 million gallons of sewage, storm water spilled into Grand and Red Cedar rivers this month
("Heavy rains last week caused roughly 11 million gallons of sewage and storm water to pour into the Grand and Red Cedar rivers.", {"entities": [(48, 54, "UNIT")]}),
#TD10: 38 million gallons of sewage, storm water spilled into Grand and Red Cedar rivers this month
("More than 10 million gallons poured into the Grand River and roughly 470,000 gallons into the Red Cedar River.", {"entities": [(22, 28, "UNIT")]}),
#TD13: Contamination plume leaves manufacturing property in Kalamazoo Township
("Johnson said the latest results taken from monitoring wells found between 2 ppb and 4 ppb.", {"entities": [(76, 78, "UNIT")]}),
#TD15: Toxic pollution at Wolverine tannery is extensive, new report shows
("Nearby, soil under a paved area between the existing Wolverine shoe depot store and the trail is contaminated by lead between 2.5 million and 11 million-ppb.", {"entities": [(145, 155, "UNIT")]})
