class UnknownCommand:
	@staticmethod
	def register():
		return {"imports": ["import org.bukkit.event.command.UnknownCommandEvent"], "recog-void": "onUnknownCommand", "recog-event": "UnknownCommandEvent e"}