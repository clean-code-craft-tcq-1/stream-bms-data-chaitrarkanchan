import unittest
import receiver_functions
import receiver_input


class receiver_test(unittest.TestCase):
  def test_bms_param(self):
    self.assertTrue(receiver_functions.bms_min([10,12,14,15,18]))
    self.assertTrue(receiver_functions.bms_max([10,12,14,15,18]))
    self.assertTrue(receiver_functions.bms_movingaverage([10,12,14,15,18]))
    

    
if __name__ == '__main__':
  unittest.main()
