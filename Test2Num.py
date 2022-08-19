from Add2Num import MyBigNumber
import unittest
class TestSumMethods(unittest.TestCase):
    def test_sum(self):
        BigNum = MyBigNumber()
        # Case of Different length and having a remainder over to the last digit
        self.assertEqual(BigNum.sum("192780","33221"), "226001", "Should be 226001")
        # Basic sum
        self.assertEqual(BigNum.sum("1","2"), "3", "Should be 3")
        # The two functions below test different lenght sums
        self.assertEqual(BigNum.sum("1","200"), "201", "Should be 201")
        self.assertEqual(BigNum.sum("1","20"), "21", "Should be 21")
        # Case of the last digit having a remainder
        self.assertEqual(BigNum.sum("77378279320090","61813294987513"), "139191574307603", "Should be 139191574307603")


unittest.main()