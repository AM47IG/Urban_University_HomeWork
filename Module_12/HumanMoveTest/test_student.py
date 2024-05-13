import unittest
from main import Student


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student_one = Student('Вася')
        self.student_two = Student('Гена')

    def test_walk(self):
        [self.student_one.run() for _ in range(10)]
        result = self.student_one.distance
        target = 100
        msg = f'Дистанции не равны [дистанция человека(объекта)] != {target}'
        self.assertEqual(result, target, msg)

    def test_run(self):
        [self.student_two.walk() for _ in range(10)]
        result = self.student_two.distance
        target = 50
        msg = f'Дистанции не равны [дистанция человека(объекта)] != {target}'
        self.assertEqual(result, target, msg)

    def test_race(self):
        self.student_one.run()
        self.student_two.walk()
        result_one = self.student_one.distance
        result_two = self.student_two.distance
        msg = '[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].'
        self.assertGreater(result_one, result_two, msg)


if __name__ == '__main__':
    unittest.main()
