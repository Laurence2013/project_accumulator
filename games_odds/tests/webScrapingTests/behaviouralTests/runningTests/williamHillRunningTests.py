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
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame3.wh3TestingWilliamHillDeleteOneCsvFile1 import Wh3TestingWilliamHillDeleteOneCsvFile1
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame3.wh3TestingWilliamHillDeleteTwoCsvFile2 import Wh3TestingWilliamHillDeleteTwoCsvFile2
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame3.wh3TestingWilliamHillDeleteThreeCsvFile3 import Wh3TestingWilliamHillDeleteThreeCsvFile3

from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame4.wh4TestingWilliamHillDeleteOneCsvFile1 import Wh4TestingWilliamHillDeleteOneCsvFile1
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame4.wh4TestingWilliamHillDeleteTwoCsvFile2 import Wh4TestingWilliamHillDeleteTwoCsvFile2
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame4.wh4TestingWilliamHillDeleteThreeCsvFile3 import Wh4TestingWilliamHillDeleteThreeCsvFile3

from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame5.wh5TestingWilliamHillDeleteOneCsvFile1 import Wh5TestingWilliamHillDeleteOneCsvFile1
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame5.wh5TestingWilliamHillDeleteTwoCsvFile2 import Wh5TestingWilliamHillDeleteTwoCsvFile2
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame5.wh5TestingWilliamHillDeleteThreeCsvFile3 import Wh5TestingWilliamHillDeleteThreeCsvFile3

from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame6.wh6TestingWilliamHillDeleteOneCsvFile1 import Wh6TestingWilliamHillDeleteOneCsvFile1
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame6.wh6TestingWilliamHillDeleteTwoCsvFile2 import Wh6TestingWilliamHillDeleteTwoCsvFile2
from games_odds.tests.webScrapingTests.behaviouralTests.williamHillGame6.wh6TestingWilliamHillDeleteThreeCsvFile3 import Wh6TestingWilliamHillDeleteThreeCsvFile3

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

        wh3_testingWilliamHillDeleteOneCsvFile1 = Wh3TestingWilliamHillDeleteOneCsvFile1()
        wh3_testingWilliamHillDeleteTwoCsvFile2 = Wh3TestingWilliamHillDeleteTwoCsvFile2()
        wh3_testingWilliamHillDeleteThreeCsvFile3 = Wh3TestingWilliamHillDeleteThreeCsvFile3()

        wh4_testingWilliamHillDeleteOneCsvFile1 = Wh4TestingWilliamHillDeleteOneCsvFile1()
        wh4_testingWilliamHillDeleteTwoCsvFile2 = Wh4TestingWilliamHillDeleteTwoCsvFile2()
        wh4_testingWilliamHillDeleteThreeCsvFile3 = Wh4TestingWilliamHillDeleteThreeCsvFile3()

        wh5_testingWilliamHillDeleteOneCsvFile1 = Wh5TestingWilliamHillDeleteOneCsvFile1()
        wh5_testingWilliamHillDeleteTwoCsvFile2 = Wh5TestingWilliamHillDeleteTwoCsvFile2()
        wh5_testingWilliamHillDeleteThreeCsvFile3 = Wh5TestingWilliamHillDeleteThreeCsvFile3()

        wh6_testingWilliamHillDeleteOneCsvFile1 = Wh6TestingWilliamHillDeleteOneCsvFile1()
        wh6_testingWilliamHillDeleteTwoCsvFile2 = Wh6TestingWilliamHillDeleteTwoCsvFile2()
        wh6_testingWilliamHillDeleteThreeCsvFile3 = Wh6TestingWilliamHillDeleteThreeCsvFile3()

        suite.addTest(testingWilliamHillDeleteOneCsvFile0)
        suite.addTest(testingWilliamHillDeleteTwoCsvFile1)
        suite.addTest(testingWilliamHillDeleteThreeCsvFile2)

        suite.addTest(testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(testingWilliamHillDeleteThreeCsvFile3)

        suite.addTest(wh2_testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(wh2_testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(wh2_testingWilliamHillDeleteThreeCsvFile3)

        suite.addTest(wh3_testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(wh3_testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(wh3_testingWilliamHillDeleteThreeCsvFile3)

        suite.addTest(wh4_testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(wh4_testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(wh4_testingWilliamHillDeleteThreeCsvFile3)

        suite.addTest(wh5_testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(wh5_testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(wh5_testingWilliamHillDeleteThreeCsvFile3)

        suite.addTest(wh6_testingWilliamHillDeleteOneCsvFile1)
        suite.addTest(wh6_testingWilliamHillDeleteTwoCsvFile2)
        suite.addTest(wh6_testingWilliamHillDeleteThreeCsvFile3)

        return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    test_suite = WilliamHillRunningTests()
    runner.run(test_suite.suite())
