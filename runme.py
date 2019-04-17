from plagarism_detector import PlagarismDetector
from word_list_generator import WordListGenerator
from synonym_file_parsers import SpaceSeparatedSynonymFileParser

def main():
    """
    """
    filename_1 = "file1.txt"
    filename_2 = "file2.txt"
    synonyms_filename = "syns.txt"
    N = 3

    synonym_file_parser = SpaceSeparatedSynonymFileParser(synonyms_filename)
    synonyms_dict = synonym_file_parser.get_synonyms()
    word_list_generator = WordListGenerator(synonyms_dict)

    with open(filename_1) as file1_handle:
        file1_words = word_list_generator.generate_list(file1_handle.read())
    with open(filename_2) as file2_handle:
        file2_words = word_list_generator.generate_list(file2_handle.read())

    p = PlagarismDetector(N)
    print(p.get_similiarity_percentage(file1_words, file2_words))
    return

if __name__ == "__main__":
    main()
