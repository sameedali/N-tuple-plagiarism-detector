class PlagarismDetector(object):
    def __init__(self, N=3):
        self.N = N

    def get_similiarity_percentage(self, file1_words, file2_words):
        similiarity_score = self.get_similiarity_score(file1_words, file2_words)
        return str(round(100.0 * similiarity_score, 3)) + "%"

    def get_similiarity_score(self, file1_words, file2_words):
        """
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
    TODO:
    """

    def __init__(self, word_list, N):
        """
        """
        self.tuple_dict = {}
        self.populate_tuple_dict(word_list, N)

    def populate_tuple_dict(self, word_list, N):
        """
        populates the tuple dict by finding all N tuples in word_list
        """
        # FIXME:
        assert N <= len(word_list)

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
        checks if the container contains the given tuple in O(1)
        """
        return item in self.tuple_dict

    def __len__(self):
        return len(self.tuple_dict)

    def __iter__(self):
        return iter(self.tuple_dict.keys())

    def __str__(self):
        return str(self.tuple_dict.keys())
