from collections import defaultdict
import random


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):
        '''
        Build a term dictionary mapping each word in the corpus to a list of words 
        that immediately follow it.

        This function splits the corpus text into individual words, then iterates 
        through them to create a mapping where each key is a word and its value 
        is a list of words that occur directly after that word in the corpus.

        Returns
        -------
        dict
            A dictionary where keys are words (str) and values are lists of 
            subsequent words (list of str).
        '''

        self.corpus = self.corpus.split()

        self.term_dict = defaultdict(list)

        index = 1


        for word in self.corpus:
            if index < len(self.corpus) - 1:
                self.term_dict[word].append(self.corpus[index])
                index += 1
            else:
                return self.term_dict


    def generate(self, seed_term=None, term_count=15):
        """
        Generate a random sentence based on the term dictionary.

        This function uses the term dictionary defined above to iteratively
        build a sequence of words, starting from an optionally given seed term. 
        Each next word is randomly chosen from the list of words that follow the 
        current word in the term dictionary. If a seed term is not provided, a random
        starting term is selected from the dictionary.

        Parameters
        ----------
        seed_term : str, optional
            The initial word to start the generated sentence. 
            If not provided, a random key from the term dictionary is used. 
            Raises a ValueError if the provided seed term is not found in the dictionary.
        term_count : int, optional
            The number of terms to include in the generated sentence.
            Defaults to 15.

        Returns
        -------
        str
            A randomly generated sentence composed of words derived from
            the term dictionary starting with the given or randomized
            seed term.

        Raises
        ------
        ValueError
            If a non-None seed term is provided that does not currently exist in the
            term dictionary produced.
        """

        sentence = ""
        word_count = 0
        next_word = ''

        if seed_term not in self.term_dict:
            if seed_term == None:
                keys_list = list(self.term_dict.keys())
                random_word = random.choice(keys_list)
                seed_term = random_word
            else:
                raise ValueError("This term is not in the term dictionary!")

        while word_count < term_count:
            if word_count == 0:
                curr_word = seed_term
            else:
                curr_word = next_word
            sentence += curr_word + " "

            if len(self.term_dict[curr_word]) < 1:
                next_word = random.choice(keys_list)
            else:
                next_word = random.choice(self.term_dict[curr_word])
            word_count += 1

        return sentence