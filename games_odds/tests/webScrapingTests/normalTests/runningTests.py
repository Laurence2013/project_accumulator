from django.test import TestCase
from games_odds.tests.webScrapingTests.normalTests.testingWilliamHillGame0 import TestingWilliamHillGame0
from games_odds.tests.webScrapingTests.normalTests.testingWilliamHillGame1 import TestingWilliamHillGame1
from games_odds.tests.webScrapingTests.normalTests.testingWilliamHill import TestingWilliamHill
from games_odds.tests.webScrapingTests.normalTests.testingRefreshDateAndTime0 import TestingRefreshDateAndTime0
from games_odds.tests.webScrapingTests.normalTests.testingRefreshDateAndTime1 import TestingRefreshDateAndTime1

class RunningTests(TestCase):
    def suite(self):
        suite = TestSuite()
        testingWilliamGame_0 = TestingWilliamHillGame0()
        testingWilliamGame_1 = TestingWilliamHillGame1()
        testingWilliamHill = TestingWilliamHill()
        testingRefreshDateAndTime_0 = TestingRefreshDateAndTime0()
        testingRefreshDateAndTime_1 = TestingRefreshDateAndTime1()

        suite.addTest(testingWilliamGame_0)
        suite.addTest(testingWilliamGame_1)
        suite.addTest(testingWilliamHill)
        suite.addTest(testingRefreshDateAndTime_0)
        suite.addTest(testingRefreshDateAndTime_1)

        return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    test_suite = RunningTests()
    runner.run(test_suite.suite())
