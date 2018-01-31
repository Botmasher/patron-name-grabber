# featured names
patrons_0 = \
"""Sample Name
Another Name
Third Name
"""

patrons_1 = \
"""Sample Name
Another Name
Third Name
"""

delimiter = ", "

# build lists for display
def cut_and_format_patron_list(patrons_string, splitter="\n", delimiter=", "):
	nameset = patrons_string.split("\n")
	nameset_center = int(len(nameset) * 0.5) - 1
	# split list in half and append two csv strings
	patron_lists = []
	patron_lists.append(delimiter.join(nameset[0:nameset_center]))
	patron_lists.append(delimiter.join(nameset[nameset_center:len(nameset)-1]))
	return patron_lists

patronlist_0, patronlist_1 = cut_and_format_patron_list(patrons_0)
patronlist_2, patronlist_3 = cut_and_format_patron_list(patrons_1)

print("\n--- FORMAT AND DISPLAY PATRON NAMES LISTS ---")
print("Initial list length: %s" % ( len(patrons_0.split("\n")) ))
print("Cut list length: %s " % (len(patronlist_0.split(", ")) + len(patronlist_1.split(", "))) )
print("\n")

def print_patrons(delimited_patrons_string, list_index, row_length, delimiter=", ", use_final_delimiter=True):
	final_delimiter = ", " if use_final_delimiter else ""
	print("---- LIST %s ---" % list_index)
	#for patron in delimited_string.split(delimiter): print(patron)
	patrons = delimited_patrons_string.split(delimiter)
	# divide into and check total patrons count to know how many chunks are being iterated thru
	 	# - it's leaving straggling extra lines too many commas
	for i in range(row_length):
		row = delimiter.join(patrons[i*row_length:i*row_length + row_length]) + final_delimiter
		row is not None and row != delimiter and print(row)
	#print("%s%s" % (delimited_string, final_delimiter))
	print("\n")

print_patrons(patronlist_0, 0, row_length=8)
print_patrons(patronlist_1, 1, row_length=8)
print_patrons(patronlist_2, 2, row_length=12)
print_patrons(patronlist_3, 3, row_length=12, use_final_delimiter=False)
