import indicoio
import operator



indicoio.config.api_key = 'b94312524aff44f47c4cc57b9e56c5e6'

# single example
#print indicoio.keywords("Where do I get food in Lesbos?", version=2)
#returns the words that are deemed most relevant
print indicoio.relevance("Where do I get food in Lesbos?", ["food", "general_food"]) 
#returns list of proportions representing how relevant the word is to the string
keyword_dictionary = indicoio.text_tags("Where do I get food in Lesbos?")
top_word = max(keyword_dictionary.iteritems(), key=operator.itemgetter(1))[0]
keyword_dictionary.pop(top_word)
second_top_word = 




# batch example
#print indicoio.keywords([
#    "How do I get water nearby?",
#    "Where did my family go?"
#], version=2)
#returns the words that are deemed most relevant
#print indicoio.relevance(["How do I get water nearby?", "Where did my family go?"], ["family"])
#returns list of proportions representing how relevant the word is to the string
#print indicoio.text_tags([
#    "The most common form of arrow consists of a shaft with an arrowhead attached to the front end and with fletchings and a nock attached to the other end.",
#    "Yoga in Indian traditions, however, is more than physical exercise, it has a meditative and spiritual core."
#])