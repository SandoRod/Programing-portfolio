# Band name generator
import random


titles = ["gigantic", "sour", "steamy", "gross", "stupid", 
	      "ironic", "greasy", "tangy", "smelly", "small",
	      "inventive", "spherical", "spiritual", "green",
	      "blue", "pot bellied", "pickled", "prickly"]

adjs =	["tiny", "fat", "shiny", "ecclectic", "fluffy", "bright",
	     "corrupt", "aggresive", "alarming", "amazing", "magical",
	     "courageous", "fierce", "colorless", "red", "thoughtless",
	     "smart", "delirious", "fabulous", "fergalicious", "dangerous"]

plural_nouns = ["apples", "oranges", "kiwis", "clementines",
				"wildabeasts", "mammoths", "rabbits", "sloths", "crashes",
				"spices", "eggs", "herbs", "pony tails", "bears", "snitches",
				"unicorns", "kermits", "signs", "indians", "cowboys", "cheerleaders"]

def title():
	''' This function chooses a random title for the name'''
	return random.choices(titles)

def adj():
	''' This funtion chooses a random tittle for the name'''
	return random.choice(adjs)

def plural_noun():
		return random.choice(plural_nouns)

def main():
	while True:
			name = raw_input("Enter your name")
			if name =="q":
				break
			random.seed(name)
			print title(), name, "and the", adj(), plural_noun()

main()