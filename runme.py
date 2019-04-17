"""
This file shows an example of how to use the library
"""

import sys
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

    if len(sys.argv) == 1:
        print("To run with custom arguments: python3 runme.py file1.txt "
              + "file2.txt N syn_file.txt")
    elif len(sys.argv) == 3:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
    elif len(sys.argv) == 5:
        try:
            N = int(sys.argv[3])
            filename_1 = sys.argv[1]
            filename_2 = sys.argv[2]
            synonyms_filename = sys.argv[4]
        except ValueError as value_error:
            print("Could not convert supplied value of N to integer. Aborting.")
            print(str(value_error))
            sys.exit(0)
    else:
        print("incorrent number of arguments. Arguments should be like"
              + "python3 runme.py file1.txt file2.txt N syn_file.txt" +
              "or python3 runme.py file1.txt file2.txt")

    print("Running program with file1=" + filename_1 + " and file2="
          + filename_2 + ", N=" + str(N)
          + " and synonyms file=" + str(synonyms_filename))

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
        print("plagarism percentage is:", end="")
        print(plagarism_detector.get_similiarity_percentage_str(file1_words,
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
