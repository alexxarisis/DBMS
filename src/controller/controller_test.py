import unittest   # The test framework

class Test_Plots(unittest.TestCase):
    def test_makeTimeLinePlot(self):
        
        self.assertEqual(inc_dec.increment(3), 4)

    def test_makeBarPlot(self):
        self.assertEqual(inc_dec.decrement(3), 4)
    def test_makeScatterPlot(self):
        self.assertEqual(inc_dec.decrement(3), 4)

if __name__ == '__main__':
    unittest.main()