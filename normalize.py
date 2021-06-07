#!/usr/bin/env python3 

#coding:utf-8

import unicodedata
import re

def remove_special_characters(input_str):
	nfkd_form = unicodedata.normalize('NFKD', input_str)
	only_ascii = nfkd_form.encode('ASCII', 'ignore').decode("utf-8")
	no_spaces = only_ascii.replace(" ", "_").replace("'", "_")
	no_at_sign = no_spaces.replace("@","at")
	no_special_characters = re.sub(r'[^\w\s]','',no_at_sign)
	return no_special_characters


#Test

if __name__ == "__main__":
	string = "L'école @ la maison!"
	result = remove_special_characters(string)

	assert result == ("L_ecole_at_la_maisondsgdg")


