from bs4 import BeautifulSoup
import os
import json

linkCount = 0
parents = []
hrefs = []

ignoreList = ["img"]
controlList = ["b", "small", "span", "h1,", "h2", "h3", "h4", "h5", "i"]

def controlCheck(element, controlList):
	if element.name.lower().strip() in controlList:
		controlCheck(element.parent, controlList)
	else:
		return element

resultsDir = "/home/ubuntu"
for folder in os.listdir(resultsDir):
	if "results_2017_London" in folder:
		fullPath = os.path.join(resultsDir, folder, "part-00000")


		inputData = open(fullPath, "rb")
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
				if len(link.parent) > 0:
					if link.parent.lower() in ignoreList:
						pass
					else:
					
						parentElement = controlCheck(link.parent)
					
						parentTag = parentElement.name			
						
						parentMatch = False
						for item in parents:
							if item["parents"] == parentTag:
								parentMatch = True
								item["count"] = item["count"]  + 1
						if parentMatch == False:
							parents.append({"count": 1, "parents": parentTag})
				
			print "Link Count: " + str(linkCount)
			pageCount += 1
			print "Page Count: " + str(pageCount)
			print parents


inputData.close()

outPath = "/home/ubuntu/archivesUnleashed2017/output/allWarcsContolled.json"
outputFile = open(outPath, "w")
json.dump(parents, outputFile)
outputFile.close()
