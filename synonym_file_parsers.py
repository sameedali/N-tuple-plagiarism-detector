from abc import ABC, abstractmethod


class AbstractSynonymParser(ABC):

    """
    Defined an abstract class for 
    """
    @abstractmethod
    def __init__(self, synonym_file):
        pass

    @abstractmethod
    def parse(self, file_name):
        pass
 
    @abstractmethod
    def get_synonyms(self):
        pass


class SpaceSeparatedSynonymFileParser(AbstractSynonymParser):

    """
    A class which instantiates a parser for the space separated synonym file
    """

    def __init__(self, synonym_file):
        self.synonym_dict = {}
        self.parse(synonym_file)

    def parse(self, file_name):
        """
        Reads the file given as the argument file_name and generates a
        dict of synonyms.
        """
        with open(file_name) as file_handler:
            for line in file_handler.readlines():
                words = line.split()
                synonym = words[0].lower()
                for word in words:
                    self.synonym_dict[word.lower()] = synonym
        return

    def get_synonyms(self):
        return self.synonym_dict
