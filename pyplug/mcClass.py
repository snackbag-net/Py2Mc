import os

from pyplug.creator.main import need_to_import


def generator(inp: dict):
	output = inp["generator"]["output"]
	projname = inp["generator"]["name"]
	id = inp["generator"]["id"]

	os.mkdir(output + projname)
	os.mkdir(output + projname + "/main")
	os.mkdir(output + projname + "/main/java")
	os.mkdir(output + projname + "/main/resources")
	os.mkdir(output + projname + f"/main/java/{id}")

	####################################
	############# [ MAIN ] #############
	####################################

	# Main class things
	on_startup = list(inp["startup"])
	on_disable = list(inp["disable"])

	# General things
	commands = list(inp["commands"])

	# Plugin.yml settings

	# Creation things
	tabindex = 0
	tab = "\t"
	imports = need_to_import("main")
	imports = "\n".join(imports)

	# print(imports)

	#######################

	mainfile = open(output + projname + f"/main/java/{id}/main.java", "w")

	mainfile_output = [
		f"package {id};\n",
		imports + "\n\n",
		"public final class MainTest extends JavaPlugin {",
	]
	tabindex = tabindex + 1
	mainfile_output.append(tabindex * tab + "@Override")
	mainfile_output.append(tabindex * tab + "public void onEnable() {")
	tabindex = tabindex + 1
	mainfile_output.append(tabindex * tab + f"\n{tabindex*tab}".join(on_startup))
	tabindex = tabindex - 1
	mainfile_output.append(tabindex * tab + "}\n")
	mainfile_output.append(tabindex * tab + "@Override")
	mainfile_output.append(tabindex * tab + "public void onDisable() {")
	tabindex = tabindex + 1
	mainfile_output.append(tabindex * tab + f"\n{tabindex*tab}".join(on_disable))
	tabindex = tabindex - 1
	mainfile_output.append(tabindex * tab + "}")
	tabindex = tabindex - 1
	mainfile_output.append(tabindex * tab + "}\n")

	mainfile.write("\n".join(mainfile_output))
