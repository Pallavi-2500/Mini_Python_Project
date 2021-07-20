'''
This is a test file for proj_numerology
'''
import unittest
from proj_numerology import life_path_no
from proj_numerology import heart_desire_no

class MyTestCase(unittest.TestCase):
    ''' Class created for cunit testing '''
    def test_life_path_no(self):
        '''This function tests whether the inputs to function are proper'''
        self.assertEqual(life_path_no(25062000), '6')
        self.assertEqual(heart_desire_no('pallavi sharma'), '7')
    def test_values(self):
        '''This function raises value errors when inputs to the function are not proper'''
        self.assertRaises(ValueError,life_path_no,-25 )

    def test_types(self):
        '''This function raises type errors when necessary'''
        self.assertRaises(TypeError, life_path_no,"pallavi")
        self.assertRaises(TypeError, life_path_no, True)
        self.assertRaises(TypeError, heart_desire_no, 25)
        self.assertRaises(TypeError, heart_desire_no, False)



if __name__ == '__main__':
    unittest.main()
