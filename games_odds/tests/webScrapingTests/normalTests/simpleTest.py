from django.test import TestCase

class SimpleTest(TestCase):
    def test_sample_one(self):
        total = 2 + 2
        self.assertEqual(total, 4)
