from unittest import TestCase

from python.models.coordinate import Coordinate


class TestCoordinate(TestCase):

    def setUp(self) -> None:
        self.coordinate = Coordinate(1, 2)

    def test_coordinate(self):
        pass

    def test_clone(self):
        self.assertEqual(Coordinate(-1, -1), Coordinate(-1, -1).clone())
        self.assertEqual(Coordinate(1, 2), Coordinate(1, 2).clone())
        self.assertEqual(Coordinate(1, 3), Coordinate(1, 3).clone())
        self.assertEqual(Coordinate(1, 4), Coordinate(1, 4).clone())

    def test_random(self):
        pass

    def test_in_direction(self):
        pass

    def test_in_inverse(self):
        pass
