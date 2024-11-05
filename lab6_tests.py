import data
import lab6
import unittest
from data import Book


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_closest_to_a_1(self):
        input = ['a', 'b', 'c']
        expected = 0
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_closest_to_a_2(self):
        input = ['hello', 'bye', 'see you']
        expected = 1
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_closest_to_a__3(self):
        input = ['a', 'b', 's', 'w', 'b']
        expected = 4
        actual = lab6.index_smallest_from(input, 2)
        self.assertEqual(expected, actual)


    def test_closest_to_a_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_books_1(self):
        book1 = Book([], "A title")
        book2 = Book([], "B title")
        book3 = Book([], "C title")
        book_list = [book1, book2, book3]
        expected = ['A title', 'B title', 'C title']
        actual = lab6.selection_sort_books(book_list)
        self.assertEqual(expected, actual)

    def test_selection_sort_books_2(self):
        book1 = Book([], "z title")
        book2 = Book([], "b title")
        book3 = Book([], "h title")
        book_list = [book1, book2, book3]
        expected = ['b title', 'h title', 'z title']
        actual = lab6.selection_sort_books(book_list)
        self.assertEqual(expected, actual)

    def test_selection_sort_books_3(self):
        input = []
        expected = None
        actual = lab6.selection_sort(input)
        self.assertEqual(expected, actual)

    def test_selection_sort_books_4(self):
        book1 = Book([], "+ title")
        book2 = Book([], "C title")
        book3 = Book([], "B title")
        book_list = [book1, book2, book3]
        expected = ['+ title', 'B title', 'C title']
        actual = lab6.selection_sort_books(book_list)
        self.assertEqual(expected, actual)



    # Part 2
    def test_swap_case_1(self):
        input = "Hello"
        expected = "hELLO"
        actual = lab6.swap_case(input)
        self.assertEqual(expected, actual)

    def test_swap_case_2(self):
        input = "Hi hI Hi 23 hi"
        expected = "hI Hi hI 23 HI"
        actual = lab6.swap_case(input)
        self.assertEqual(expected, actual)

    def test_swap_case_3(self):
        input = ""
        expected = ""
        actual = lab6.swap_case(input)
        self.assertEqual(expected, actual)

    # Part 3
    def test_str_translate_1(self):
        input = "abcabcabc"
        expected = "xbcxbcxbc"
        actual = lab6.str_translate(input, 'a', 'x')
        self.assertEqual(expected, actual)

    def test_str_translate_2(self):
        input = "abc%abc%abc%"
        expected = "abcdabcdabcd"
        actual = lab6.str_translate(input, '%', 'd')
        self.assertEqual(expected, actual)

    def test_str_translate_3(self):
        input = ""
        expected = ""
        actual = lab6.str_translate(input, '%', 'd')
        self.assertEqual(expected, actual)

    # Part 4

    def test_histogram_1(self):
        input = "hello hi hey hello hi hey hello hi hey hello"
        expected = {'hello': 4, 'hey': 3, 'hi': 3}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)

    def test_histogram_2(self):
        input = ""
        expected = {}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)

    def test_histogram_3(self):
        input = "hello hey hello  hey hello hi  hello"
        expected = {'hello': 4, 'hey': 2, 'hi': 1}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
