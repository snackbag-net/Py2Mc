import os
import shutil
import sys
import time

from pyplug.creator.main import *

generate_events = False
generate_args = {}
commands_place = None
events_place = None
id_fix = None
finished_generating_not = True


class Generate:
	def __init__(self):
		if generate_args is None:
			print("No args given - stopping...")
			sys.exit(0)

		self.errors = 0
		self.warns = 0

		print(f"\033[1mDEBUG:\033[0m\n{generate_args=}\n")

		self.imports = {}

		self.generator(generate_args)

	@staticmethod
	def register(type, register: dict, id_fix, package):
		if type == "event":
			# id_fix = id_fix + "/events/"
			package = package + ".events"
			item = dict(register["type"])
			item2 = item["need"]
			name = str(register["name"])

			event_file = open(f"{id_fix}/{name}.java", "w")

			event_file.write(code_event(item2, register, package))

			event_file.close()

	@staticmethod
	def events(register):
		print("Generating events...")

	def generator(self, inp: dict):
		output = inp["generator"]["output"]
		projname = inp["generator"]["name"]
		pluginyml = dict(inp["plugin-settings"])
		print(
			f"\033[1mDEBUG:\nOutput: \033[0m{output}\033[1m\nProjname: \033[0m{projname}\033[1m\nPluginYML: \033[0m{pluginyml}\n")
		id = str(inp["generator"]["id"])
		id_fix = id.replace(".", "/")
		id_split = id_fix.split("/")
		print(f"\033[1mDEBUG:\nID: \033[0m{id}\033[1m\nID_FIX: \033[0m{id_fix}\033[1m\nID_SPLIT: \033[0m{id_split}\n")

		try:
			os.mkdir(output + projname)
		except FileExistsError:
			print("There's already a project there.")
			if continue_cancel() is False:
				sys.exit()
			else:
				print("Continuing!\n\n\n")
				shutil.rmtree(output + projname)
				os.mkdir(output + projname)

		print("Generating basic folders...")
		os.mkdir(output + projname + "/main")
		os.mkdir(output + projname + "/main/java")
		os.mkdir(output + projname + "/main/resources")

		print("Generating group id...")
		id_split_len = len(id_split)
		last_split = ""
		for i in range(id_split_len):
			os.mkdir(output + projname + f"/main/java/{last_split}{id_split[i]}")
			last_split += id_split[i] + "/"
		print(f"Generating event and command folders at '{output} + {projname} + /main/java/{id_fix}/'")

		commands_place = output + projname + f"/main/java/{id_fix}/commands"
		events_place = output + projname + f"/main/java/{id_fix}/events"
		os.mkdir(commands_place)
		os.mkdir(events_place)

		####################################
		############# [ MAIN ] #############
		####################################

		# Main class things
		on_startup = list(inp["startup"])
		on_disable = list(inp["disable"])

		# General things
		# commands = list(inp["commands"])

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
			self.errors += 1
			if continue_cancel() is False:
				print("Stopping build process... Unfinished build will NOT be removed.")
				sys.exit(0)
		pluginyml_version = str(pluginyml["version"])

		if pluginyml_version.count(".") not in [2, 3, 4, 5]:
			print(
				"\033[1m\033[33mWARNING: \033[0mWe have detected that you aren't using Semantic Versioning. Please use it!")
			time.sleep(1)
			self.warns += 1

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
		mainfile_path = output + projname + f"/main/java/{id_fix}/Main.java"

		tabindex = 0
		tab = "\t"

		len1 = len(inp["register-event"])

		for events in range(len1):
			self.imports[mainfile_path] = f"import {id}.events.{inp['register-event'][events]};\n"

		self.imports[mainfile_path] = self.imports[mainfile_path] + "\n".join(need_to_import("main"))
		print(f"\033[1mDEBUG:\033[0m\n{self.imports=}\n")

		# print(imports)

		#######################


		mainfile = open(mainfile_path, "w")

		mainfile_output = [
			f"package {id};\n",
			self.imports[mainfile_path] + "\n\n",
			"public final class Main extends JavaPlugin {",
		]
		tabindex = tabindex + 1
		mainfile_output.append(tabindex * tab + "@Override")
		mainfile_output.append(tabindex * tab + "public void onEnable() {")
		tabindex = tabindex + 1


		for events in range(len1):
			mainfile_output.append(
				tabindex * tab + f"getServer().getPluginManager().registerEvents(new {inp['register-event'][events]}, this);")
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

		print(
			f"\033[1mPlease start your register.py if you have any events or commands!\nValue:\033[0mpyplug.mcClass.Generate.events(register('{events_place}'))")

	def finish(self):
		# Finish
		print("\033[1m\033[32mBuild finished!\033[0m")

		if self.errors == 0:
			errortext = "Errors: \033[1m\033[32m0\033[0m"
		else:
			errortext = f"Errors: \033[1m\033[31m{self.errors}\033[0m"

		if self.warns == 0:
			warntext = "Warns: \033[1m\033[32m0\033[0m"
		else:
			warntext = f"Warns: \033[1m\033[33m{self.warns}\033[0m"

		print(errortext + " | " + warntext)
