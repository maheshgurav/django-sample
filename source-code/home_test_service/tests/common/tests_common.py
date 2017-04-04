'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''

import unittest
from common.common_methods import remove_common_words, get_stem_words,\
    add_letters_in_term

class TestCommonMethods(unittest.TestCase):


    def test_remove_common_words_correct_result(self):
        self.assertListEqual(remove_common_words("Hotel The Prime"), ['prime'])


    def test_remove_common_words_incorrect_result(self):
        self.assertNotEqual(remove_common_words("Hotel The Prime"), ['Prime'])


    def test_remove_common_words_empty_result(self):
        self.assertListEqual(remove_common_words("Hotel The"), [])


    def test_get_stem_words_correct_result(self):
        self.assertListEqual(get_stem_words(["Hotelling", "Swimming"]), ["Hotel", "Swim"])


    def test_get_stem_words_incorrect_result(self):
        self.assertNotEqual(get_stem_words(["Hotelling", "Swimming"]), ["Hotelling", "Swimming"])


    def test_add_letters_in_term_correct_result(self):
        self.assertListEqual(add_letters_in_term("a"), ["aa", "ae", "ai", "ao", "au", "aj", "a1","a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a&"])


    def test_add_letters_in_term_incorrect_result(self):
        self.assertNotEqual(get_stem_words(["Hotelling", "Swimming"]), ["Hotelling", "Swimming"])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()