# Language Processing Python Scripts 
This repository contains a series scripts for extracting features from .wav files - these scripts were written to better understand Natural Language Processing.
## lm.py
Program that makes use of the nltk (Natural Language ToolKit) library to parse through a text file and construct unigrams and bigrams based off of word frequencies. Additionally, by examining the rate at which certain words appear within a text, the program can use a greedy algorithm to predict the most probable sentences to appear within the text. 
## dtw.py
Program that utilizes the concepts of Dynamic Time Warping by parsing through two text files of sound features, where each line of a text file will represent one frame of a .wav file (with each value representing a particular feature). By comparing two files against each other, one can make an assumption about whether or not the two files are representing the same word or phrase; the smaller the Euclidean distance, the more likely it is that the two text files are representing the same word/phrase.
## classify.py
Program that relies on several libraries include sklearn (SciKit-Learn) and NumPy to generate classifiers that can be used to evaluate the speech features of a speaker. By examining an individual's speech features, assumptions can be made about whether a speaker has a particular accent or even a speech impediment (such as one that is caused by dementia).

Contributors: Jordan Edward Shea, Emily Prud'hommeaux
