import unittest
import numpy as np

from sorting import main


class TestSum(unittest.TestCase):
    def test_list_int(self):

        Pass = True        
        data = main()  
        if (np.shape(data[0])) != ():
            for j in range(data.shape[0]):    
                for i in range((data.shape[1])-1):
                    if data[j][i] <= data[j][i+1] :
                        Pass = True
                    else :
                        Pass = False
                    self.assertEqual(Pass, True) 
        else :
            for i in range(len(data)-1):
                if data[i] <= data[i+1] :
                    Pass = True
                else :
                    Pass = False
                self.assertEqual(Pass, True) 
    
if __name__ == '__main__':
    unittest.main()