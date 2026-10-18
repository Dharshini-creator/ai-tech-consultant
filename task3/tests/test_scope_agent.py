
import unittest



from agents.scope_agent import (
    create_scope,
    approve_scope,
    request_scope_changes,
    reject_scope,
)
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


    def test_approve_scope(self):
        scope = {"project_name": "Customer Dashboard"}

        approve_scope(scope)

        self.assertEqual(scope["review_status"], "approved")
        self.assertTrue(scope["approved"])

    def test_request_scope_changes(self):
        scope = {"project_name": "Customer Dashboard"}

        request_scope_changes(scope, "Add a login feature.")

        self.assertEqual(scope["review_status"], "changes_requested")
        self.assertFalse(scope["approved"])
        self.assertEqual(
            scope["review_feedback"],
            "Add a login feature."
        )

    def test_reject_scope(self):
        scope = {"project_name": "Customer Dashboard"}

        reject_scope(scope, "The scope is incomplete.")

        self.assertEqual(scope["review_status"], "rejected")
        self.assertFalse(scope["approved"])
        self.assertEqual(
            scope["review_feedback"],
            "The scope is incomplete."
        )

    
    def test_extracts_multiple_requirements(self):
        notes = (
            "The app must support mobile devices.\n"
            "The system should load quickly."
        )
        result = create_scope(notes)
        self.assertEqual(len(result["requirements"]), 2)

    def test_extracts_multiple_deliverables(self):
        notes = (
            "Build a customer dashboard.\n"
            "Create a weekly report."
        )
        result = create_scope(notes)
        self.assertEqual(len(result["deliverables"]), 2)

    def test_question_word_is_detected(self):
        notes = "The launch date is still unknown."
        result = create_scope(notes)
        self.assertEqual(
            result["open_questions"],
            ["The launch date is still unknown."]
        )

    def test_scope_starts_with_extracted_lists(self):
        notes = "Build a reporting dashboard."
        result = create_scope(notes)
        self.assertIn("requirements", result)
        self.assertIn("deliverables", result)
        self.assertIn("open_questions", result)
        self.assertIn("all_notes", result)

if __name__ == "__main__":
    unittest.main()
