'''
This new prototype assertDataTypeOfListIsEqual, is very important test for the integration test. This is because it further test more if the games crawled from the website behaves a certain way
'''

class TestCaseExactDataTypeList:
    def assertDataTypeOfListIsEqual(self, list1, list2):
        isLenSame = self.checkBothListsAreEqualOfLength(list1, list2)
        if isLenSame is True:
            innerList1 = self.checkTheCorrectNumOfListinList(list1)
            innerList2 = self.checkTheCorrectNumOfListinList(list2)
            if innerList1[0] is innerList2[0]:
                isTheSame = self.checkInnerEachElementInList(innerList1[1], innerList2[1])
                if isTheSame is False:
                    return False
                if isTheSame is True:
                    return True
        return False

    def checkBothListsAreEqualOfLength(self, list1, list2):
        if (len(list1) is len(list2)):
            return True
        return False

    def checkTheCorrectNumOfListinList(self, checkingListForListTypes):
        num_of_list = 0
        inner_each_list = list()
        for eachList in checkingListForListTypes:
            checkType = type(eachList)
            if checkType is list:
                num_of_list += 1
                inner_each_list.append(eachList)
        return num_of_list, inner_each_list

    def checkInnerEachElementInList(self, innerList1, innerList2):
        eachList_list1 = list()
        eachList_list2 = list()

        for eachList1 in innerList1:
            eachList_list1.append(type(eachList1))

        for eachList2 in innerList2:
            eachList_list2.append(type(eachList2))

        for eachList in range(0, len(eachList_list1)):
            if eachList_list1[eachList] != eachList_list2[eachList]:
                return False
        return True

    # def checkInnerEachElementInList(self, innerList1, innerList2):
    #     print(innerList1)
    #     print()
    #     print(innerList2)
    #     eachList_list1 = list()
    #     eachList_list2 = list()
    #
    #     for eachList1 in innerList1:
    #         eachList_list1.append(type(eachList1))
    #
    #     for eachList2 in innerList2:
    #         eachList_list2.append(type(eachList2))
    #     for eachList in range(0, len(eachList_list1)):
    #         print('1 ',eachList_list1[eachList],' - ', eachList_list2[eachList])
    #         if eachList_list1[eachList] is eachList_list2[eachList]:
    #             for innerEachGames in range(0, len(innerList1)):
    #                 if innerList1[innerEachGames] != str and innerList2[innerEachGames] != str:
    #                     print('1 whagwan')
    #                     return False;
    #         else:
    #             print('2 whagwan')
    #             return False
    #     return True
