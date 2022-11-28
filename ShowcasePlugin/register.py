import pyplug
from ShowcasePlugin.events.join_event import join_event


def register(id_fix):
	register = {
		"register": [
			pyplug.mcClass.Generate.register("event", join_event(), id_fix, "me.yourname.showcase")
		],
	}

	return register


pyplug.mcClass.Generate.events(register('out/ShowcasePlugin/main/java/me/yourname/showcase/events'))