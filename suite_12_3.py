import unittest
import test_12_3

runners_walkers = unittest.TestSuite()
runners_walkers.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
runners_walkers.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))

runloader = unittest.TextTestRunner(verbosity=2)
runloader.run(runners_walkers)