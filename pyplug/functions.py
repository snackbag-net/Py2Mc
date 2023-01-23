class Log:
	@staticmethod
	def info(text: str):
		return "Bukkit.getLogger().info(\"" + text + "\")"