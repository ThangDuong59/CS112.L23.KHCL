import unittest
import numpy as np
import maxLenString as mLS
class unitTesting(unittest.TestCase):

    # have 20 test cases, dir test case
    dirtest = "materials/"
    arr = np.load(dirtest + 'inputArr.npy', allow_pickle=True)
    x = np.load(dirtest + 'inputX.npy', allow_pickle= True)
    expect = np.load(dirtest + 'outputAnswer.npy', allow_pickle= True)

    # show test case ith
    def showTestcase(self, testcase_ith):
        print('Given array: {}'.format(self.arr[testcase_ith]))
        print('Value x: {}'.format(self.x[testcase_ith][0]))
        print('True result: {}'.format(self.expect[testcase_ith]))

    # testing case ith
    def checkCase(self, testcase_ith):
        arr_ith = self.arr[testcase_ith]
        x_ith = self.x[testcase_ith]
        expect_ith = self.expect[testcase_ith]
        # them ham so can kiem tra o day de test 20 cases
        actual_ith =  mLS.main(arr_ith, x_ith)#self.expect[testcase_ith]# function - arr -x
        self.assertEqual(expect_ith, actual_ith)

    def test0(self):
        self.checkCase(0)
    def test1(self):
        self.checkCase(1)
    def test2(self):
        self.checkCase(2)
    def test3(self):
        self.checkCase(3)
    def test4(self):
        self.checkCase(4)
    def test5(self):
        self.checkCase(5)
    def test6(self):
        self.checkCase(6)
    def test7(self):
        self.checkCase(7)
    def test8(self):
        self.checkCase(8)
    def test9(self):
        self.checkCase(9)
    def test10(self):
        self.checkCase(10)
    def test11(self):
        self.checkCase(11)
    def test12(self):
        self.checkCase(12)
    def test13(self):
        self.checkCase(13)
    def test14(self):
        self.checkCase(14)
    def test15(self):
        self.checkCase(15)
    def test16(self):
        self.checkCase(16)
    def test17(self):
        self.checkCase(17)
    def test18(self):
        self.checkCase(18)
    def test19(self):
        self.checkCase(19)


unittest.main()