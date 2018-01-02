from django.test import TestCase
from games_odds.tests.testsForCoral.extendedUnitTests.testCaseExactDataTypeList import TestCaseExactDataTypeList

'''
This unit test will test the TestCaseExactDataTypeList class for a scenario of two lists that differs from each other. This is a typical behaviour, that normally happens in real scenarios
'''

class TestingTestCaseExactDataTypeList(TestCase):
    def setUp(self):
        self.dataTypeList = TestCaseExactDataTypeList()
        self.diffListTypes1 = [['hello', 'world'],'my',['hel45453lo', 'world545'],'name','is','lozza',187]
        self.diffListTypes2 = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53']]
        self.diffListTypes3 = [['Wolves', 'v', 'Chelsea', '2.28', '5.30', '1.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53'], ['Bristol', 'City', 'v', 'Man', 'City', '6.00', '4.20', '1.53']]
        self.diffListTypes4 = [['Wolves', 'v', 'Bradford', '2.28', '5.30', '1.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53'], ['Bristol', 'City', 'v', 'Man', 'City', '6.00', '4.20', '1.53']]

    def test_01_len_of_diffListType1_is_not_equal_to_diffListType2(self):
        '''
        In here a scenario, two different lists passed in as arguments, isLenSame should return True and the assertEqual will PASS as it is supposed to be False
        '''
        isLenSame = self.dataTypeList.checkBothListsAreEqualOfLength(self.diffListTypes1, self.diffListTypes2)
        self.assertEqual(False, isLenSame)

    def test_02_checkIfListHasInnerList(self):
        '''
        In this scenario, no matter what index inner lists are in a list, the total amount of list should be the same, which is 2
        '''
        test_list = [['hello', 'world332'],'my','name','is','lozza',187,['he1212llo', 'wod332']]
        hasInnerList1 = self.dataTypeList.checkTheCorrectNumOfListinList(self.diffListTypes1)
        hasInnerList2 = self.dataTypeList.checkTheCorrectNumOfListinList(test_list)
        self.assertEqual(2, hasInnerList1[0])
        self.assertEqual(2, hasInnerList2[0])

    def test_03_checkIfListHasInnerList(self):
        '''
        In this scenario, no matter what index inner lists are in a list, the total amount of list should be the same, which is 2
        '''
        test_list = [['hello', 'world332'],'my','name','is','lozza',187,['he1212llo', 'wod332']]
        hasInnerList1 = self.dataTypeList.checkTheCorrectNumOfListinList(self.diffListTypes2)
        hasInnerList2 = self.dataTypeList.checkTheCorrectNumOfListinList(test_list)
        self.assertEqual(2, hasInnerList1[0])
        self.assertEqual(2, hasInnerList2[0])

    def test_04_checkIfListHasInnerList(self):
        '''
        In this scenario, no matter what index inner lists are in a list and no matter HOW MANY elements in each inner list, it should amount to 2
        '''
        test_list = [['hello', 'world332', 'w121orld332', 'worsdfld332'],'my','name','is','lozza',187,['aasas','he1212llo', 'wod332']]
        hasInnerList1 = self.dataTypeList.checkTheCorrectNumOfListinList(self.diffListTypes1)
        hasInnerList2 = self.dataTypeList.checkTheCorrectNumOfListinList(test_list)
        self.assertEqual(2, hasInnerList1[0])
        self.assertEqual(2, hasInnerList2[0])

    def test_05_checkIfListHasInnerList(self):
        '''
        In this scenario, no matter what index inner lists are in a list and no matter HOW MANY elements in each inner list, it should amount to 2
        '''
        test_list = [['hello', 'world332', 'w121orld332', 'worsdfld332'],'my','name','is','lozza',187,['aasas','he1212llo', 'wod332']]
        hasInnerList1 = self.dataTypeList.checkTheCorrectNumOfListinList(self.diffListTypes2)
        hasInnerList2 = self.dataTypeList.checkTheCorrectNumOfListinList(test_list)
        self.assertEqual(2, hasInnerList1[0])
        self.assertEqual(2, hasInnerList2[0])

    def test_06_comparing_types(self):
        '''
        In here two list as arguments, the first list index has an inner list, and the second list first index has an inner list, the return should be 2 as the both inner list have the number of the same data types in each inner list index
        '''
        test_list = [['hello', 2123],'my','name','is','lozza',187]
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList(self.diffListTypes1[0], test_list[0])
        self.assertFalse(getTotalListDataTypeLength)

    def test_07_comparing_types(self):
        '''
        In here two list as arguments, the first list index has an inner list, and the second list first index has an inner list, the return should be 2 as the both inner list have the number of the same data types in each inner list index
        '''
        test_list = [['hello', 2123],'my','name','is','lozza',187]
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList(self.diffListTypes1[0], test_list[0])
        self.assertFalse(getTotalListDataTypeLength)

    # def test_08_comparing_types(self):
    #     '''
    #     In here two list as arguments, the first list index has an inner list, and the second list first index has an inner list, the return should be 2 as the both inner list have the number of the same data types in each inner list index
    #     '''
    #     test_list = [['hello', '2123'],'my','name','is','lozza',187]
    #     getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList(self.diffListTypes1[0], test_list[0])
    #     self.assertFalse(getTotalListDataTypeLength)

    def test_09_comparing_types(self):
        '''
        In here you have two lists as arguments, the first list index has an inner list with two string data types, the second list has an inner list with one as a string data type and the second as a float data type, the result should equal to False
        '''
        test_list = [['hello', 32.32],'my','name','is','lozza',187]
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList(self.diffListTypes1[0], test_list[0])
        self.assertEqual(False, getTotalListDataTypeLength)

    def test_10_comparing_types(self):
        '''
        In here you have two lists as arguments, the first list index has an inner list with two string data types, the second list has an inner list with one as a string data type and the second as a float data type, the result should equal to False
        '''
        test_list = [[32.32, 'hello'],'my','name','is','lozza',187]
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList(self.diffListTypes1[0], test_list[0])
        self.assertEqual(False, getTotalListDataTypeLength)

    def test_11_comparing_types(self):
        test_list1 = [[32.32, 'hello'],[32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo']]
        hasInnerList = self.dataTypeList.checkTheCorrectNumOfListinList(test_list1)
        self.assertEqual([32.32, 'hello'], hasInnerList[1][0])
        self.assertEqual([32.232, 'hello1'], hasInnerList[1][1])
        self.assertEqual([32.352, 'he33llo'], hasInnerList[1][2])

    def test_12_comparing_types(self):
        test_list1 = [[32.32, 'hello'],[32.232, 32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo']]
        hasInnerList = self.dataTypeList.checkTheCorrectNumOfListinList(test_list1)
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList([32.32, 'hello'], hasInnerList[1][0])
        self.assertTrue(getTotalListDataTypeLength)

    def test_13_comparing_types(self):
        test_list1 = [[32.32, 'hello'],[32.232, 32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo']]
        hasInnerList = self.dataTypeList.checkTheCorrectNumOfListinList(test_list1)
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList([32.232, 32.232, 'hello1'], hasInnerList[1][1])
        self.assertTrue(getTotalListDataTypeLength)

    def test_14_comparing_types(self):
        test_list1 = [[32.32, 'hello'],[32.232, 32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo', 'he33llo', 2]]
        hasInnerList = self.dataTypeList.checkTheCorrectNumOfListinList(test_list1)
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList([32.352, 'he33llo', 'he33llo', 2], hasInnerList[1][2])
        self.assertTrue(getTotalListDataTypeLength)

    def test_15_comparing_types(self):
        test_list1 = [[32.32, 'hello'],[32.232, 32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo', 'he33llo', 2]]
        hasInnerList = self.dataTypeList.checkTheCorrectNumOfListinList(test_list1)
        getTotalListDataTypeLength = self.dataTypeList.checkInnerEachElementInList(['qorld', 32.232, 32.232, 'hello1'], hasInnerList[1][2])
        self.assertFalse(getTotalListDataTypeLength)

    def test_16_checkingInnerListNotTheSameLength(self):
        test_list1 = [[32.32, 'hello'],[32.232, 32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo', 'he33llo', 2]]
        getTotalListDataTypeLength = self.dataTypeList.checkBothListsAreEqualOfLength(['qorld', 32.232, 32.232, 'hello1'], test_list1[0])
        self.assertFalse(getTotalListDataTypeLength)

    def test_17_testing_as_whole(self):
        test_list1 = [[32.32, 'hello'],[32.232, 32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo', 'he33llo', 2]]
        getTotalListDataTypeLength = self.dataTypeList.assertDataTypeOfListIsEqual(self.diffListTypes3, test_list1)
        self.assertFalse(getTotalListDataTypeLength)

    def test_18_testing_as_whole(self):
        test_list1 = [[32.32, 'hello'],[32.232, 32.232, 'hello1'],'is','lozza',187, [32.352, 'he33llo', 'he33llo', 2]]
        getTotalListDataTypeLength = self.dataTypeList.assertDataTypeOfListIsEqual(self.diffListTypes3, self.diffListTypes3)
        self.assertTrue(getTotalListDataTypeLength)
