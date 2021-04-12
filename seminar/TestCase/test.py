import unittest
import numpy as np

class unitTesting(unittest.TestCase):

    # have 20 test cases, dir test case
    dirtest = '/home/vantai/Desktop/Code/cs112/'
    arr = np.load(dirtest + 'ARR.npy', allow_pickle=True)
    x = np.load(dirtest + 'X.npy', allow_pickle= True)
    expect = np.load(dirtest + 'RESULT.npy', allow_pickle= True)

    # show test case ith
    def showTestcase(self, testcase_ith):
        print('Given array: {}'.format(self.arr[testcase_ith]))
        print('Value x: {}'.format(self.x[testcase_ith][0]))
        print('True result: {}'.format(self.expect[testcase_ith]))

    # testing case ith
    def _testCase(self, testcase_ith):
        arr_ith = self.arr[testcase_ith]
        x_ith = self.x[testcase_ith]
        expect_ith = self.expect[testcase_ith]
        # them ham so can kiem tra o day de test 20 cases
        actual_ith =  self.expect[testcase_ith]# function - arr -x
        self.assertEqual(expect_ith, actual_ith)

    def test0(self):
        self._testCase(0)
    def test1(self):
        self._testCase(1)
    def test2(self):
        self._testCase(2)
    def test3(self):
        self._testCase(3)
    def test4(self):
        self._testCase(4)
    def test5(self):
        self._testCase(5)
    def test6(self):
        self._testCase(6)
    def test7(self):
        self._testCase(7)
    def test8(self):
        self._testCase(8)
    def test9(self):
        self._testCase(9)
    def test10(self):
        self._testCase(10)
    def test11(self):
        self._testCase(11)
    def test12(self):
        self._testCase(12)
    def test13(self):
        self._testCase(13)
    def test14(self):
        self._testCase(14)
    def test15(self):
        self._testCase(15)
    def test16(self):
        self._testCase(16)
    def test17(self):
        self._testCase(17)
    def test18(self):
        self._testCase(18)
    def test19(self):
        self._testCase(19)


unittest.main()