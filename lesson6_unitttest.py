import unittest

class MyDict(dict):
    pass

class TestMyDict(unittest.TestCase):
    def setUp(self):
        print('this is setup')
    def tearDown(self):
        print('this is tear down')
    def test_init(self):
        md = MyDict(one = 1, two = 2)
        self.assertEqual(md['one'], 1)

if __name__ == '__main__':
    unittest.main()
