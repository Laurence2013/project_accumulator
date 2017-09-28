from django.test import TestCase
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame0.testingWilliamHillDeleteOneCsvFile0 import TestingWilliamHillDeleteOneCsvFile0
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame0.testingWilliamHillDeleteTwoCsvFile1 import TestingWilliamHillDeleteTwoCsvFile1
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame0.testingWilliamHillDeleteThreeCsvFile2 import TestingWilliamHillDeleteThreeCsvFile2
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame1.testingWilliamHillDeleteOneCsvFile1 import TestingWilliamHillDeleteOneCsvFile1
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame1.testingWilliamHillDeleteTwoCsvFile2 import TestingWilliamHillDeleteTwoCsvFile2
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame1.testingWilliamHillDeleteThreeCsvFile3 import TestingWilliamHillDeleteThreeCsvFile3
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame2.wh2TestingWilliamHillDeleteOneCsvFile1 import Wh2TestingWilliamHillDeleteOneCsvFile1
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame2.wh2TestingWilliamHillDeleteTwoCsvFile2 import Wh2TestingWilliamHillDeleteTwoCsvFile2
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame2.wh2TestingWilliamHillDeleteThreeCsvFile3 import Wh2TestingWilliamHillDeleteThreeCsvFile3

class WilliamHillRunningTests(TestCase):
    def suite(self):
        suite = TestSuite()
        testingWilliamHillDeleteOneCsvFile0 = TestingWilliamHillDeleteOneCsvFile0()
        testingWilliamHillDeleteTwoCsvFile1 = TestingWilliamHillDeleteTwoCsvFile1()
        testingWilliamHillDeleteThreeCsvFile2 = TestingWilliamHillDeleteThreeCsvFile2()

        testingWilliamHillDeleteOneCsvFile1 = TestingWilliamHillDeleteOneCsvFile1()
        testingWilliamHillDeleteTwoCsvFile2 = TestingWilliamHillDeleteTwoCsvFile2()
        testingWilliamHillDeleteThreeCsvFile3 = TestingWilliamHillDeleteThreeCsvFile3()

        wh2_testingWilliamHillDeleteOneCsvFile1 = Wh2TestingWilliamHillDeleteOneCsvFile1()
        wh2_testingWilliamHillDeleteTwoCsvFile2 = wh2TestingWilliamHillDeleteTwoCsvFile2()
        wh2_testingWilliamHillDeleteThreeCsvFile3 = wh2TestingWilliamHillDeleteThreeCsvFile3()

        suite.addTest(testingWilliamHillDeleteOneCsvFile0)
        suite.addTest(testingWilliamHillDeleteTwoCsvFile1)
        suite.addTest(testingWilliamHillDeleteThreeCsvFile2)

        suite.addTest(testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(testingWilliamHillDeleteThreeCsvFile3)

        suite.addTest(wh2_testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(wh2_testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(wh2_testingWilliamHillDeleteThreeCsvFile3)

        return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    test_suite = WilliamHillRunningTests()
    runner.run(test_suite.suite())
