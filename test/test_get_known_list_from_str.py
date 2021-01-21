import unittest

from src.get_known_list_from_str import get_known_list_from_str


class TestGetKnownListFromStr(unittest.TestCase):
    def test_user_input_rejected_containing_mistake(self):
        self.assertEqual(
            None,
            get_known_list_from_str("feaver cough", ["fever", "cough"]),
        )

    def test_user_input_rejected_for_one_symptom(self):
        self.assertEqual(
            None,
            get_known_list_from_str("itching", ["fever", "cough"]),
        )

    def test_user_input_rejected_for_no_symptom(self):
        self.assertEqual(
            None,
            get_known_list_from_str("", ["fever", "cough"]),
        )

    def test_user_input_accepted(self):
        self.assertEqual(
            ["fever", "cough"],
            get_known_list_from_str("fever cough", ["fever", "cough"]),
        )

    def test_user_input_accepted_for_one_symptom(self):
        self.assertEqual(
            ["fever"],
            get_known_list_from_str("fever", ["fever", "cough"]),
        )


if __name__ == "__main__":
    unittest.main()
