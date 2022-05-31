import unittest


def print_hi(name):
    print(f'Hello, world, {name}')


if __name__ == '__main__':
    print_hi('john')


class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        self.assertTrue(True)