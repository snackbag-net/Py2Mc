package me.yourname.showcase;

import java.util.List;
import java.util.logging.Logger;
import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.plugin.java.JavaPlugin;


public final class MainTest extends JavaPlugin {
	@Override
	public void onEnable() {
		Bukkit.getLogger().info("Startup");
		Bukkit.getLogger().warning("This is a startup message, §cyou can put as many as you want!");
	}

	@Override
	public void onDisable() {
		Bukkit.getLogger().info("Goodbye!");
		Bukkit.getLogger().info("Here too.");
	}
}
