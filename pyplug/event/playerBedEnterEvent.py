def register():
	return_item = {
		"need": ["import org.bukkit.event.player.PlayerBedEnterEvent", "player_bed_enter_event"]
	}
	return return_item


def set_join_message(join_message: str, to: str = None) -> str:
	if to is None:
		return f"event.setJoinMessage(\"{join_message}\")"
	else:
		return f"event.setJoinMessage(\"{join_message}\").to{to}"