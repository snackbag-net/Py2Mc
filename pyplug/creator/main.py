import re
import sys

import pyplug.event.common


def need_to_import(list_name: str) -> list:
	if list_name == "main":
		return [
			"import java.util.logging.Logger;",
			"import org.bukkit.Bukkit;",
			"import org.bukkit.ChatColor;",
			"import org.bukkit.command.Command;",
			"import org.bukkit.command.CommandSender;",
			"import org.bukkit.entity.Player;",
			"import org.bukkit.plugin.java.JavaPlugin;",
		]


def code_event(list_name: list, register: dict, package) -> str:
	event = list_name[0]
	event_name = list_name[1]
	name = register["name"]
	tabindex = 0
	tab = "\t"
	imports = [
		"import org.bukkit.entity.Player;",
		"import org.bukkit.event.EventHandler;",
		"import org.bukkit.event.Listener;",
	]

	if event_name == "player_join_event":
		print(register["execute"])
		imports.append(event)
		return_code = []
		return_code.append("package " + package + ";")
		return_code.append(tab * tabindex + "\n".join(imports))
		return_code.append(tab * tabindex + f"\npublic class {name} implements Listener " + "{")
		tabindex = tabindex + 1
		return_code.append(tab * tabindex + "\n@EventHandler")
		return_code.append(tab * tabindex + "public static void onPlayerJoin(PlayerJoinEvent event) {")
		tabindex = tabindex + 1
		return_code.append(tab * tabindex + f"\n{tab*tabindex}".join(register["execute"]))
		tabindex = tabindex - 1
		return_code.append(tab * tabindex + "}")
		tabindex = tabindex - 1
		return_code.append(tab * tabindex + "}")

		return "\n".join(return_code)


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
