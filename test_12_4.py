import unittest
import rt_with_exceptions as runner
import logging


LOG_FILENAME = 'runner_test.log'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO, filemode="w", encoding='UTF-8',
    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_walk(self):
        try:
            ds1 = runner.Runner("Ivan", -100)
            for i in range(10):
                ds1.walk()
            logging.info("'test_walk' выполнен успешно")
            self.assertEqual(ds1.distance, 50)
            return ds1.distance
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            self.assertEqual(ds1.distance, 50)
            return ds1.distance


    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_run(self):
        try:
            ds2 = runner.Runner(2, 10)
            for i in range(10):
                ds2.run()
            self.assertEqual(ds2.distance, 100)
            logging.info("'test_run' выполнен успешно")
            return ds2.run().distance
        except:
            logging.warning("Неверный тип данных для Runner", exc_info=True)
            self.assertEqual(ds2.distance, 100)
            return ds2.distance


    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_chellenge(self):
        self.frst_r = runner.Runner(name="Iiigor")
        self.sec_r = runner.Runner(name="Oleg")
        for i in range(10):
            self.frst_r.run()
            self.sec_r.walk()
        self.assertNotEqual(self.frst_r.run, self.sec_r.walk)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):

        del cls.all_results


    def setUp(self):
        self.run_1 = runner.Runner('Усейн', 10)
        self.run_2 = runner.Runner('Андрей', 9)
        self.run_3 = runner.Runner('Ник', 3)
        self.results = {}

    def tearDown(self):

        self.all_results = self.results
        for key in self.all_results:
            print(key, self.all_results[key])
        print('___ ' * 20)
        super().tearDown()

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start1(self):
        d = runner.Tournament(90, self.run_1, self.run_3)
        ds1 = d.start()
        self.results = ds1
        self.assertTrue(self.results[2] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start2(self):
        d = runner.Tournament(90, self.run_2, self.run_3)
        ds2 = d.start()
        self.results = ds2
        self.assertTrue(self.results[2] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start3(self):
        d = runner.Tournament(90,  self.run_3, self.run_1, self.run_2)
        ds3 = d.start()
        self.results = ds3
        self.assertTrue(self.results[3] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start4(self):
        """Введен дополнительно """
        d = runner.Tournament(90,  self.run_2, self.run_1, self.run_3)
        ds4 = d.start()
        self.results = ds4
        self.assertTrue(self.results[2] == 'Андрей', 'Наличие логической ошибки в методе start')


if __name__ == '__main__':
    unittest.main()
