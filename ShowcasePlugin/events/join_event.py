import pyplug.event as event
import pyplug.event.common as eventcm
import pyplug.functions.common as cm
import pyplug.functions as fn


def join_event() -> dict:
	item = {
		"type": event.playerJoinEvent.register(),
		"name": "joinEvent",
		"execute": [
			cm.Var.set("joinEvent", "player", eventcm.DefineEventPlayer.python()),
			eventcm.DefineEventPlayer.java(),
			event.playerJoinEvent.set_join_message(cm.Get.name(cm.Var.get("joinEvent", "player")) + " has joined!"),
			cm.send_actionbar(cm.Var.get("joinEvent", "player"), "Thanks for " + cm.color("blue") + "joining" + cm.color("reset") + "!")
		],
	}

	return item
