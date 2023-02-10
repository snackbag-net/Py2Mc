class DefEventPlayer:
	@staticmethod
	def python():
		return {"imports": None, "return_value": "eventPlayer"}

	@staticmethod
	def java():
		return {"imports": None, "return_value": "Player eventPlayer = event.getPlayer()"}

def cancel(boolean: bool = True):
	if boolean is False:
		return {"imports": None, "return_value": "event.setCancelled(false)"}
	else:
		return {"imports": None, "return_value": "event.setCancelled(true)"}