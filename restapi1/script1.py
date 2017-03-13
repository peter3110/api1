
from twitter import *

config = {
	"consumer_key" : "cKQFXpg98bIdU7irE2WH7EegG",
	"consumer_secret" :  "7xeB2gZbyPed2ij48SAF6lSJenjLStesWYSsqgHwxRMOcm81fo",
	"access_key": "2881028314-Sbuzxrk5xLigDdHDQj6a5PaK9x82ns7R7ZpbzBi",
	"access_secret" : "45mNxJ7gGFiV1jrpDTqRpp2uOnM9VsDX1OeyHGJXD3WVh"
}

def query1(username):
	twitter = Twitter(
			auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
	query = twitter.friends.ids(screen_name = username)

	result = [None] * len(query["ids"])
	
	for i in range(0, len(query["ids"])):
		ids = query["ids"][i]

		subquery = twitter.users.lookup(user_id = ids)

		for user in subquery:
			result[i] =  user["screen_name"]

	return result