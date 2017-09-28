from django.test import TestCase
from games_odds.tests.webScrapingTests.behaviouralTests.testingByGettingAllOddsFromTbodyLink0 import TestingByGettingAllOddsFromTbodyLink0
from games_odds.tests.webScrapingTests.behaviouralTests.testingCombineOddsWithItsMatch import TestingCombineOddsWithItsMatch
from games_odds.tests.webScrapingTests.behaviouralTests.testingConvertFractionToDecimal import TestingConvertFractionToDecimal
from games_odds.tests.webScrapingTests.behaviouralTests.testingEitherFilesAreEmptyOrNot import TestingEitherFilesAreEmptyOrNot
# from games_odds.tests.webScrapingTests.behaviouralTests.testingGettingFootballTeamNames import TestingGettingFootballTeamNames
from games_odds.tests.webScrapingTests.behaviouralTests.testingWilliamHillFootballSpanLinksShould import TestingWilliamHillFootballSpanLinksShould
from games_odds.tests.webScrapingTests.behaviouralTests.testingWilliamHillFootballTbodyLinksShould import TestingWilliamHillFootballTbodyLinksShould

class RunningTests(TestCase):
    def suite(self):
        suite = TestSuite()
        testingEitherFilesAreEmptyOrNot = TestingEitherFilesAreEmptyOrNot()
        testingWilliamHillFootballTbodyLinksShould = testingWilliamHillFootballTbodyLinksShould()
        # TestingWilliamHillFootballSpanLinksShould = TestingWilliamHillFootballSpanLinksShould()
        # testingByGettingAllOddsFromTbodyLink0 = TestingByGettingAllOddsFromTbodyLink0()
        # testingConvertFractionToDecimal = TestingConvertFractionToDecimal()
        # testingCombineOddsWithItsMatch = TestingCombineOddsWithItsMatch()

        suite.addTest(testingEitherFilesAreEmptyOrNot)
        suite.addTest(testingWilliamHillFootballTbodyLinksShould)
        # suite.addTest(TestingWilliamHillFootballSpanLinksShould)
        # suitsuite.addTest(testingByGettingAllOddsFromTbodyLink0)
        # suite.addTest(testingConvertFractionToDecimal)
        # suite.addTest(testingCombineOddsWithItsMatch)

        return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    test_suite = RunningTests()
    runner.run(test_suite.suite())
