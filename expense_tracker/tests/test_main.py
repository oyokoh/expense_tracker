
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

import main


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        main.expenses.clear()

    @patch("builtins.input", side_effect=["Transport", "500"])
    def test_add_valid_expense(self, mock_input):
        main.add_expense()

        self.assertEqual(len(main.expenses), 1)
        self.assertEqual(main.expenses[0]["description"], "Transport")
        self.assertEqual(main.expenses[0]["amount"], 500)

    @patch("builtins.input", side_effect=["", "500"])
    def test_reject_blank_description(self, mock_input):
        main.add_expense()

        self.assertEqual(len(main.expenses), 0)

    @patch("builtins.input", side_effect=["Transport", "abc"])
    def test_reject_invalid_amount(self, mock_input):
        main.add_expense()

        self.assertEqual(len(main.expenses), 0)

    def test_view_empty_expenses(self):
        output = StringIO()

        with redirect_stdout(output):
            main.view_expenses()

        self.assertIn(
            "No expenses recorded yet.",
            output.getvalue()
        )

    def test_total_of_expenses(self):
        main.expenses.extend([
            {"description": "Transport", "amount": 500},
            {"description": "Lunch", "amount": 1250.50},
        ])

        output = StringIO()

        with redirect_stdout(output):
            main.show_total()

        self.assertIn("1750.50", output.getvalue())


if __name__ == "__main__":
    unittest.main()
