# unit_testing

Wrote unit test for a function that calculates the area of a circle considering multiple user cases.

For areas greater than zero, use the 
assertAlmostEqual(the function with an argument, and the actual result).
    if the ouput are equal to 3d.p python assumes the values are equal.

For common input errors like negative number etc, use the 
assertRaises(the error to be raised, the function, the wrong input)
    eg def test_values(self):
            self.assertRaises(ValueError, circle_area, -2)