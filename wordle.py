import random
import sys
from termcolor import colored
import nltk
nltk.download('words')
from nltk.corpus import words

def print_menu():
    print("Let's play Wordle!:")
    print("Six chances to guess a 5 letter word. Type your first guess and hit enter!\n")