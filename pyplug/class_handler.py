import os

import pyplug.helper as helper

imports = {"Main": ["import org.bukkit.*", "import org.bukkit.plugin.java.JavaPlugin"]}
tabs = {"Main": 0}
tab = "\t"
newline = "\n"
variables = {}


class Generator:
	def __init__(self, values):
		self.main_class(values)

	def main_class(self, values):
		values_gen = values["generator"] # generator settings
		values_conf = values["plugin-settings"]
		values_start = values["startup"] # startup commands
		values_disa = values["disable"] # disable command

		values_start.append("Bukkit.getLogger().info(\"Made with Py2Mc\")") # add credit
		values_disa.append("Bukkit.getLogger().info(\"Made with Py2Mc\")") # add credit

		values2_outfold = values_gen["output"] # out settings
		values2_id = str(values_gen["id"]) # package id
		values2_folder = values2_id.replace(".", "/") # replace all the . with /
		values2_folders = values2_folder.split("/") # split it by all /

		values2_name = values_gen["name"] # plugin generator name

		values2_vname = values_conf["name"] # plugin (visible) name
		values2_ver = values_conf["version"] # plugin version

		helper.ifFileExistsM(values2_outfold) # generate the out folder
		helper.ifFileExistsM(values2_outfold + "java") # generate the java folder

		last_folders = "java/" # last folders list
		pos = values2_outfold + last_folders # get the writer position

		for i in range(len(values2_folders)):
			helper.ifFileExistsM(values2_outfold + last_folders + values2_folders[i])
			last_folders = last_folders + values2_folders[i] + "/"

		pos = values2_outfold + last_folders # update writer position

		file_main = open(pos + "Main.java", "w") # define the file

		helper.ifFileExistsM(values2_outfold + "java/resources") # make the resources folder
		helper.ifFileExistsM(pos + "events") # make some important folders
		helper.ifFileExistsM(pos + "gui")
		helper.ifFileExistsM(pos + "commands")

		file_plyml = open(values2_outfold + "java/resources/" + "plugin.yml", "w") # generate the plugin.yml

		file_plyml.write(f"""main: {values2_id}.Main
name: {values2_vname}
version: {values2_ver}""") # write the plugin.yml
		# code main file

		file_main_text = [[], [], [], [], []]  # no semi, autosemi, no semi, # autosemi

		# Main.java code
		file_main_text[0].append(tab * tabs["Main"] + f"package {values2_id};\n\n")
		file_main_text[0].append(tab * tabs["Main"] + ";\n".join(imports["Main"]) + ";\n")
		file_main_text[0].append(tab * tabs["Main"] + "\npublic final class Main extends JavaPlugin {\n")
		tabs["Main"] += 1
		file_main_text[0].append(tab * tabs["Main"] + "@Override\n")
		file_main_text[0].append(tab * tabs["Main"] + "public void onEnable() {\n")
		tabs["Main"] += 1
		file_main_text[1].append(tab * tabs["Main"] + ';\n'.join(values_start) + ";\n")
		tabs["Main"] -= 1
		file_main_text[2].append(tab * tabs["Main"] + "\n" + tab * tabs["Main"] + "}" + tab * tabs["Main"] + "\n\n" + tab * tabs["Main"] + "@Override\n")
		file_main_text[2].append(tab * tabs["Main"] + "public void onDisable() {\n")
		tabs["Main"] += 1
		file_main_text[3].append(tab * tabs["Main"] + ';\n'.join(values_disa) + ";\n")
		file_main_text[4].append(tab * tabs["Main"] + "\n}\n}\n")

		# main file code finalizing
		file_main_finaltext = []
		file_main_finaltext.append(''.join(file_main_text[0]) + "\n")
		file_main_finaltext.append(tab * tabs['Main'] + f"\n{f';{newline}'.join(file_main_text[1])}")
		file_main_finaltext.append(f"\n{''.join(file_main_text[2])}")
		file_main_finaltext.append(tab * tabs['Main'] + f"\n{f';{newline}'.join(file_main_text[3])}")
		file_main_finaltext.append(f"\n{''.join(file_main_text[4])}")

		file_main.write(''.join(file_main_finaltext))
