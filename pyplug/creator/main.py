import re


def need_to_import(list_name: str) -> list:
	if list_name == "main":
		return [
			"import java.util.List;",
			"import java.util.logging.Logger;",
			"import org.bukkit.Bukkit;",
			"import org.bukkit.ChatColor;",
			"import org.bukkit.command.Command;",
			"import org.bukkit.command.CommandSender;",
			"import org.bukkit.entity.Player;",
			"import org.bukkit.event.EventHandler;",
			"import org.bukkit.event.EventPriority;",
			"import org.bukkit.event.Listener;",
			"import org.bukkit.event.player.AsyncPlayerChatEvent;",
			"import org.bukkit.event.player.PlayerJoinEvent;",
			"import org.bukkit.plugin.java.JavaPlugin;",
		]


def is_alphanumeric_str(text):
	if (re.match(r'^[A-Za-z0-9_]+$', text) != None):
		return True
	return False


def continue_cancel():
	while True:
		action = input("'continue' or 'cancel' process? Enter here: ")
		action = action.lower()
		if action == "continue":
			return True
		elif action == "cancel":
			return False
		else:
			continue
