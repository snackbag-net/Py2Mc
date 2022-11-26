import os
import sys
import time

from pyplug.creator.main import need_to_import, is_alphanumeric_str, continue_cancel


def generator(inp: dict):
	errors = 0
	warns = 0
	output = inp["generator"]["output"]
	projname = inp["generator"]["name"]
	pluginyml = dict(inp["plugin-settings"])
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

	# Plugin.yml optional values fix
	pluginyml_description = None
	pluginyml_author = None
	pluginyml_website = None
	pluginyml_prefix = None

	pluginyml_authors = None
	pluginyml_depend = None
	pluginyml_softdepend = None
	pluginyml_loadbefore = None

	# Plugin.yml settings
	# *NEEDED VALUES*
	pluginyml_main = id + ".Main"  # auto assign
	pluginyml_name = pluginyml["name"]  # needs to be alphanumeric

	if is_alphanumeric_str(pluginyml_name) is False:
		print(
			"\033[1m\033[31mFATAL ERROR: \033[0m\033[38mThe plugin name in 'plugin-settings' can only be: 'a-z,A-Z,0-9,_'. Please change immediately! If not changed, plugin will not show up on server.\033[0m")
		time.sleep(1)
		errors += 1
		if continue_cancel() is False:
			print("Stopping build process... Unfinished build will NOT be removed.")
			sys.exit(0)
	pluginyml_version = str(pluginyml["version"])

	if pluginyml_version.count(".") not in [2, 3, 4, 5]:
		print(
			"\033[1m\033[33mWARNING: \033[0mWe have detected that you aren't using Semantic Versioning. Please use it!")
		time.sleep(1)
		warns += 1

	# *OPTIONAL VALUES*
	pluginyml_description = pluginyml.get("description")
	pluginyml_author = pluginyml.get("author")
	pluginyml_website = pluginyml.get("website")
	pluginyml_prefix = pluginyml.get("prefix")

	# *OPTIONAL VALUES THAT NEED TO BE TURNED INTO YAML-LIST*
	pluginyml_authors = pluginyml.get("authors")  # turn this into list later
	pluginyml_depend = pluginyml.get("depend")  # turn this into list later
	pluginyml_softdepend = pluginyml.get("softdepend")  # turn this into list later
	pluginyml_loadbefore = pluginyml.get("loadbefore")  # turn this into list later

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
	mainfile_output.append(tabindex * tab + f"\n{tabindex * tab}".join(on_startup))
	tabindex = tabindex - 1
	mainfile_output.append(tabindex * tab + "}\n")
	mainfile_output.append(tabindex * tab + "@Override")
	mainfile_output.append(tabindex * tab + "public void onDisable() {")
	tabindex = tabindex + 1
	mainfile_output.append(tabindex * tab + f"\n{tabindex * tab}".join(on_disable))
	tabindex = tabindex - 1
	mainfile_output.append(tabindex * tab + "}")
	tabindex = tabindex - 1
	mainfile_output.append(tabindex * tab + "}\n")

	mainfile.write("\n".join(mainfile_output))

	mainfile.close()

	pluginymlfile = open(output + projname + f"/main/resources/plugin.yml", "w")
	pluginymlfile_output = [
		f"main: {pluginyml_main}\n",
		f"name: {pluginyml_name}\n",
		f"version: {pluginyml_version}\n",
	]
	if pluginyml_description is not None:
		pluginymlfile_output.append("description: " + pluginyml_description + "\n")
	if pluginyml_author is not None:
		pluginymlfile_output.append("author: " + pluginyml_author + "\n")
	if pluginyml_authors is not None:
		pluginymlfile_output.append("authors: [" + pluginyml_authors + "]\n")
	if pluginyml_website is not None:
		pluginymlfile_output.append("website: " + pluginyml_website + "]\n")
	if pluginyml_depend is not None:
		pluginymlfile_output.append("depend: [" + pluginyml_author + "]\n")
	if pluginyml_prefix is not None:
		pluginymlfile_output.append("prefix: " + pluginyml_prefix + "\n")
	if pluginyml_softdepend is not None:
		pluginymlfile_output.append("softdepend: [" + pluginyml_softdepend + "]\n")
	if pluginyml_loadbefore is not None:
		pluginymlfile_output.append("loadbefore: [" + pluginyml_loadbefore + "]\n")

	pluginymlfile.write("".join(pluginymlfile_output))
	pluginymlfile.close()

	# Finish
	print("\033[1m\033[32mBuild finished!\033[0m")

	if errors == 0:
		errortext = "Errors: \033[1m\033[32m0\033[0m"
	else:
		errortext = f"Errors: \033[1m\033[31m{errors}\033[0m"

	if warns == 0:
		warntext = "Warns: \033[1m\033[32m0\033[0m"
	else:
		warntext = f"Warns: \033[1m\033[33m{warns}\033[0m"

	print(errortext + " | " + warntext)
