# -*- coding: utf-8 -*-
import unittest
import runner2

class RannerTest(unittest.TestCase):

    def test_walk(self):
        ds1 = runner2.Runner("Ivan")
        for i in range(10):
            ds1.walk()
        self.assertEqual(ds1.distance, 50)

    def test_run(self):
        ds2 = runner2.Runner("Petr")
        for i in range(10):
            ds2.run()
        self.assertEqual(ds2.distance, 100)
        
    def test_chellenge(self):
        self.frst_r - runner2.Runner(name="Iiigor")
        self.sec_r - runner2.Runner(name="Oleg")
        for i in range(10):
            self.frst_r.run()
            self.sec_r.walk()
        self.assertNotEqual(self.frst_r.run, self.sec_r.walk)


if __name__ == '__main__':
    unittest.main()
