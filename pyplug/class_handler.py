import os
import time

import pyplug.helper as helper
from pyplug.helper import Color
try:
	import requests
except ImportError:
	helper.pipInstaller()

imports = {"Main": ["import org.bukkit.*", "import org.bukkit.plugin.java.JavaPlugin"]}
tabs = {"Main": 0}
tab = "\t"
newline = "\n"
variables = {}

ern = None


class Generator:
	def __init__(self, values):
		print(Color.LIGHTBLUE + "[DEBUG] Building plugin... (self.main_class(values))" + Color.RESET)
		self.main_class(values) # build main class

	def main_class(self, values):
		values_gen = values["generator"] # generator settings
		values_conf = values["plugin-settings"]
		values_start = values["startup"] # startup commands
		values_disa = values["disable"] # disable command

		values_start.append({"imports": ["import org.bukkit.Bukkit"], "return_value": "Bukkit.getLogger().info(\"Made with Py2Mc\")"}) # add credit
		values_disa.append({"imports": ["import org.bukkit.Bukkit"], "return_value": "Bukkit.getLogger().info(\"Made with Py2Mc\")"}) # add credit

		values2_outfold = values_gen["output"] # out settings
		values2_id = str(values_gen["id"]) # package id
		values2_folder = values2_id.replace(".", "/") # replace all the . with /
		values2_folders = values2_folder.split("/") # split it by all /

		values2_name = values_gen["name"] # plugin generator name

		print(Color.LIGHTBLUE + "[DEBUG] Generating folders..." + Color.RESET)

		values2_vname = values_conf["name"] # plugin (visible) name
		values2_ver = values_conf["version"] # plugin version

		helper.ifFileExistsM(values2_outfold) # generate the out folder
		helper.ifFileExistsM(values2_outfold + "java") # generate the java folder

		last_folders = "java/" # last folders list
		pos = values2_outfold + last_folders # get the writer position

		for i in range(len(values2_folders)):
			helper.ifFileExistsM(values2_outfold + last_folders + values2_folders[i])
			last_folders = last_folders + values2_folders[i] + "/"

		print(Color.LIGHTBLUE + "[DEBUG] Setting 'pos'" + Color.RESET)

		pos = values2_outfold + last_folders # update writer position

		print(Color.LIGHTBLUE + "[DEBUG] Creating main file..." + Color.RESET)

		file_main = open(pos + "Main.java", "w") # define the file

		print(Color.LIGHTBLUE + "[DEBUG] Generating folders..." + Color.RESET)

		helper.ifFileExistsM(values2_outfold + "java/resources") # make the resources folder
		helper.ifFileExistsM(pos + "events") # make some important folders
		helper.ifFileExistsM(pos + "gui")
		helper.ifFileExistsM(pos + "commands")

		print(Color.LIGHTBLUE + "[DEBUG] Creating plugin yml..." + Color.RESET)

		file_plyml = open(values2_outfold + "java/resources/" + "plugin.yml", "w") # generate the plugin.yml

		print(Color.LIGHTBLUE + "[DEBUG] Writing plugin yml" + Color.RESET)

		file_plyml.write(f"""main: {values2_id}.Main
name: {values2_vname}
version: {values2_ver}""") # write the plugin.yml
		# code main file

		file_main_text = [[], [], [], [], []]  # no semi, autosemi, no semi, # autosemi

		print(Color.LIGHTBLUE + "[DEBUG] Writing main file" + Color.RESET)

		# get all events to register
		if values["events"] is not None:
			for i in range(len(values["events"])):
				l_ern = values["events"][i]["name"] # l_ern means local_event_register_name
				file_main_text[1].append("getServer().getPluginManager().registerEvents(new " + l_ern + "(), this)") # register the event

				imports["Main"].append(f"import {values2_id}.events.{l_ern}") # import the event

				print(Color.LIGHTBLUE + "[DEBUG] Registered event: " + Color.BLUE + Color.BOLD + l_ern + Color.RESET)

				self.events(values2_id, values["events"][i], values2_outfold) # build the event

		print(Color.LIGHTBLUE + "[DEBUG] Fixing main file" + Color.RESET)

		for i in range(len(values_start)): # trying to get imports for all the stuff that needs them in onEnable()
			try:
				if values_start[i]['imports'] is not None: # if there's imports
					for x in range(len(values_start[i]['imports'])):
						if values_start[i]['imports'][x] not in imports["Main"]: # if import isn't already imported
							imports["Main"].append(values_start[i]['imports'][x])
			except TypeError as err: # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT IMPORT with TypeError): ' +  Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + 'Main/start', err)
				time.sleep(1)

		for i in range(len(values_disa)): # trying to get imports for all the stuff that needs them in onEnable()
			try:
				if values_disa[i]['imports'] is not None: # if there's imports
					for x in range(len(values_disa[i]['imports'])):
						if values_disa[i]['imports'][x] not in imports["Main"]: # if import isn't already imported
							imports["Main"].append(values_disa[i]['imports'][x])
			except TypeError as err: # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT IMPORT with TypeError): ' +  Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + 'Main/disa', err)
				time.sleep(1)

		# Main.java code
		file_main_text[0].append(tab * tabs["Main"] + f"package {values2_id};\n\n")
		file_main_text[0].append(tab * tabs["Main"] + ";\n".join(imports["Main"]) + ";\n")
		file_main_text[0].append(tab * tabs["Main"] + "\npublic final class Main extends JavaPlugin {\n")
		tabs["Main"] += 1
		file_main_text[0].append(tab * tabs["Main"] + "@Override\n")
		file_main_text[0].append(tab * tabs["Main"] + "public void onEnable() {\n")
		tabs["Main"] += 1
		for i in range(len(values_start)): # fix importer and tabber
			try:
				print(values_start)
				file_main_text[1].append(tab * tabs["Main"] + (values_start[i]['return_value']) + ";") # add the return value
			except TypeError as err: # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT GENERATE with TypeError): ' +  Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + 'Main/start', err)
				time.sleep(1)
		tabs["Main"] -= 1
		file_main_text[2].append(tab * tabs["Main"] + "\n" + tab * tabs["Main"] + "}" + tab * tabs["Main"] + "\n\n" + tab * tabs["Main"] + "@Override\n")
		file_main_text[2].append(tab * tabs["Main"] + "public void onDisable() {\n")
		tabs["Main"] += 1
		for i in range(len(values_disa)): # fix importer and tabber
			try:
				file_main_text[3].append(tab * tabs["Main"] + (values_disa[i]['return_value']) + ";") # add the return value
			except TypeError as err: # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT GENERATE with TypeError): ' +  Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + 'Main/disa', err)
				time.sleep(1)
		file_main_text[4].append(tab * tabs["Main"] + "\n}\n}\n")

		# main file code finalizing
		file_main_finaltext = []
		file_main_finaltext.append(''.join(file_main_text[0]) + "\n")
		file_main_finaltext.append(tab * tabs['Main'] + f"\n{f';{newline}'.join(file_main_text[1])}")
		file_main_finaltext.append(f"\n{''.join(file_main_text[2])}")
		file_main_finaltext.append(tab * tabs['Main'] + f"\n{f';{newline}'.join(file_main_text[3])}")
		file_main_finaltext.append(f"\n{''.join(file_main_text[4])}")

		print(Color.LIGHTBLUE + "[DEBUG] Writing main file" + Color.RESET)

		file_main.write(''.join(file_main_finaltext))
		# if warns == 0:
		# 	warnt = Color.GREEN + Color.BOLD + "0" + Color.RESET
		# else:
		# 	warnt = Color.YELLOW + Color.BOLD + warns + Color.RESET
		#
		# if errors == 0:
		# 	errort = Color.GREEN + Color.BOLD + "0" + Color.RESET
		# else:
		# 	errort = Color.RED + Color.BOLD + errors + Color.RESET
		#
		# print("Finished build with " + warnt + " warns and " + errort + " errors!")
		print("Finished build")


	def events(self, values_id: str, infos: dict, out):
		print(Color.LIGHTBLUE + "[DEBUG] Starting write of event " + Color.BOLD + Color.BLUE + infos["name"] + Color.RESET)
		values_id2 = values_id + ".events"
		folder = values_id.replace(".", "/")
		folders = folder.split("/")

		pos = f"{out}java/{folder}/events" # current writer position
		event_file = open(f"{pos}/{infos['name']}.java", "w") # make the file
		ern = f"event/{infos['name']}" # ern means event_register_name

		tabs[ern] = 0 # set the tabs for this file
		imports[ern] = ["import org.bukkit.event.EventHandler", "import org.bukkit.event.Listener"] # add some imports for basic stuff
		for i in range(len(infos['type']['imports'])):
			imports[ern].append(infos['type']['imports'][i]) # add the extra imports

		for i in range(len(infos['execute'])): # trying to get imports for all the stuff that needs them
			try:
				if infos['execute'][i]['imports'] is not None: # if there's imports
					for x in range(len(infos['execute'][i]['imports'])):
						if infos['execute'][i]['imports'][x] not in imports[ern]:
							imports[ern].append(infos['execute'][i]['imports'][x])
			except TypeError as err: # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT IMPORT with TypeError): ' +  Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + infos['name'], err)
				time.sleep(1)

		event_file_text = [[], [], []] # hand semicolon, auto semicolon, hand semicolon

		print(Color.LIGHTBLUE + "[DEBUG] Writing event " + Color.BLUE + Color.BOLD + infos["name"] + Color.RESET)

		# event code
		event_file_text[0].append(tab * tabs[ern] + f"package {values_id2};\n")
		event_file_text[0].append(tab * tabs[ern] + ";\n".join(imports[ern]) + ";\n")
		event_file_text[0].append(tab * tabs[ern] + f"public class {infos['name']} implements Listener " + "{")
		tabs[ern] += 1
		event_file_text[0].append(tab * tabs[ern] + "@EventHandler")
		event_file_text[0].append(tab * tabs[ern] + f"void {infos['type']['recog-void']}({infos['type']['recog-event']}) " + "{")
		tabs[ern] += 1
		for i in range(len(infos['execute'])): # fix importer and tabber
			try:
				event_file_text[1].append(tab * tabs[ern] + (infos['execute'][i]['return_value']) + ";") # add the return value
			except TypeError as err: # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT GENERATE with TypeError): ' +  Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + infos['name'], err)
				time.sleep(1)

		tabs[ern] -= 1
		event_file_text[2].append(tab * tabs[ern] + "}")
		tabs[ern] -= 1
		event_file_text[2].append(tab * tabs[ern] + "}")

		# write event file
		event_file.write("\n".join(event_file_text[0]) + "\n" + "\n".join(event_file_text[1]) + "\n" + "\n".join(event_file_text[2]))