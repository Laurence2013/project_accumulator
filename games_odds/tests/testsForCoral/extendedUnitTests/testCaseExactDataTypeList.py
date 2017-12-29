class TestCaseExactDataTypeList:
    def assertDataTypeOfListIsEqual(self, list1, list2):
        isLenSame = self.checkBothListsAreEqualOfLength(list1, list2)
        if isLenSame is True:
            self.checkEachElementInList(list2)
        return False

    def checkBothListsAreEqualOfLength(self, list1, list2):
        if (len(list1) is len(list2)):
            return True
        return False

    def checkEachElementInList(self, list2):
        print()
        test = type(list2[0])
        print(dir(test))
        print()
        print(test)
        if test is list:
            print('hello')
