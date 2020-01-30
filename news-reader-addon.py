# Add-on development first example

import globalPluginHandler
import tones # We want to hear beeps.
import speech
import ui
import requests

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_news():
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=baf6d4e18e8c43a88fc9d2a28e88fc13"
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
		ui.message(results[i])

	__gestures={
		"kb:tab": "news"
	}
