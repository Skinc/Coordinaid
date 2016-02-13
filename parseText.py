import indicoio
import operator
import pickle
import time 
entities = ["redcross", "refuaid", "un"]
locationOrg = {"Lesbos": "redcross", "Munich": "germangov" }
indicoio.config.api_key = 'b94312524aff44f47c4cc57b9e56c5e6'

# pickle.dump( users, open( "users.p", "wb" ) )
qs = {"Where do I find water?": {"answer": "At the bubbler", "expiration": time.time() + 100, "org": "redcross"}, "What time is sunset?": {"answer": "6pm", "expiration": time.time() + 10000, "org": "un"}}
pickle.dump( qs, open( "questions.p", "wb" ) )

#returns entity 
def entityMatch(message):
	ne = indicoio.named_entities(message)
	for e in ne.keys():
		if ne[e]["confidence"] > .8:
			if ne[e]["categories"]["organization"] > .5:
				if e in entities:
					return e
	return "None"
#returns entity based onw hat is needed
def entityMatchSkill():
	return 0

def ticketCreate(message, number, entity):
	print "creating ticket" + message+number+entity

def store(message, number):
	print "Storing message:"
	print "Number: " + number
	print "Message: " + message

def analyzeUser(number):
	print "Getting all info for:" + number
	return {"messages": 12, "languageLevel": 3 }

#true if prev answer anseers
def comparePrev(message, number):
	prev = pickle.load( open( "questions.p", "rb" ))
	if message in prev.keys():
		if time.time() < prev[message]["expiration"]:
			print "answer found:"
			print prev[message]["answer"]
			return True
		else:
			print "print answer out of date, sending to org again"
			ticketCreate(message, number, prev[message]["org"])
			return True
	else:
		print "no prev messages"
		return False

def parse(message, number):
	store(message, number)
	userProf = analyzeUser(number)

	if comparePrev(message, number):
		return "Message Sent"
	else:
		ent = entityMatch(message)
		if  ent == "None":
			print "keywords"
			print indicoio.keywords(message, version=2)
			print "tags"
			print indicoio.text_tags(message, threshold = .03)
			print "relevance"
			print indicoio.relevance("Renowned soccer legend Pele will be visiting...", ["Germany", "relocation", "Food", "Safety", "Family", "Transportation", "clothing"])

		else:
			"Found Entity, directing there"
			ticketCreate(message, number, ent)


# m = "Hello, I am looking for a way to see where my family has settled in Germany. Who do I talk to?"
m = "I am travelling to Munich next, where do I go there to find a job?"
parse(m , "1234566789")

# namedEntity recognizes names and orgs
# relevance
# sentiment



