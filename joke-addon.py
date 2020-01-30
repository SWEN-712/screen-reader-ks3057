import globalPluginHandler
import tones
import ui
from random import randrange

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_doBeep(self, gesture):
		d = {1:"A perfectionist walked into a bar…apparently, the bar wasn’t set high enough.",
		2:"I ate a clock yesterday, it was very time-consuming.",
		3:"Did you hear about the crook who stole a calendar? He got twelve months.",
		4:"Did you hear about the semi-colon that broke the law? He was given two consecutive sentences.",
		5:"I woke up this morning and forgot which side the sun rises from, then it dawned on me."}

		var = randrange(1, len(d) + 1)
		ui.message(d[var])

	__gestures={
		"kb:NVDA+A": "doBeep"
	}
