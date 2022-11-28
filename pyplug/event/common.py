class DefineEventPlayer:
	@staticmethod
	def python():
		return "eventPlayer"

	@staticmethod
	def java():
		return "Player eventPlayer = event.getPlayer();"


def cancel(boolean: bool = True) -> str:
	if boolean is False:
		return "event.setCancelled(false);"
	elif boolean is True:
		return "event.setCancelled(true);"
	else:
		return ""

