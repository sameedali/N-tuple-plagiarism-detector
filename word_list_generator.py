"""
This module defines a WordListGenerator class which generates
wordlists from an input text file for plagiarism detection.
"""
import re


class WordListGenerator(object):
    """
    A class which handles the word list generation for the plagiarism detection
    """

    def __init__(self, synonyms_dict, word_regex=r"[a-zA-z]+"):
        """
        Iniitalizes the WordListGenerator object

        @param synonyms_dict a dictionary of string->string mapping synonyms
        @param word_regex A regular expression which defines what a
        word is. By default it is only words consisting of alphabets.
        """
        self.synonym_dict = synonyms_dict
        self.word_regex = word_regex

    def convert_to_words(self, input_string):
        """
        Converts a given string into a list of lowercase words.
        Returns an empty list if no word is found.
        A word consists of alphabets only, defined by the regex
        [a-zA-Z]+ as default.
        A custom regex may be supplied by passing it as an argument to
        the WordListGenerator constructor

        Parameters:
        s (string): The input string which will be parsed into words

        Returns:
        List[string]: List of words parsed from string
        """
        return [word.lower() for word in re.findall(self.word_regex,
                                                    input_string)]

    def replace_synonyms(self, words):
        """
        Given a list of words, replace the synonyms wih the first
        synonym in the corresponding line of synonym file.

        Example if words are:
        ["hello", "run", "world"]

        the output would be:
        ["hello", "walk", world]

        where "walk run stroll" is the corresponding synonyms line in
        the synonyms file.

        @param words a list of strings
        @return a list of string with synonyms replaced as defined in
        the synonym_dict dictionary
        """
        return [self.synonym_dict[word] if word in self.synonym_dict else word
                for word in words]

    def generate_list(self, raw_input_string):
        """
        Generates a word list from a given input string, and
        replaces all synonyms in the word list with those in the synonym
        dictionary.

        @param raw_input_string the string read from the input file
        @returns a list of words with synonyms replaced
        """

        words = self.convert_to_words(raw_input_string)
        words = self.replace_synonyms(words)
        return words
