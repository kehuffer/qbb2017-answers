#!/usr/bin/env python
# Documentation
# $ ./day2-homework-2.py <t_data.ctab> <formatted_output_file> {"ignore" | <fill_value>}


import sys

ctab_file = open(sys.argv[1])
mapped_file = open(sys.argv[2])
no_uniprot = sys.argv[3]

mapped_fields_dict = {}

for line in mapped_file:
    mapped_fields = line.rstrip("\r\n").split()
    mapped_fields_dict[mapped_fields[0]] = mapped_fields[1]

for line in ctab_file:
    # Remove any newlines from end of line,
    # then split using tab as delimiter
    # -> List of strings representing fields
    ctab_fields = line.rstrip("\r\n").split("\t")
    ctab_fb = ctab_fields[8]
    if ctab_fb in mapped_fields_dict:
        print line.rstrip("\r\n"), "\t", mapped_fields_dict[ctab_fb]
        #ctab_fields.append(mapped_fields_dict[ctab_fb])
        #print ctab_fields
        # print line from ctab file with the uniprot identifier
    else:
        # ignore or fill with user-specified value
        if no_uniprot == "ignore":
            continue

        else:
            print line.rstrip("\r\n"), "\t", no_uniprot
            #ctab_fields.append(no_uniprot)
            #print ctab_fields

