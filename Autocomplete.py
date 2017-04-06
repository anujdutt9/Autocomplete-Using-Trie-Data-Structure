# Autocomplete using Python, Trie Data Structure, Depthh First Search

# Author: Anuj Dutt
# Date Created: 4/6/2017

import os
import sys

# Ternary Search Tree Implementation
class Trie(object):
    # Function to Initialize the root node
    def __init__(self):
        # Initialize the Root Node
        # In a Trie, a root node is empty
        self.childNode = {}
        # Check if we have reached the end of the word (last character)
        self.word_finished = False


    # Add String to Trie
    def add_Child(self, word):
        # If string is empty
        if len(word) == 0:
            self.word_finished = True
            return
            # Each node except the Root node has a key
            # The key is the character from a string
            # The last key contains the value for the string
        key = word[0]  # First character of string

        # Update String after removing first character
        word = word[1:]
        # If the character already exists in the child Node to the Root Node
        # Continue adding the next characters of the word till it is done
        if key in self.childNode:
            self.childNode[key].add_Child(word)
        else:
            # If this character does not exist
            # Create a new node and insert the key character
            node = Trie()
            # Create the child node with key character
            self.childNode[key] = node
            # Keep on iterating till done with the word
            node.add_Child(word)


    # Function to Search Words based on Prefix Input.
    # If the prefix characters match, the word exists else it does not exist
    def search_word(self, prefix, word_keys=""):
        # Searach the word character by character using prefix
        # If the prefix characters exist, the word may exist
        # else, we can break here itself.
        if len(prefix) > 0:
            key = prefix[0]
            prefix = prefix[1:]
            # If the key 'character of prefix' matches the key in the tree
            # Append it to the word_keys to be returned as a string.
            if key in self.childNode:
                word_keys = word_keys + key
                self.childNode[key].search_word(prefix, word_keys)
            else:
                print('No match found...')
        else:
            # If we are at the leaf node, print out the string formed using word keys till now
            if self.word_finished == True:
                print('Suggested Word: ', word_keys)

            # If prefix get exhausted, Use Depth First Searach to traverse the tree
            for key in self.childNode.keys():
                self.childNode[key].DFS(word_keys + key)


    # Function to do a Depth First Search through the Trie to find the next Keys to prefix
    # Goes till the leaf node and returns all the strings that can be made
    def DFS(self, word_keys=None):
        # When hash of the current node is empty, that means it is a leaf node.
        # Hence print sofar (sofar is a string containing the path as character sequences through which state transition occured)
        if self.childNode.keys() == []:
            print('Suggested Word: ', word_keys)
            return

        # If we are at the last node i.e leaf node, we have reached the end of the string
        if self.word_finished == True:
            print('Suggested Word: ', word_keys)

        # Recursively call Depth First Search for all nodes pointed by the current key
        # current key is the parent to the leaf node/nodes
        for key in self.childNode.keys():
            # word_keys: contains the string till the parent node
            # Recursively call DFS and form strings using all its child nodes.
            self.childNode[key].DFS(word_keys + key)



# ------------------------ Testing ---------------------------
if __name__ == '__main__':
    # --------------- Usage Intructions -------------
    print('--- Autocomplete using Trie Data Structure ---\n')
    print('Usage:\n')
    print('1. Enter Prefix on prompt to get Suggested Words.\n')
    print('2. Enter QP on prompt to exit the code\n')
    print()
    # ------------------------------------------------
    trie = Trie()
    # open the Dictionary file and load the words into the Trie
    with open('words.txt','r') as f:
        words = f.readline().strip('\r\n')
        while words != '':
            trie.add_Child(words)
            words = f.readline().strip('\r\n')

    while True:
        print('Enter prefix: ', end='')
        prefix = input()
        if prefix == 'QP':
            print('Thanks for using... :)')
            break
        trie.search_word(prefix)
        print('\n')

# ----------------------------------- EOC ----------------------------------