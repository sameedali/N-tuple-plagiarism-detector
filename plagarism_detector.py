"""
This module defines a plagarism detector in Python.
"""


class PlagarismDetector(object):
    """
    A class which defines the plagarism detector
    """

    def __init__(self, N=3):
        """
        Initializes the plagarism detector.

        @param N the size of N-tuple. default value = 3
        """
        self.N = N

    def get_similiarity_percentage(self, file1_words, file2_words):
        """
        Returns the similiarity score (see get_similiarity_score) as a
        percentage string.

        @param file1_words word list from file1 with synonms replaced
        @param file2_words word list from file2 with synonms replaced
        @returns the similiarity score (see get_similiarity_score) as
        a percentage string.
        """
        similiarity_score = self.get_similiarity_score(file1_words,
                                                       file2_words)
        return str(round(100.0 * similiarity_score, 3)) + "%"

    def get_similiarity_score(self, file1_words, file2_words):
        """
        Returns the similiarity score for the given file words by
        calculating the number of common tuples divided by the total
        tuples in file1.

        @param file1_words word list from file1 with synonms replaced
        @param file2_words word list from file2 with synonms replaced
        @returns number of common N-tuples/number of tuples in
        file1_words
        """
        file1_tuples_container = NTupleContainer(file1_words, self.N)
        file2_tuples_contianer = NTupleContainer(file2_words, self.N)
        similar_tuple_count = 0.0

        # This for loop takes O(n) time. The __contains__ method
        # defined in the NTupleContainer class words in O(1) so the
        # line `t in # file2_tuples_contianer` should run in O(1).
        for n_tuple in file1_tuples_container:
            if n_tuple in file2_tuples_contianer:
                similar_tuple_count += 1

        return similar_tuple_count/float(len(file1_tuples_container))


class NTupleContainer(object):
    """
    A custom ADT which holds the N-tuples found in a word list.

    This is used by the PlagarismDetector class to efficiently
    calculate the similiarity score
    """

    def __init__(self, word_list, N):
        """
        initializes the continer by generating all N-sized tuples from
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
        returns True if the container contains the given tuple in O(1)
        otherwise returns False
        """
        return item in self.tuple_dict

    def __len__(self):
        """
        returns the number of tuples held in the container.
        """
        return len(self.tuple_dict)

    def __iter__(self):
        """
        Allows the container to be iterable in python.
        """
        return iter(self.tuple_dict.keys())

    def __str__(self):
        """
        returns the elements contained in the container as a string.
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
