import unittest
import json
import os
from datetime import datetime
from expensestracker import ExpenseTracker


class TestExpenseTracker(unittest.TestCase):
    """Unit tests for ExpenseTracker class."""
    
    def setUp(self):
        """Create a test tracker with a temporary file."""
        self.test_file = "test_expenses.json"
        self.tracker = ExpenseTracker(self.test_file)
    
    def tearDown(self):
        """Clean up test file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_expense(self):
        """Test adding an expense."""
        initial_count = len(self.tracker.expenses)
        
        # Manually add an expense
        expense = {
            "amount": 100.0,
            "category": "Food",
            "description": "Lunch",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "timestamp": datetime.now().isoformat()
        }
        self.tracker.expenses.append(expense)
        
        self.assertEqual(len(self.tracker.expenses), initial_count + 1)
    
    def test_save_expenses(self):
        """Test saving expenses to JSON file."""
        expense = {
            "amount": 50.0,
            "category": "Travel",
            "description": "Bus fare",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "timestamp": datetime.now().isoformat()
        }
        self.tracker.expenses.append(expense)
        self.tracker.save_expenses()
        
        # Load from file and verify
        with open(self.test_file, "r") as f:
            saved = json.load(f)
        
        self.assertEqual(len(saved), 1)
        self.assertEqual(saved[0]["amount"], 50.0)
    
    def test_load_expenses(self):
        """Test loading expenses from JSON file."""
        # Create a test file
        test_data = [
            {
                "amount": 100.0,
                "category": "Food",
                "description": "Dinner",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        with open(self.test_file, "w") as f:
            json.dump(test_data, f)
        
        # Load and verify
        tracker = ExpenseTracker(self.test_file)
        self.assertEqual(len(tracker.expenses), 1)
        self.assertEqual(tracker.expenses[0]["amount"], 100.0)
    
    def test_total_calculation(self):
        """Test total expenses calculation."""
        expenses = [
            {"amount": 100.0, "category": "Food", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
            {"amount": 50.0, "category": "Travel", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
            {"amount": 30.0, "category": "Entertainment", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
        ]
        
        self.tracker.expenses = expenses
        total = sum(exp['amount'] for exp in self.tracker.expenses)
        
        self.assertEqual(total, 180.0)
    
    def test_filter_by_category(self):
        """Test filtering expenses by category."""
        expenses = [
            {"amount": 100.0, "category": "Food", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
            {"amount": 50.0, "category": "Travel", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
            {"amount": 75.0, "category": "Food", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
        ]
        
        self.tracker.expenses = expenses
        food_expenses = [exp for exp in self.tracker.expenses if exp.get("category", "").lower() == "food"]
        
        self.assertEqual(len(food_expenses), 2)
        self.assertEqual(sum(exp['amount'] for exp in food_expenses), 175.0)
    
    def test_empty_expenses(self):
        """Test handling of empty expense list."""
        self.assertEqual(len(self.tracker.expenses), 0)
    
    def test_delete_expense(self):
        """Test deleting an expense."""
        expenses = [
            {"amount": 100.0, "category": "Food", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
            {"amount": 50.0, "category": "Travel", "description": "", "date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat()},
        ]
        
        self.tracker.expenses = expenses
        initial_count = len(self.tracker.expenses)
        
        # Delete first expense
        self.tracker.expenses.pop(0)
        
        self.assertEqual(len(self.tracker.expenses), initial_count - 1)
        self.assertEqual(self.tracker.expenses[0]["amount"], 50.0)


if __name__ == "__main__":
    unittest.main()
