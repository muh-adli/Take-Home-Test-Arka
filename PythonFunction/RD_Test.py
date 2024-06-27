import unittest
from .RemoveDuplicate import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def check_result(self, test_name, input_list, expected_output):
        print()
        print(f"Test Name: {test_name}")
        print(f"Input: {input_list}")
        result = remove_duplicates(input_list)
        print(f"Output: {result}")
        self.assertEqual(result, expected_output, f"Failed for input: {input_list}. Expected: {expected_output}, but got: {result}")

    def test_empty_list(self):
        self.check_result("test_empty_list", [], [])

    def test_single_element_list(self):
        self.check_result("test_single_element_list", [1], [1])

    def test_no_duplicates(self):
        self.check_result("test_no_duplicates", [1, 2, 3, 4], [1, 2, 3, 4])

    def test_with_duplicates(self):
        self.check_result("test_with_duplicates", [1, 2, 3, 2, 1, 4, 5, 4], [1, 2, 3, 4, 5])

    def test_all_duplicates(self):
        self.check_result("test_all_duplicates", [1, 1, 1, 1], [1])

    def test_string_elements(self):
        self.check_result("test_string_elements", ["Toyota", "BMW", "Toyota", "Volvo", "BMW"], ["Toyota", "BMW", "Volvo"])

    def test_mixed_elements(self):
        self.check_result("test_mixed_elements", [1, "Toyota", 2, "Toyota", 1, 3, "BMW"], [1, "Toyota", 2, 3, "BMW"])


if __name__ == '__main__':
    unittest.main()
