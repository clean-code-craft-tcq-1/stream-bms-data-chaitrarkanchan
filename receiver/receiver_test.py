import unittest
import receiver_functions
import receiver_input


class receiver_test(unittest.TestCase):
  def test_bms_param(self):
    self.assertTrue(receiver_functions.bms_min([12,13,16,18,20]))
    self.assertTrue(bms_min == 12)
    self.assertTrue(receiver_functions.bms_max([12,13,16,18,20]))
    self.assertTrue(bms_max == 20)
    self.assertTrue(receiver_functions.bms_movingaverage([12,13,16,18,20]))
    
if __name__ == '__main__':
  unittest.main()
