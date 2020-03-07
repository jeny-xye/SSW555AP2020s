import unittest
from unittest.mock import patch
from gedcom_app.control.US0203 import birth_b_marriage_us02, birth_b_death_us03
from gedcom_app.control.parser import parse_gedcom
from gedcom_app.control.build_entity import build_family, build_individual


class Test(unittest.TestCase):

    def test_US03(self):
        path = "C:\\project05\\test.ged"
        m,n = parse_gedcom(path)

        with patch('builtins.print') as mocked_print:
            birth_b_death_us03(build_individual(m))
            mocked_print.assert_called_with(
                "Error: INDIVITUAL: US03 birth before death：line 5 and 9: I01: 5 JUL 1950 isn't before 31 DEC 1949")


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

