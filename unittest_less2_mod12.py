# -*- coding: utf-8 -*-
import unittest
import runner_and_tournament as iat
# from pprint import pprint


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        super().setUp()
        # self.runner_1 = {'Усейн': 10}
        # self.runner_2 = {'Андрей': 9}
        # self.runner_3 = {'Ник': 3}
        self.run_1 = iat.Runner('Усейн', 10)
        self.run_2 = iat.Runner('Андрей', 9)
        self.run_3 = iat.Runner('Ник', 3)
        # self.list_runs = [[self.run_1, self.run_3], [self.run_2, self.run_3], [self.run_2, self.run_1, self.run_3]]

    @classmethod
    def tearDownClass(cls):
        print("Результаты забега: ", cls.all_results)
        del cls.all_results
        # for n, run in cls.all_results.items():
        #     # print(n, run)
        #     print('забег N', n)
        #     print(cls.all_results.items())
        #     for key, value in run.items():
        #         print(key, value, run.items())

    def test_start1(self):
        d = iat.Tournament(90, self.run_1, self.run_3)
        ds1 = d.start()
        print(ds1)
        self.all_results = ds1
        self.assertTrue(ds1 == 'Ник')

    def test_start2(self):
        d = iat.Tournament(90, self.run_2, self.run_3)
        ds2 = d.start()
        print(ds2)
        self.all_results = ds2
        self.assertTrue(ds2 == 'Ник')

    def test_start3(self):
        d = iat.Tournament(90, self.run_2, self.run_1, self.run_3)
        ds3 = d.start()
        print(ds3)
        self.all_results = ds3
        self.assertTrue(ds3 == 'Ник')


if __name__ == '__main__':
    unittest.main()
