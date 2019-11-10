import unittest

import nuclear

class NukeTests(unittest.TestCase):
    def setUp(self):
        self.nuke = nuclear.Nuclear(["Firefox"], 0)

    def test_get_pids_list(self):
        pids = self.nuke.get_pids("dns")
        assert type(pids) is list

    def test_get_pids_int(self):
        pids = self.nuke.get_pids("dns")
        assert type(pids[0]) is int

if __name__ == '__main__':
    unittest.main()
