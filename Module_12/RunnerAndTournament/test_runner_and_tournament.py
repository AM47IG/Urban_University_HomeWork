import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_win = Runner('Усэйн', 10)
        self.runner_two = Runner('Андрей', 9)
        self.runner_loser = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(*cls.all_results, sep='\n')

    def test_1(self):
        tournament = Tournament(90, self.runner_win, self.runner_loser)
        result = tournament.start()
        self.all_results.append(result)
        msg1 = f'Самый медленный бегун не последний!'
        msg2 = f'Самый быстрый бегун не первый!'
        self.assertTrue(result[2] == self.runner_loser, msg1)  # Словарь не способен по индексу [-1] вывести последнего
        self.assertTrue(result[1] == self.runner_win, msg2)

    def test_2(self):
        tournament = Tournament(90, self.runner_two, self.runner_loser)
        result = tournament.start()
        self.all_results.append(result)
        msg1 = f'Самый медленный бегун не последний!'
        msg2 = f'Самый быстрый бегун не первый!'
        self.assertTrue(result[2] == self.runner_loser, msg1)  # Словарь не способен по индексу [-1] вывести последнего
        self.assertTrue(result[1] == self.runner_two, msg2)

    def test_3(self):
        tournament = Tournament(90, self.runner_win, self.runner_two, self.runner_loser)
        result = tournament.start()
        self.all_results.append(result)
        msg1 = f'Самый медленный бегун не последний!'
        msg2 = f'Самый быстрый бегун не первый!'
        self.assertTrue(result[3] == self.runner_loser, msg1)  # Словарь не способен по индексу [-1] вывести последнего
        self.assertTrue(result[1] == self.runner_win, msg2)


if __name__ == '__main__':
    unittest.main()
