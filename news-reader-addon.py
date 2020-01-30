# Add-on development first example

import globalPluginHandler
import tones
import speech
import ui
import requests

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_news():
	    url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=baf6d4e18e8c43a88fc9d2a28e88fc13"
	    open_bbc_page = requests.get(url).json()
	    articles = open_bbc_page["articles"]
	    results = []

	    for ar in articles:
		results.append(ar["title"])

	    for i in range(len(results)):
			ui.message(results[i])

		__gestures={
			"kb:NVDA+A": "news"
		}
