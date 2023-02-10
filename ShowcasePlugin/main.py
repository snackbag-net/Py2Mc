import pyplug
from pyplug import class_handler as ch
from pyplug.functions import *

import ShowcasePlugin.events as events

plugin = {
	"generator": {
		"output": "out/",
		"name": "ShowcasePlugin",
		"id": "me.yourname.showcase",
		"autocompile": False,
		"autocompile_path": None
	},

	"plugin-settings": {
		"name": "ShowcasePlugin",
		"version": "1.0.0",
	},

	"events": [events.OnPlayerJoin.retev()],
	"commands": None,

	"startup": [
		Log.info("Hello!"),
		Log.info("LOL!")
	],

	"disable": [

	],
}

ch.Generator(plugin)