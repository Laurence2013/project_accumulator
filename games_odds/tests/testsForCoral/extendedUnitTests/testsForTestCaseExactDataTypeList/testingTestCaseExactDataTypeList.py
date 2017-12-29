from django.test import TestCase
from games_odds.tests.testsForCoral.extendedUnitTests.testCaseExactDataTypeList import TestCaseExactDataTypeList

'''
This unit test will test the TestCaseExactDataTypeList class for a scenario of two lists that differs from each other. This is a typical behaviour, that normally happens in real scenarios
'''

class TestingTestCaseExactDataTypeList(TestCase):
    def setUp(self):
        self.dataTypeList = TestCaseExactDataTypeList()
        self.diffListTypes1 = [['hello'],'my','name','is','lozza',187]
        self.diffListTypes2 = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53']]

    def test_01_len_of_diffListType1_is_not_equal_to_diffListType2(self):
        '''
        In here a scenario would be two different lists passed, but should return False and the assertNotEqual will PASS as it is NOT equal
        '''
        isLenSame = self.dataTypeList.checkBothListsAreEqualOfLength(self.diffListTypes1, self.diffListTypes2)
        print()
        self.assertEqual(False, isLenSame)

    def test_02_get_types(self):
        '''
        In here you have to pass the second argument to loop over it and pass the types in a list ready for comparing with the expected result
        '''
        self.dataTypeList.checkEachElementInList(self.diffListTypes2)
