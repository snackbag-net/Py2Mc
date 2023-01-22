class PlayerJoinEvent:
	@staticmethod
	def register():
		return_item = {
			"need": ["import org.bukkit.event.player.PlayerJoinEvent", "player_join_event"]
		}
		return return_item

	@staticmethod
	def set_join_message(join_message: str) -> str:
		return f"event.setJoinMessage(\"{join_message}\")"
