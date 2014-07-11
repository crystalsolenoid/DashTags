#leave this program running to
#collect a bunch of tags and frequencies
#from my dash!

#future plans:
#	save dictionary into text file?
#	display data
#	add top 10 longest tags to refresh output

#imports
import pytumblr #API for tumblr
import time #for time.sleep()
import operator #for operator.itemgetter()
import secret #put your own personal API keys here

#login to tumblr (purple-mustard)
client = pytumblr.TumblrRestClient(
	secret.API_KEY[0],
	secret.API_KEY[1],
	secret.API_KEY[2],
	secret.API_KEY[3])

#declaring stuff
dTags={} #keeps track of tag frequencies
lSeen=[] #remembers which posts are already seen

def printResults(tagDict): #(dictionary)
	#copy-pasted this next line from stackoverflow:
	lResults = sorted(tagDict.items(), key=operator.itemgetter(1),reverse=True)
	print "\n"
	print "all tags:"
	print tagDict
	print "\ntop 10:"
	for i in range(0,10):
		print str(tagDict[lResults[i][0]]) + " " + str(lResults[i][0])

def fixUpTag(tag): #(string)
	#remove //'s and trailing whitespace
	return tag.strip('/').strip(' ')

def addTag(tagDict,tag): #(dictionary, string)
	if tag in tagDict:
		tagDict[tag] += 1
	else:
		tagDict[tag] = 1
	return tagDict

while True:
	lDash = client.dashboard()["posts"] #grab posts from dash
	for dPost in lDash: #add tags to dictionary
		#ignore the post if already seen:
		if dPost["id"] in lSeen:
			continue #goes on to next item in for loop
		else:
			lSeen.append(dPost["id"])
		#count tags
		for sTag in dPost["tags"]:
			sTrimmedTag = fixUpTag(sTag)
			dTags = addTag(dTags,sTrimmedTag)
	printResults(dTags) #print results
	time.sleep(60) #wait this many seconds for refresh