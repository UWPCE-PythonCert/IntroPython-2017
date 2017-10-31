donor_fnames = ['Bill', 'Melvin', 'Daphnie', 'Chauncey', 'Frieda']
donor_lnames = ['Gates', 'Smith', 'Jones', 'Doe', 'Whatever']
donations = [[200, 500], [2000.00, 3000.50, 3000.00], [1500.00, 500.25], [400.00], [2000.12, 3000, 4000]]

keys = ['f_name', 'l_name', 'don_amt', 'don_num']
donor_dict = dict.fromkeys(keys, None)

#donor_dict = dict(zip('f_name', donor_fnames))

for i in range(len(donor_fnames)):
	donor_dict[f_name].append(donor_fnames)

print(donor_dict)



#all_words = []
#with open(infile) as novel:
#	novel.readline()
#	for line in novel:
#		line = line.strip()
#		split_line = line.split()
#		all_words.extend(split_line)

#new_words = []
#for i in all_words:
#	if i.strip():
#		new_words.append(i.strip())