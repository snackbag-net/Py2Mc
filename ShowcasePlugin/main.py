import pyplug
import pyplug.functions.generic as fn
import pyplug.functions as cm

plugin = {
	"generator": {
		"output": "out/",
		"name": "ShowcasePlugin",
		"id": "me.yourname.showcase",

	},

	"plugin-settings": {
		"name": "ShowcasePlugin",
		"version": "1.0.0",
	},

	"commands": {

	},

	"startup": [
		fn.logger.info("Startup"),
		fn.logger.warning("This is a startup message, " + cm.color("red") + "you can put as many as you want!")
	],

	"disable": [
		fn.logger.info("Goodbye!"),
		fn.logger.info("Here too.")
	],

}

pyplug.mcClass.generator(plugin)
