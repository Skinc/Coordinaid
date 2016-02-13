from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACd69c33276c5f43dc74c458d6a05b3612" 
AUTH_TOKEN = "def0627db89d5df3de6b25ec89c499fc" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
client.messages.create(
	to="9524519109", 
	from_="+19782370602", 
	body="go chipotleloverrrrrr",  
)