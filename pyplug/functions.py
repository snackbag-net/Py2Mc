import pyplug.storage as store

class Log:
	@staticmethod
	def info(text: str):
		return {"imports": ["import org.bukkit.Bukkit"], "return_value": "Bukkit.getLogger().info(\"" + text + "\")"}

	@staticmethod
	def warn(text: str):
		return {"imports": ["import org.bukkit.Bukkit"], "return_value": "Bukkit.getLogger().warning(\"" + text + "\")"}

class Commons:
	@staticmethod
	def java_do_nothing():
		return {"imports": None, "return_value": "if (\"\".isEmpty()) {} // do nothing"}

class ExperimentalCommons:
	@staticmethod
	def toStr():
		return {"imports": None, "return_value": ".toString()"}

	@staticmethod
	def fix_val(*args, imports: list = None):
		return_value = ""
		for arg in args:
			return_value = return_value + arg['return_value']

		return {"imports": imports, "return_value": return_value}

class Player:
	@staticmethod
	def force_cmd(python_player: str, command: str):
		return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".performCommand(\"" + command + "\")"}

	@staticmethod
	def ban(python_player: str, reason: str):
		return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".banPlayer(\"" + reason + "\")"}

	@staticmethod
	def kick(python_player: str, reason: str):
		return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".kickPlayer(\"" + reason + "\")"}

	class Get:
		@staticmethod
		def name(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getName()"}

		@staticmethod
		def address(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getAddress()"}

		@staticmethod
		def allow_fly(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getAllowFlight()"}

		@staticmethod
		def bed_spawn(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getBedSpawnLocation()"}

		@staticmethod
		def client_brand(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getClientBrandName()"}

		@staticmethod
		def client_view(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getClientViewDistance()"}

		@staticmethod
		def cooldown(python_player: str, item: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getCooldown(" + item + ")"}

		@staticmethod
		def xp(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getExp()"}

		@staticmethod
		def speed_fly(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getFlySpeed()"}

		@staticmethod
		def health(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getHealth()"}

		@staticmethod
		def level(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLevel()"}

		@staticmethod
		def ptime(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPlayerTime()"}

		@staticmethod
		def ptime_offset(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPlayerTimeOffset()"}

		@staticmethod
		def pweather(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPlayerWeather()"}

		@staticmethod
		def prev_gamemode(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPreviousGameMode()"}

		@staticmethod
		def resource_pack_status(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getResourcePackStatus()"}

		@staticmethod
		def scoreboard(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getScoreboard()"}

		@staticmethod
		def simulation_distance(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getSimulationDistance()"}

		@staticmethod
		def spec_target(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getSpectatorTarget()"}

		@staticmethod
		def total_xp(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getTotalExperience()"}

		@staticmethod
		def view_distance(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getViewDistance()"}

		@staticmethod
		def speed_walk(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getWalkSpeed()"}

		@staticmethod
		def world(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getWorld()"}

		@staticmethod
		def display_name(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getDisplayName()"}

		@staticmethod
		def locale(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLocale()"}

		@staticmethod
		def tab_footer(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPlayerListFooter()"}

		@staticmethod
		def tab_header(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPlayerListHeader()"}

		@staticmethod
		def tab_name(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPlayerListName()"}

		@staticmethod
		def resource_pack_hash(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getResourcePackHash()"}

		@staticmethod
		def absorption_amount(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getAbsorptionAmount()"}

		@staticmethod
		def active_item(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getActiveItem()"}

		@staticmethod
		def active_effects(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getActivePotionEffect()"}

		@staticmethod
		def arrow_cooldown(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getArrowCooldown()"}

		@staticmethod
		def arrows_in_body(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getArrowsInBody()"}

		@staticmethod
		def arrows_stuck(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getArrowsStuck()"}

		@staticmethod
		def attack_cooldown(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getAttackCooldown()"}

		@staticmethod
		def bed_loc(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getBedLocation()"}

		@staticmethod
		def bee_stingers_in_body(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getBeeStingersInBody()"}

		@staticmethod
		def can_pickup(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getCanPickupItems()"}

		@staticmethod
		def chunk(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getChunk()"}

		@staticmethod
		def entity_id(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getEntityID()"}

		@staticmethod
		def xp_to_level(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getExpToLevel()"}

		@staticmethod
		def eye_height(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getEyeHeight()"}

		@staticmethod
		def eye_loc(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getEyeLocation()"}

		@staticmethod
		def facing(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getFacing()"}
		
		@staticmethod
		def fall_dist(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getFallDistance()"}

		@staticmethod
		def fire_ticks(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getFireTicks()"}

		@staticmethod
		def food_level(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getFoodLevel()"}

		@staticmethod
		def freeze_ticks(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getFreezeTicks()"}

		@staticmethod
		def gamemode(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getGameMode()"}

		@staticmethod
		def height(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getHeight()"}

		@staticmethod
		def hurt_direction(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getHurtDirection()"}

		@staticmethod
		def inventory(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getInventory()"}

		@staticmethod
		def item_in_use(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getItemInUse()"}

		@staticmethod
		def item_on_cursor(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getItemOnCursor()"}

		@staticmethod
		def item_use_remaining_time(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getItemUseRemainingTime()"}

		@staticmethod
		def killer(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getKiller()"}

		@staticmethod
		def last_damage(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLastDamage()"}

		@staticmethod
		def last_damage_cause(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLastDamageCause()"}

		@staticmethod
		def last_login(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLastLogin()"}

		@staticmethod
		def last_seen(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLastSeen()"}

		@staticmethod
		def leash_holder(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLeashHolder()"}

		@staticmethod
		def loc(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLocation()"}

		@staticmethod
		def main_hand(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getMainHand()"}

		@staticmethod
		def max_fire_ticks(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getMaxFireTicks()"}

		@staticmethod
		def max_freeze_ticks(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getMaxFreezeTicks()"}

		@staticmethod
		def max_air(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getMaximumAir()"}

		@staticmethod
		def max_no_damage_ticks(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getMaximumNoDamageTicks()"}

		@staticmethod
		def near_entities(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getNearbyEntities()"}

		@staticmethod
		def no_damage_ticks(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getNoDamageTicks()"}

		@staticmethod
		def open_inv(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getOpenInventory()"}

		@staticmethod
		def origin(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getOrigin()"}

		@staticmethod
		def passengers(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPassengers()"}

		@staticmethod
		def passenger(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPassenger()"}

		@staticmethod
		def portal_cooldown(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPortalCooldown()"}

		@staticmethod
		def pose(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPose()"}

		@staticmethod
		def potential_bed_loc(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPotentialBedLocation()"}

		@staticmethod
		def effect(python_player: str, effect: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getPotionEffect(" + effect + ")"}

		@staticmethod
		def saturated_regen_rate(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getSaturatedRegenRate()"}

		@staticmethod
		def server(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getServer()"}

		@staticmethod
		def sleep_ticks(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getSleepTicks()"}

		@staticmethod
		def starvation_rate(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getStarvationRate()"}

		@staticmethod
		def target_block(python_player: str, max_distance: int):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getTargetBlock(" + str(max_distance) + ")"}

		@staticmethod
		def target_block_face(python_player: str, max_distance: int):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getTargetBlockFace(" + str(max_distance) + ")"}

		@staticmethod
		def target_block_info(python_player: str, max_distance):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getTargetBlockInfo(" + max_distance + ")"}

		@staticmethod
		def ticks_lived(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getTicksLived()"}

		@staticmethod
		def type(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getType()"}

		@staticmethod
		def uuid(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getUniqueID()"}

		@staticmethod
		def vehicle(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getVehicle()"}

		@staticmethod
		def last_played(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getLastPlayed()"}

		@staticmethod
		def max_health(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getMaxHealth()"}

		@staticmethod
		def custom_name(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getCustomName()"}

		@staticmethod
		def item_in_hand(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getItemInHand()"}

		@staticmethod
		def compass_target(python_player: str):
			return {"imports": "import org.bukkit.entity.Player", "return_value": python_player + ".getCompassTarget()"}
class WVar:
	@staticmethod
	def set(namespace: str, key: str, value: str):
		try:
			store.variables[namespace][key] = value
			return {"imports": None, "return_value": None}
		except KeyError:
			store.variables[namespace] = {}
			store.variables[namespace][key] = value
			return {"imports": None, "return_value": None}

	@staticmethod
	def get(namespace: str, key: str):
		return store.variables[namespace][key]

	@staticmethod
	def clear(namespace: str, key: str = None):
		if key is not None:
			del store.variables[namespace][key]
			return {"imports": None, "return_value": None}
		else:
			del store.variables[namespace]
			return {"imports": None, "return_value": None}

def send_msg(text: str, target: str):
	return {"imports": ["import org.bukkit.entity.Player"], "return_value": f"{target}.sendMessage(\"{text}\")"}

def send_title(target: str, title: str, subtitle: str = None, fade_in: int = None, stay: int = None, fade_out: int = None):
	if fade_in is None:
		return {"imports": ["import org.bukkit.entity.Player"], "return_value": f"{target}.sendTitle(\"{title}\", \"{subtitle}\")"}
	else:
		return {"imports": ["import org.bukkit.entity.Player"], "return_value": f"{target}.sendTitle(\"{title}\", \"{subtitle}\", {fade_in}, {stay}, {fade_out})"}


def send_actionbar(text: str, target: str):
	return {"imports": ["net.md_5.bungee.api.ChatMessageType", "net.md_5.bungee.api.chat.TextComponent"], "return_value": f"{target}.sendTitle(ChatMessageType.ACTION_BAR, new TextComponent(\"{text}\"))"}

