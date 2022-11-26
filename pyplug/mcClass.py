import os

from pyplug.creator.main import need_to_import


def generator(inp: dict):
	output = inp["generator"]["output"]
	projname = inp["generator"]["name"]
	id = str(inp["generator"]["id"])
	id_fix = id.replace(".", "/")
	id_split = id_fix.split("/")

	os.mkdir(output + projname)
	os.mkdir(output + projname + "/main")
	os.mkdir(output + projname + "/main/java")
	os.mkdir(output + projname + "/main/resources")

	id_split_len = len(id_split)
	last_split = ""
	for i in range(id_split_len):
		os.mkdir(output + projname + f"/main/java/{last_split}{id_split[i]}")
		last_split += id_split[i] + "/"

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

	mainfile = open(output + projname + f"/main/java/{id_fix}/Main.java", "w")

	mainfile_output = [
		f"package {id};\n",
		imports + "\n\n",
		"public final class Main extends JavaPlugin {",
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
