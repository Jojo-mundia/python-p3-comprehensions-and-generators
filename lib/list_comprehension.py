#!/usr/bin/env python3

def return_evens(num_list):
    # Keep only the even numbers
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    # Add an exclamation mark to each sentence
    return [s + "!" for s in sentence_list]
