import math

patron_names = \
"""Name One
N4me_Tw0
name three
"""

# TODO range over rows to print out exact number of names per row
# TODO calc either from total number of groups or from number of names per group

def lists_from_lines(multiline_string, splitter="\n", delimiter=", ", groups=1):
	"""Split and collect string lines into one or more lists"""
	textlines = multiline_string.split("\n")
	formatted_list = []

	i_cut = 0
	for group_n in range(1, groups+1):
		i_prev = i_cut
		if group_n < groups:
			i_cut = int(math.ceil((group_n / groups) * len(textlines)))
		else:
			i_cut = len(textlines)-1 		# to end, ignoring last newline
		new_group = delimiter.join(textlines[i_prev : i_cut])
		new_group.strip()
		formatted_list.append(new_group)

	formatted_lines = {
		'list': formatted_list,
		'delimiter': delimiter,
		'source': {
			'text': multiline_string,
			'split_by': splitter
		}
	}
	return formatted_lines

def print_patrons(formatted_batches, row_length=None, delimiter=", ", use_group_delimiter=False, use_final_delimiter=False, source_names=None):
	"""Take a list of already-delimited patron name batches and print them group by group"""
	def add_delimiter(group_i):
		return formatted_batches[group_i] + delimiter
	print_lns = []
	print_lns.append("\n--- FORMATTED PATRON NAMES ---")
	if source_names is not None: print_lns.append("Source list length: %s" % len(patron_names.split("\n")))
	for i in range(len(formatted_batches)):
		print_lns.append("\n---- LIST %s ---" % (i+1))
		print_lns.append("(%s names)\n" % len(formatted_batches[i].split(delimiter)))
		patron_names_group = add_delimiter(i) if use_group_delimiter == True and i != len(formatted_batches)-1 else formatted_batches[i]
		if use_final_delimiter: patron_names_group = add_delimiter(i)
		if len(formatted_batches[i]) < 1: patron_names_group = ""
		print_lns.append(patron_names_group.strip())
	print_lns.append("\n")
	for ln in print_lns: print(ln)
	return print_lns

formatted_patrons = lists_from_lines(patron_names, delimiter=", ", groups=4)
print_patrons(formatted_patrons['list'], delimiter=formatted_patrons['delimiter'], use_group_delimiter=True)
