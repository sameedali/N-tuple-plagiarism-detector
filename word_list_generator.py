import re


class WordListGenerator(object):
    """
    TODO:
    """

    def __init__(self, synonyms_dict):
        self.synonym_dict = synonyms_dict

    @staticmethod
    def convert_to_words(input_string):
        """
        Converts a given string into a list of lowercase words.
        Returns an empty list if no word is found.
        A word consists of alphabets only, defined by the regex [a-zA-Z]+.

        Parameters:
        s (string): The input string which will be parsed into words

        Returns:
        List: List of words parsed from string
        """
        word_regex = r"[a-zA-z]+"
        return [word.lower() for word in re.findall(word_regex, input_string)]

    def replace_synonyms(self, words):
        """
        Given a list of words, replace the synonyms wih the first
        synonym in the synonym list.
        example:
        ["hello", "run", "world"] -> ["hello", "walk", world]
        synonym file:
        walk run stroll
        """
        return [self.synonym_dict[word] if word in self.synonym_dict else word
                for word in words]

    def generate_list(self, raw_input_string):
        """
        TODO:
        """
        words = self.convert_to_words(raw_input_string)
        words = self.replace_synonyms(words)
        return words
