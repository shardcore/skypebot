# coding=UTF-8

from string import Template
import random

class DrinkCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("begrudgingly serves $name $drink."),
							Template("ostentatiously prepares $name $drink and pockets the change."),
							Template("eyeballs $name for a moment, then shoves $drink across the bar."),
							Template("fills up $drink for $name from the drips tray."),
							Template("waves his hands and $drink appears in front of $name in a puff of sulphurous smoke."),
							Template("extrudes a pseudopod in the direction of $name, bearing $drink."),
							Template("points out that $name has had enough already (drunk)"),
							Template("does his best Tom Cruise impression and mixes a $drink into a tall glass for $name."),
							Template("stops watching the sports for a minute. Long enough to top up a $drink for $name."),
							Template("suggests that $name can go somewhere else if they want a $dirnk. Disgusting drink."),
							Template("longs for closing time."),
							Template("calls the law. $name was caught doing lewd acts in the toilets."),
							Template("shakes a fresh $drink all over $name's nice new face."),
							Template("calmly explains to $name that $drink was always there, and vanishes.")
							]
		
		self.pre_modifiers = [ "half a",
				   "a stingy",
				   "a watery",
				   "a pitcher of",
				   "a cloudy",
				   "a glitchy",
				   "an horrific",
				   "a most erotic",
				   "a quart of",
				   "a fur-lined",
				   "a luminous",
				   "an acid-laced",
				   "the opposite of a" ]				
		
		self.drinks = [ "Beer",
			"Ale",
			"Bongwater",
			"Barleywine",
			"Bloody Mary",
			"Delirium Tremens",
			"Bitter ale",
			"Mild ale",
			"Pale ale",
			"Porter",
			"Stout",
			"Cask ale",
			"Stock ale",
			"Fruit Beer",
			"Lager beer",
			"Bock",
			"Dry beer",
			"Maerzen",
			"Pilsener",
			"Schwarzbier",
			"Sahti",
			"Small beer",
			"Wheat beer",
			"Witbier White Beer",
			"Hefeweizen",
			"Cauim",
			"Four Roses Bourbon"
			"Chicha",
			"Cider",
			"Huangjiu",
			"Icariine Liquor",
			"Kilju",
			"Kumis",
			"Lappish Hag's Love Potion",
			"Mead",
			"Palm wine",
			"Perry",
			"Plum jerkum",
			"Pulque",
			"Sake",
			"Sonti",
			"Tepache",
			"Tonto",
			"Tiswin",
			"Wine",
			"Fruit wine",
			"Table wine",
			"Sangria",
			"Champagne",
			"Port",
			"Madeira",
			"Marsala",
			"Sherry",
			"Vermouth",
			"Vinsanto",
			"Absinthe",
			"Akvavit",
			"Arak",
			"Arrack",
			"Baijiu",
			"Cachaca",
			"Gin",
			"Damson gin",
			"Sloe gin",
			"Gulu",
			"Horilka",
			"Kaoliang",
			"Maotai",
			"Mezcal",
			"Ogogoro",
			"Ouzo",
			"Palinka",
			"Pisco",
			"Rakia",
			"Slivovitz",
			"Rum",
			"hot chocolate"
			"PG Tips"
			"Soju",
			"Tequila",
			"Vodka",
			"Metaxa",
			"Whisky",
			"Bourbon",
			"Scotch",
			"Tennessee whiskey",
			"Brandy",
			"Armagnac",
			"Cognac",
			"Damassine",
			"Himbeergeist",
			"Kirsch",
			"Poire Williams",
			"Williamine",
			"Zwetschgenwasser",
			"Lambrini",
			"Paint thinner",
			"Grog",
			"Moonshine",
			"Cider",
			"Scrumpy" ]

	def execute( self, message ):
		drink = random.choice( self.drinks )
		pre_modifier = random.choice( self.pre_modifiers )
		if(pre_modifier[-1].lower() == 'a') and (drink[:1].lower()=='a'):
			pre_modifier += "n"
		drink = "%s %s" % (pre_modifier, drink)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, drink=drink)
		return "/me %s" % message_out
		

	
