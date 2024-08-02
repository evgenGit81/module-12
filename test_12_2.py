# -*- coding: utf-8 -*-
import unittest
import runner_and_tournament as iat


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):

        del cls.all_results

    def setUp(self):
        # super().setUp()
        self.run_1 = iat.Runner('Усейн', 10)
        self.run_2 = iat.Runner('Андрей', 9)
        self.run_3 = iat.Runner('Ник', 3)
        self.results = {}


    def tearDown(self):

        self.all_results = self.results
        print(self.all_results)
        for key in self.all_results:
            print(key, self.all_results[key])
        print('___ ' * 20)
        super().tearDown()


    def test_start1(self):
        d = iat.Tournament(90, self.run_1, self.run_3)
        ds1 = d.start()
        self.results = ds1
        self.assertTrue(self.results[2] == 'Ник')

    def test_start2(self):
        d = iat.Tournament(90, self.run_2, self.run_3)
        ds2 = d.start()
        self.results = ds2
        self.assertTrue(self.results[2] == 'Ник')


    def test_start3(self):
        d = iat.Tournament(90,  self.run_3, self.run_1, self.run_2)
        ds3 = d.start()
        self.results = ds3
        self.assertTrue(self.results[3] == 'Ник')


    def test_start4(self):
        """Введен дополнительно """
        d = iat.Tournament(90,  self.run_2, self.run_1, self.run_3)
        ds4 = d.start()
        self.results = ds4
        self.assertTrue(self.results[2] == 'Андрей', 'Наличие логической ошибки в методе start')


if __name__ == '__main__':
    unittest.main()

