import os

import pyplug.helper as helper

imports = {}
variables = {}


class Generator:
	def __init__(self, values):
		self.main_class(values)

	def main_class(self, values):
		values_gen = values["generator"]
		values_conf = values["plugin-settings"]
		values_start = values["startup"]
		values_disa = values["disable"]

		values2_outfold = values_gen["output"]
		values2_id = str(values_gen["id"])
		values2_folder = values2_id.replace(".", "/")
		values2_folders = values2_folder.split("/")

		values2_name = values_gen["name"]

		values2_vname = values_conf["name"]
		values2_ver = values_conf["version"]

		helper.ifFileExistsM(values2_outfold)
		helper.ifFileExistsM(values2_outfold + "java")

		helper.ifFileExistsM(values2_outfold + "java")

		last_folders = "java/"
		pos = values2_outfold + last_folders

		for i in range(len(values2_folders)):
			helper.ifFileExistsM(values2_outfold + last_folders + values2_folders[i])
			last_folders = last_folders + values2_folders[i] + "/"

		pos = values2_outfold + last_folders

		file_main = open(pos + "Main.java", "w")

		helper.ifFileExistsM(values2_outfold + "java/resources")
		helper.ifFileExistsM(pos + "events")
		helper.ifFileExistsM(pos + "gui")
		helper.ifFileExistsM(pos + "commands")

		file_plyml = open(values2_outfold + "java/resources/" + "plugin.yml", "w")

		file_plyml.write(f"""main: {values2_id}.Main
name: {values2_vname}
version: {values2_ver}""")
		# code main file

		file_main_text = []

		file_main_text.append("a")

		file_main.write("".join(file_main_text))
