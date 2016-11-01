#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

def words(string_word):
	split_item = [",","\n","\t", " "]
	split_word = string_word.replace("\n", " ")
	split_word = split_word.replace("\t", " ")
	split_word = split_word.replace("  ", " ")
	split_word = split_word.split(" ")
	#print split_word
	word_count = {}
	for item in split_word:
		if item.isdigit() == True:
			item = int(item)
			if item in word_count:
				word_count[item] += 1
			else:
				word_count[item] = 1
		else:
			if item in word_count:
				word_count[item] += 1
			else:
				word_count[item] = 1

	return word_count

print (words("Nairobi is a city of\ncity city  1 2 Nairobi"))
print (words('¡Hola! ¿Qué tal? Привет!'))