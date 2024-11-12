from unittest import TestCase
import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {} # Создаём словарь для хранения результатов всех тестов

    def setUp(self):
        # создаем три объекта
        self.usein = Runner('Усейн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов в столбец
        for result in cls.all_results.values():
            print(result)
    def test_Usein_Nik(self): #создаем турнир для участников Усейн и Ник
        tournament = Tournament(90, self.usein, self.nik)
        # запускаем турнир
        results = tournament.start()
        TournamentTest.all_results['test_usein_nik_race'] = {k: v.name for k, v in results.items()}
        # проверяем что Ник финишировал последний
        self.assertTrue(results[max(results)].name == 'Ник')
    def test_Andrew_Nik(self):
        tornament = Tournament(90, self.andrew, self.nik)
        results = tornament.start()
        TournamentTest.all_results['test_andrew_nik_race'] = {k: v.name for k, v in results.items()}
        self.assertTrue(results[max(results)].name == 'Ник')
    def test_Usein_Andrew_Nik(self):
        tornament = Tournament(90, self.usein, self.andrew, self.nik)
        results = tornament.start()
        TournamentTest.all_results['test_usein_andrew_nik_race'] = {k: v.name for k, v in results.items()}
        self.assertTrue(results[max(results)].name == 'Ник')

# Запускаем тесты
if __name__ == '__main__':
    unittest.main()


