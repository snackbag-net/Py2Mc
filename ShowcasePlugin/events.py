import pyplug.event_commons as ec
import pyplug.functions as fn
# import pyplug.java as j
from pyplug.functions import ExperimentalCommons as exc
from pyplug.functions import Player
from pyplug.java import Statement as s
from pyplug.java import Needed as n
from pyplug.events.player import Join as Event

fn.WVar.set("opj", "player", ec.DefEventPlayer.python())
player = fn.WVar.get("opj", "player")['return_value']

class OnPlayerJoin:

	@staticmethod
	def retev():
		event = {
			"type": Event.register(),
			"name": "OnPlayerJoin",
			"execute": [
				fn.Log.info("test"),
				{"imports": ["import org.bukkit.entity.hdjask"], "return_value": "hallu"},
				{"imports": ["import org.bukkit.entity.hdjask"], "return_value": "hallu"},
				# ec.DefEventPlayer.java(),
				exc.fix_val(fn.send_msg("Hello! That was a wrong command.", player), exc.toStr()),
				# exc.fix_val(fn.ExperimentalCommons.toStr(), fn.ExperimentalCommons.toStr()),
				# Player.Get.arrows_in_body(player)
			]
		}

		return event
