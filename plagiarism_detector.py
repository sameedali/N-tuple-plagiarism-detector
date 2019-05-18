"""
This module defines a plagiarism detector in Python.
"""


class PlagiarismDetector(object):
    """
    A class which defines the plagiarism detector
    """

    def __init__(self, N=3):
        """
        Initializes the plagiarism detector.

        @param N the size of N-tuple. default value = 3
        """
        self.N = N

    def get_similiarity_percentage_str(self, file1_words, file2_words):
        """
        Returns the similiarity score (see get_similiarity_score) as a
        percentage string.

        @param file1_words word list from file1 with synonyms replaced
        @param file2_words word list from file2 with synonyms replaced
        @returns the similiarity score percentage as a string.
        """
        similiarity_score = self.get_similiarity_score(file1_words,
                                                       file2_words)
        return str(int(round(100.0 * similiarity_score, 3))) + "%"

    def get_similiarity_score(self, file1_words, file2_words):
        """
        Returns the similiarity score for the given file words by
        calculating the number of common tuples divided by the total
        tuples in file1.

        @param file1_words word list from file1 with synonyms replaced
        @param file2_words word list from file2 with synonyms replaced
        @returns number of common N-tuples/number of tuples in
        file1_words
        """
        file1_tuples_container = NTupleContainer(file1_words, self.N)
        file2_tuples_contianer = NTupleContainer(file2_words, self.N)
        similar_tuple_count = 0.0
        total_tuple_count = float(len(file1_tuples_container))

        # This for loop takes O(n) time. The __contains__ method
        # defined in the NTupleContainer class words in O(1) so the
        # line `t in # file2_tuples_contianer` should run in O(1).
        for n_tuple in file1_tuples_container:
            if n_tuple in file2_tuples_contianer:
                similar_tuple_count += 1

        similarity_score = similar_tuple_count/total_tuple_count
        return similarity_score


class NTupleContainer(object):
    """
    A custom ADT which holds the N-tuples found in a word list.

    This is used by the PlagiarismDetector class to efficiently
    calculate the similarity score
    """

    def __init__(self, word_list, N):
        """
        initializes the container by generating all N-sized tuples from
        the word_list.
        """
        self.tuple_dict = {}
        self.populate_tuple_dict(word_list, N)

    def populate_tuple_dict(self, word_list, N):
        """
        Populates the tuple dict by finding all N tuples in word_list.
        """
        if N > len(word_list):
            raise NValueTooLarge("N is larger than the length of word_list.")
        if N <= 0:
            raise NValueTooSmall("Value of N cannot be <= 0")

        self.tuple_dict = {}
        sliding_window = []
        for word in word_list:
            sliding_window.append(word)
            if len(sliding_window) == N:
                self.tuple_dict[tuple(sliding_window)] = True
                # remove the last element so we can slide to the next
                # element when we append later
                sliding_window.pop(0)

    def __contains__(self, item):
        """
        Allows the use of the "in" keyword with this container.
        @return True if the container contains the given tuple in O(1)
        otherwise returns False
        """
        return item in self.tuple_dict

    def __len__(self):
        """
        Allows the len() function to work on this container.
        @return the number of tuples held in the container.
        """
        return len(self.tuple_dict)

    def __iter__(self):
        """
        Allows the container to be iterable in python.
        @returns an iterator over the tuples in the container
        """
        return iter(self.tuple_dict.keys())

    def __str__(self):
        """
        @return the elements contained in the container as a string.
        """
        return str(self.tuple_dict.keys())


class NValueTooLarge(Exception):
    """
    A custom exception which is raised when the value of N is too large.
    """
    pass


class NValueTooSmall(Exception):
    """
    A custom exception which is raised when the value of N <= 0.
    """
    pass
