import unittest
from RemoveDuplicate import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def check_result(self, input_list, expected_output):
        result = remove_duplicates(input_list)
        self.assertEqual(result, expected_output, f"Failed for input: {input_list}. Expected: {expected_output}, but got: {result}")

    def test_empty_list(self):
        self.check_result([], [])

    def test_single_element_list(self):
        self.check_result([1], [1])

    def test_no_duplicates(self):
        self.check_result([1, 2, 3, 4], [1, 2, 3, 4])

    def test_with_duplicates(self):
        self.check_result([1, 2, 3, 2, 1, 4, 5, 4], [1, 2, 3, 4, 5])

    def test_all_duplicates(self):
        self.check_result([1, 1, 1, 1], [1])

    def test_string_elements(self):
        self.check_result(["a", "b", "a", "c", "b"], ["a", "b", "c"])

    def test_mixed_elements(self):
        self.check_result([1, "a", 2, "a", 1, 3, "b"], [1, "a", 2, 3, "b"])

if __name__ == '__main__':
    unittest.main()
