import unittest
import test_runner
import test_runner_and_tournament

rtTS = unittest.TestSuite()
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_and_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rtTS)
