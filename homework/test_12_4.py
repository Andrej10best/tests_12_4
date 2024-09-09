import unittest
from unittest import TestCase
from main import Runner, Tournament
import logging
from logging import basicConfig



class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            self.people_1 = Runner('Max', -5)
            for _ in range(10):
                self.people_1.walk()
            self.assertEqual(self.people_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.people_2 = Runner(13.5)
            for _ in range(10):
                self.people_2.run()
            self.assertEqual(self.people_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.people_3 = Runner('Rick')
        self.people_4 = Runner('Morty')
        for _ in range(10):
            self.people_3.run()
        for _ in range(10):
            self.people_4.walk()
        self.assertNotEqual(self.people_3.distance, self.people_4.distance)


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            dict_ = {}
            for key, val in result.items():
                dict_[key] = val.name
            print(dict_)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_runner_1(self):
        self.race = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.race.start()
        result_win = self.all_results[max(self.all_results.keys())]
        self.assertTrue(result_win == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_runner_2(self):
        self.race = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.race.start()
        result_win = self.all_results[max(self.all_results.keys())]
        self.assertTrue(result_win == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_runner_3(self):
        self.race = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = self.race.start()
        result_win = self.all_results[max(self.all_results.keys())]
        self.assertTrue(result_win == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
     unittest.main()
     basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                 format='%(levelname)s %(message)s')

