SAMEED ALI

Assumptions
===========
1. A word is defined as containing uppercase and lowercase letter
only. To change this pass the alternate regex in the argument for
WordListGenerator constructor.

2. Code is written in python3.

3. A N-tuple is counted once even if it occurs multiple times in file2.

Design Summary
==============
A simple summary of what the code does is as follows:
1. A wordlist is generated from the input text files by parsing out
the words as a list of strings.

2. The synonyms in this wordlist are then replaced by the first
synonym in the corresponding line of the synonym file example:

"go for a walk" will be parsed as ["go","for", "a", "walk"]
then walk will be replaced by "run" if the synonym table contains the
line "run walk stroll".
This is because in the synonym file run was the first synonym in the
corresponding synonym line.
I chose to do this because the question wants to treat all synonyms as
the same word.

3. N-tuples are constructed from the above word lists for both files.

4. The number of N-tuples in file1 that also exist in file2 are
counted and the percentage calculated.


Code structure
==============
The code consists of the following files:
   runme.py
   plagarism_detector.py
   synonym_file_parsers.py
   word_list_generator.py

The file runme is contains the main() function and is the one the user
should run as:
$ python3 runme.py file1.txt file2.txt N syn_list.txt
or
$ python3 runme.py file1.txt file2.txt

This command will print out the usage instructions:
$ python3 runme.py

The synonym_file_parsers.py contains the synonym file parser.
The word_list_generator.py contains the class responsible for
generating a word list from the input file strings and replacing
synonyms as explained in the design summary. It takes the synonyms as
a dictionary in its constructor arguments.

The plagiarism_detector.py defines two classes the NTupleContainer
class generates the N-tuples from the word lists and provides methods
to iterate over and query the generated N-tuples.

It is used by the PlagiarismDetector class as a helper when it
calculates the similarity score.

The PlagiarismDetector class takes in two word lists, uses the
NTupleContainer to generate Ntuples and then computes the similarity
score.

Design Decisions and optimizations
==================================
> While getting the right answer is important, we are also interested
  in how well thought out your solution is; are there easier, or faster ways?
> Is the code understandable to another engineer picking it up?

I chose to store the synonym list in a hash table data structure so we
can do O(1) time lookup when we are given a word to see if it has a
synonym or not.

Furhtermore, the N-tuples generated from the text input files are also
stored in a Hash Table so we can do O(1) time lookup. We need this so
can efficiently check if one file contains a tuple that is also there
in another file another file.

I created a custom class called NTupleContainer which holds the
N-tuples and I defined the __contains__ and __iter__ methods so I
could iterate over it and check if a tuple is contained in it in a
more readable way.

By defining these methods I can write more easy to understand and
readable code like use the"in" keyword to check if a tuple is in the
custom data structure. For example:

> for n_tuple in file1_tuples_container: # readable looping
>     if n_tuple in file2_tuples_contianer: # I can use "in" keyword; it is in O(1) as well as I used a hastable
>         similar_tuple_count += 1

I chose to do this so if another engineer were to continue working on
this code, they could do it easily.

I have extensively documented the code, and chosen self explanatory
variable and function names.

Furthermore, I chose to write a generator class which accepts the
synonyms list as input into its constructor so we can use the same
class to generate the word lists for multiple files.

I have also handled exceptions in the code and made custom exceptions
and used them where appropriate.

> If there are obvious ways it could be abstracted or extended, is it
  designed to support that? 
> For example, this N-tuple detection algorithm may end up being used
  in other contexts (like a website) and so should be easy to reuse.

I designed the code to be as modular as possible. This allows the code
to be easily extended in the future.

For example if we need to support a different file format for the
synonym file all we need to do is write another class which inherits
from the abstract base class for the synonym parser and use that as
the parser and rest of the code will work as expected.

Furthermore, the words in the input file are split on a regular
expression, which can be modified by passing an additional parameter
and the code will work for an alternate definition of word.

