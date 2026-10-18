
import unittest

from agents.scope_agent import create_scope


class TestScopeAgent(unittest.TestCase):

    def test_extracts_requirements(self):
        notes = "The system must support mobile devices."

        result = create_scope(notes)

        self.assertEqual(
            result["requirements"],
            ["The system must support mobile devices."]
        )

    def test_extracts_deliverables(self):
        notes = "Build a customer dashboard."

        result = create_scope(notes)

        self.assertEqual(
            result["deliverables"],
            ["Build a customer dashboard."]
        )

    def test_extracts_open_questions(self):
        notes = "Confirm which users can access reports?"

        result = create_scope(notes)

        self.assertEqual(
            result["open_questions"],
            ["Confirm which users can access reports?"]
        )


if __name__ == "__main__":
    unittest.main()
