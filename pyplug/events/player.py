class AdvancementDone:
	@staticmethod
	def register():
		return {"imports": ["import org.bukkit.event.player.PlayerAdvancementDoneEvent", "import org.bukkit.advancement.Advancement"], "recog-void": "onAdvancementDone", "recog-event": "AdvancementDoneEvent event, Player eventPlayer"}

	value_advancement = "advancement"
	value_event = "event"

	class GetAdvancement:
		@staticmethod
		def value():
			return "event.getAdvancement()"

		@staticmethod
		def display():
			return "event.getAdvancement().getDisplay()"

		@staticmethod
		def description():
			return "event.getAdvancement().description()"

		@staticmethod
		def title():
			return "event.getAdvancement().title()"

class Join:
	@staticmethod
	def register():
		return {"imports": ["import org.bukkit.event.player.PlayerJoinEvent"], "recog-void": "onPlayerJoin", "recog-event": "PlayerJoinEvent event"}

	value_advancement = "advancement"
	value_event = "event"

	@staticmethod
	def set_joinmsg(message):
		return "event.setJoinMessage(\"" + message + "\")"