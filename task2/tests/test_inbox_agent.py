
import unittest

from src.inbox_agent import (
    analyze_email,
    approve_reply,
    edit_reply,
    reject_reply,
)


class TestInboxAgent(unittest.TestCase):

    def test_urgent_email(self):
        email = {
            "sender": "user@example.com",
            "subject": "Urgent meeting",
            "body": "Please schedule this immediately.",
        }

        result = analyze_email(email)

        self.assertEqual(result["priority"], "high")
        self.assertEqual(result["category"], "meeting")

    def test_billing_email(self):
        email = {
            "sender": "user@example.com",
            "subject": "Invoice question",
            "body": "I need help with my payment.",
        }

        result = analyze_email(email)

        self.assertEqual(result["category"], "billing")

    def test_general_email(self):
        email = {
            "sender": "user@example.com",
            "subject": "Hello",
            "body": "Just saying hello.",
        }

        result = analyze_email(email)

        self.assertEqual(result["priority"], "normal")
        self.assertEqual(result["category"], "general")
        self.assertTrue(result["suggested_reply"])


    def test_approve_reply(self):
        result = {"suggested_reply": "Thank you for contacting us."}

        approve_reply(result)

        self.assertEqual(result["review_status"], "approved")
        self.assertTrue(result["approved"])

    def test_edit_reply(self):
        result = {"suggested_reply": "Old reply"}

        edit_reply(result, "Updated reply")

        self.assertEqual(result["suggested_reply"], "Updated reply")
        self.assertEqual(result["review_status"], "pending")
        self.assertFalse(result["approved"])

    def test_reject_reply(self):
        result = {"suggested_reply": "Unwanted reply"}

        reject_reply(result)

        self.assertEqual(result["review_status"], "rejected")
        self.assertFalse(result["approved"])

    
    def test_refund_email_is_billing(self):
        email = {
            "sender": "customer@example.com",
            "subject": "Refund request",
            "body": "I would like a refund for my last payment.",
        }
        result = analyze_email(email)
        self.assertEqual(result["category"], "billing")

    def test_deadline_email_is_high_priority(self):
        email = {
            "sender": "customer@example.com",
            "subject": "Project deadline",
            "body": "We need an answer before the deadline.",
        }
        result = analyze_email(email)
        self.assertEqual(result["priority"], "high")

    def test_support_error_email(self):
        email = {
            "sender": "customer@example.com",
            "subject": "Website error",
            "body": "I get an error when opening the page.",
        }
        result = analyze_email(email)
        self.assertEqual(result["category"], "support")

    def test_new_draft_starts_pending(self):
        email = {
            "sender": "customer@example.com",
            "subject": "Product information",
            "body": "Please send me more information.",
        }
        result = analyze_email(email)
        self.assertEqual(result["review_status"], "pending")
        self.assertFalse(result["approved"])

if __name__ == "__main__":
    unittest.main()
