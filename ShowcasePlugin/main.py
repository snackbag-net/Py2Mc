import pyplug
import pyplug.functions as function

plugin = {
	"generator": {
		"output": "out/",
		"name": "ShowcasePlugin",
		"id": "me.yourname.showcase",

	},

	"commands": {

	},

	"startup": [
		function.logger.info("Startup"),
		function.logger.warning("This is a startup message, you can put as many as you want!")
	],

	"disable": [
		function.logger.info("Goodbye!"),
		function.logger.info("Here too.")
	],

}

pyplug.mcClass.generator(plugin)
