import unittest
from first_project import avg


class EasyTestCase(unittest.TestCase):

    def test_easy_input(self):
        self.assertEqual(avg(1, 2, 3),2)

    def test_easy_input_two(self):
        pass

class MediumTestCase(unittest.TestCase):

    def test_medium_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, "Augusto"),2)

    def test_medium_input_two(self):
       with self.assertRaises(TypeError):
           self.assertEqual(avg(1, 2, "3"),2)



class HardTestCase(unittest.TestCase):

    def test_hard_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, None),2)

    def test_hard_input_two(self):
       with self.assertRaises(TypeError):
           self.assertEqual(avg(1, 2, float),2)

    def test_hard_input_three(self):
       with self.assertRaises(TypeError):
           self.assertEqual(avg(1, 2, frozenset),2)

    def test_hard_input_four(self):
       with self.assertRaises(TypeError):
           self.assertEqual(avg(1, 2, set),2)


if __name__== '__main__':
    unittest.main()            