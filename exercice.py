#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
def get_num_letters(text):
	text_alpha = " ".join(ch for ch in text if text.isalnum())
	return text_alpha

def get_word_length_histogram(text):
	mots = text.split()
	liste_nombre_lettres = []
	for i in range(len(max(mots , key=len))+1): #revoir key
		liste_nombre_lettres.append(0)
	for i in mots:
		liste_nombre_lettres[len(i)] +=1
	return liste_nombre_lettres



def format_histogram(histogram):
	liste_nombre_lettres = [0, 0, 0, 1, 1, 4, 0, 1, 1, 0, 0, 0, 1]
	ROW_CHAR = "*"
	for i in range(1, len(liste_nombre_lettres)):
		histogram = print(i , liste_nombre_lettres[i] * ROW_CHAR)
	return histogram

def format_horizontal_histogram(histogram):
	liste_nombre_lettres = [0, 0, 0, 1, 1, 4, 0, 1, 1, 0, 0, 0, 1]
	BLOCK_CHAR = "|"
	for i in liste_nombre_lettres:
		histogram = print(BLOCK_CHAR * i)
	LINE_CHAR = "¯"
	print(LINE_CHAR * len(liste_nombre_lettres))

	return histogram


if __name__ == "__main__":
	text = "salut! je suis rayan"
	print(get_num_letters(text))
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))##