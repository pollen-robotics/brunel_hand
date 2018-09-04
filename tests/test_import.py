import unittest


class TestImport(unittest.TestCase):
    def test_import_general(self):
        import brunel_hand

    def test_import_hand(self):
        from brunel_hand import BrunelHand


if __name__ == '__main__':
    unittest.main()
