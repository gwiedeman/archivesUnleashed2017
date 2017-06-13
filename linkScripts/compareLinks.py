from bs4 import BeautifulSoup
import os
import json

linkCount = 0
menuLinks = [{"value": 0, "name": "Hard Links (http...)"}, {"value": 0, "name": "Relative Links"}]
contentLinks = [{"value": 0, "name": "Hard Links (http...)"}, {"value": 0, "name": "Relative Links"}]
hrefs = []

controlList = ["b", "small", "span", "h1,", "h2", "h3", "h4", "h5", "i"]

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
				parentTag = link.parent.name
				if parentTag.lower() == "li":
					if href.startswith("http"):
						for slice in menuLinks:
							if slice["value"] == "Hard Links (http...)":
								slice["value"] = slice["value"] + 1
					else:
						for slice in menuLinks:
							if slice["value"] == "Relative Links":
								slice["value"] = slice["value"] + 1
				elif patentTag.lower() =="div" or patentTag.lower() =="p":
					if href.startswith("http"):
						for slice in contentLinks:
							if slice["value"] == "Hard Links (http...)":
								slice["value"] = slice["value"] + 1
					else:
						for slice in contentLinks:
							if slice["value"] == "Relative Links":
								slice["value"] = slice["value"] + 1
				print contentLinks
				print menuLinks


inputData.close()

menuOut = "/home/ubuntu/archivesUnleashed2017/output/menuPaths.json"
outputFile1 = open(menuOut, "w")
json.dump(menuLinks, outputFile1)
outputFile1.close()

contentOut = "/home/ubuntu/archivesUnleashed2017/output/contentPaths.json"
outputFile2 = open(contentOut, "w")
json.dump(contentLinks, outputFile2)
outputFile2.close()
