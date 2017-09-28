from django.test import TestCase

class SimpleTest(TestCase):
    def test_sample_one(self):
        total = 2 + 2
        self.assertEqual(total, 4)

    def test_sample_two(self):
        total = 2 + 3
        self.assertEqual(total, 5)

    def test_sample_three(self):
        total = 3 + 3
        assert(total) == 9
