import unittest
import receiver_functions
import receiver_input


class receiver_test(unittest.TestCase):  
  def test_bms_param(self):
   
    self.assertTrue(receiver_functions.bms_min_temp([12,13,16,18,20]))
    self.assertTrue(receiver_functions.bms_min_soc([11,12,15,17,19]))    
    self.assertTrue(receiver_functions.bms_max_temp([12,13,16,18,20]))
    self.assertTrue(receiver_functions.bms_max_soc([11,12,15,17,19]))     
    self.assertTrue(receiver_functions.bms_movingaverage([12,13,16,18,20],[11,12,15,17,19]))
    
if __name__ == '__main__':
  unittest.main()
