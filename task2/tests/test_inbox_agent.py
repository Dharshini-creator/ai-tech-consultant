
import unittest

from src.inbox_agent import analyze_email


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


if __name__ == "__main__":
    unittest.main()
