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
