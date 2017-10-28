#!/usr/bin/env python

import os

# parse the students file
cur_dir=os.getcwd()
students_file = os.path.realpath(os.path.join(cur_dir,"..","..","..","examples","Session01","students.txt"))
print(students_file)

students = open(students_file, "r")
all_langs = {}
for student in students:
	name, misc = student.strip().split(":")
	# skip the header
	if name == "Name":
		continue
	# convert comma spaces to commas so we can isolate
	# space delimited entries
	misc = misc.strip().replace(", ", ",")
	# convert space delimited to comma delimited so we
	# can split everything
	misc = misc.replace(" ", ",")
	langs = misc.split(",")
	trim_indexes = []
	for index, lang in enumerate(langs):
		langs[index] = lang.strip()
		if lang == "":
			trim_indexes.append(index)
			#print("delempty!")
		else:
			# if the first entry in the list isn't lower, 
			# it's probaly a nickname so mark it for deletion
			if index == 0 and lang != lang.lower():
				trim_indexes.append(index)
			# exception handling
			if lang in ["new" ]:
				trim_indexes.append(index)
	# remove items that are not languages
	for bad_item in reversed(trim_indexes):
		#print("deleting",langs[bad_item])
		del langs[bad_item]

	# print the cleaned list
	print(name, langs)

	for lang in langs:
		# if there is no entry, add one
		if lang not in all_langs.keys():
			all_langs[lang]=[]
		# add the student to the list of suspects
		all_langs[lang].append(name)

students.close()

languages=list(all_langs.keys())
num_lang=len(languages)

print("")
print("{} languages used by this class: {}".format(num_lang,languages))
print("")

# print per lang stats
for lang in languages:
	print(lang,len(all_langs[lang]))

#print(total_langs)
#print(all_langs)
