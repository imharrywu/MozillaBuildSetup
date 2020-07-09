import imp
import sys

import unittest

# Note:
#   In Python 3.x, this test case is in Lib/test/test_importlib/test_util.py

class MagicNumberTests(unittest.TestCase):
    """
    Test release compatibility issues relating to precompiled bytecode
    """
    @unittest.skipUnless(
        sys.version_info.releaselevel in ('candidate', 'final'),
        'only applies to candidate or final python release levels'
    )
    def test_magic_number(self):
        """
        Each python minor release should generally have a MAGIC_NUMBER
        that does not change once the release reaches candidate status.

        Once a release reaches candidate status, the value of the constant
        EXPECTED_MAGIC_NUMBER in this test should be changed.
        This test will then check that the actual MAGIC_NUMBER matches
        the expected value for the release.

        In exceptional cases, it may be required to change the MAGIC_NUMBER
        for a maintenance release. In this case the change should be
        discussed in python-dev. If a change is required, community
        stakeholders such as OS package maintainers must be notified
        in advance. Such exceptional releases will then require an
        adjustment to this test case.
        """
        EXPECTED_MAGIC_NUMBER = 62211
        raw_magic = imp.get_magic()
        actual = (ord(raw_magic[1]) << 8) + ord(raw_magic[0])

        msg = (
            "To avoid breaking backwards compatibility with cached bytecode "
            "files that can't be automatically regenerated by the current "
            "user, candidate and final releases require the current  "
            "importlib.util.MAGIC_NUMBER to match the expected "
            "magic number in this test. Set the expected "
            "magic number in this test to the current MAGIC_NUMBER to "
            "continue with the release.\n\n"
            "Changing the MAGIC_NUMBER for a maintenance release "
            "requires discussion in python-dev and notification of "
            "community stakeholders."
        )
        self.assertEqual(EXPECTED_MAGIC_NUMBER, actual)#, msg)


def test_main():
    from test.support import run_unittest
    run_unittest(MagicNumberTests)

if __name__ == '__main__':
    test_main()
