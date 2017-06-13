from bs4 import BeautifulSoup
import os

linkCount = 0
parents = []
hrefs = []

controlList = ["b", "small", "span", "h1,", "h2", "h3", "h4", "h5", "i"]

rawFile = "/home/ubuntu/results_2017_London/part-00000"

inputData = open(rawFile, "rb")
inputText = inputData.read()

startFix = "<html>" + inputText.split("<html>", 1)[1]
endFix = startFix.rsplit("</html>", 1)[0] + "</html>"

pageCount = 0
for thing in endFix.split("<html>"):
	page = "<html>" + thing
	soup = BeautifulSoup(page)
	for link in soup("a"):
		linkCount += 1
		href = link.get('href', None)
		hrefs.append(href)
		parentTag = link.parent.name
		
		parentMatch = False
		for item in parents:
			if  parentTag in item:
				parentMatch = True
				item[1] = item[1] + 1
		if parentMatch == False:
			parents.append([parentTag, 1])
		
	print "Total Links: " + str(linkCount)
	pageCount += 1
	print pageCount
	print parents


inputData.close()


