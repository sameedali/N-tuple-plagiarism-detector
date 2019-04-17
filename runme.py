"""
This file shows an example of how to use the library
"""

from plagarism_detector import PlagarismDetector
from plagarism_detector import NValueTooLarge
from plagarism_detector import NValueTooSmall
from word_list_generator import WordListGenerator
from synonym_file_parsers import SpaceSeparatedSynonymFileParser


def main():
    filename_1 = "file1.txt"
    filename_2 = "file2.txt"
    synonyms_filename = "syns.txt"
    N = 3

    try:
        synonym_file_parser = SpaceSeparatedSynonymFileParser(synonyms_filename)
        synonyms_dict = synonym_file_parser.get_synonyms()

        word_list_generator = WordListGenerator(synonyms_dict)


        with open(filename_1) as file1_handle:
            file1_string = file1_handle.read()
            file1_words = word_list_generator.generate_list(file1_string)

        with open(filename_2) as file2_handle:
            file2_string = file2_handle.read()
            file2_words = word_list_generator.generate_list(file2_string)

        plagarism_detector = PlagarismDetector(N)
        print(plagarism_detector.get_similiarity_percentage(file1_words,
                                                            file2_words))
    except IOError as ioerror:
        print("Error opeining file. Aborting program.")
        print(str(ioerror))
    except NValueTooLarge as nvalueerror:
        print(str(nvalueerror))
        print("Exception occurred. Aborting program.")
    except NValueTooSmall as nvalueerror:
        print(str(nvalueerror))
        print("Exception occurred. Aborting program.")
    return

if __name__ == "__main__":
    main()
