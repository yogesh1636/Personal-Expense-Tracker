import json
import os
from datetime import datetime, timedelta
from pathlib import Path


class ExpenseTracker:
    """A comprehensive expense tracker with JSON storage, date tracking, and filtering."""
    
    def __init__(self, filename="expenses.json"):
        """Initialize the expense tracker with JSON file storage."""
        self.filename = filename
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading expenses: {e}")
                return []
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.expenses, f, indent=2)
            print("✅ Expense saved successfully!\n")
        except IOError as e:
            print(f"❌ Error saving expense: {e}\n")
    
    def add_expense(self):
        """Add a new expense with amount, category, and description."""
        try:
            amount = float(input("Enter expense amount (₹): "))
            if amount <= 0:
                print("❌ Amount must be positive!\n")
                return
            
            print("\n📂 Categories: Food, Travel, Entertainment, Utilities, Shopping, Healthcare, Other")
            category = input("Enter category: ").strip()
            
            if not category:
                category = "Other"
            
            description = input("Enter description (optional): ").strip()
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            
            if not date:
                date = datetime.now().strftime("%Y-%m-%d")
            else:
                # Validate date format
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    print("❌ Invalid date format! Using today's date.\n")
                    date = datetime.now().strftime("%Y-%m-%d")
            
            expense = {
                "amount": amount,
                "category": category,
                "description": description,
                "date": date,
                "timestamp": datetime.now().isoformat()
            }
            
            self.expenses.append(expense)
            self.save_expenses()
            
        except ValueError:
            print("❌ Please enter a valid amount!\n")
    
    def view_expenses(self):
        """Display all expenses in a formatted table."""
        if not self.expenses:
            print("📭 No expenses found!\n")
            return
        
        print("\n" + "="*80)
        print(f"{'Date':<12} {'Category':<15} {'Amount':<12} {'Description':<30}")
        print("="*80)
        
        for expense in self.expenses:
            date = expense.get("date", "N/A")
            category = expense.get("category", "N/A")[:14]
            amount = f"₹{expense['amount']:.2f}"
            description = expense.get("description", "")[:29]
            print(f"{date:<12} {category:<15} {amount:<12} {description:<30}")
        
        print("="*80 + "\n")
    
    def view_by_category(self):
        """View expenses filtered by category."""
        if not self.expenses:
            print("📭 No expenses found!\n")
            return
        
        categories = set(exp.get("category", "Other") for exp in self.expenses)
        print("\n📂 Available Categories:")
        for i, cat in enumerate(sorted(categories), 1):
            print(f"   {i}. {cat}")
        
        category_input = input("\nEnter category name: ").strip()
        
        filtered = [exp for exp in self.expenses if exp.get("category", "").lower() == category_input.lower()]
        
        if not filtered:
            print(f"❌ No expenses found in '{category_input}' category!\n")
            return
        
        print(f"\n📊 Expenses in '{category_input}' category:")
        print("="*80)
        print(f"{'Date':<12} {'Amount':<12} {'Description':<40}")
        print("="*80)
        
        total = 0
        for exp in filtered:
            date = exp.get("date", "N/A")
            amount = f"₹{exp['amount']:.2f}"
            description = exp.get("description", "")[:39]
            print(f"{date:<12} {amount:<12} {description:<40}")
            total += exp['amount']
        
        print("="*80)
        print(f"{'Category Total:':<12} {f'₹{total:.2f}':<12}\n")
    
    def view_by_date_range(self):
        """View expenses within a date range."""
        if not self.expenses:
            print("📭 No expenses found!\n")
            return
        
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format!\n")
            return
        
        filtered = [exp for exp in self.expenses 
                   if start <= datetime.strptime(exp.get("date", "1970-01-01"), "%Y-%m-%d") <= end]
        
        if not filtered:
            print(f"❌ No expenses found between {start_date} and {end_date}!\n")
            return
        
        print(f"\n📊 Expenses from {start_date} to {end_date}:")
        print("="*80)
        print(f"{'Date':<12} {'Category':<15} {'Amount':<12} {'Description':<30}")
        print("="*80)
        
        total = 0
        for exp in sorted(filtered, key=lambda x: x.get("date", "")):
            date = exp.get("date", "N/A")
            category = exp.get("category", "N/A")[:14]
            amount = f"₹{exp['amount']:.2f}"
            description = exp.get("description", "")[:29]
            print(f"{date:<12} {category:<15} {amount:<12} {description:<29}")
            total += exp['amount']
        
        print("="*80)
        print(f"{'Period Total:':<12} {f'₹{total:.2f}':<12}\n")
    
    def total_expenses(self):
        """Display total expenses with breakdown by category."""
        if not self.expenses:
            print("📭 No expenses found!\n")
            return
        
        total = sum(exp['amount'] for exp in self.expenses)
        
        # Category breakdown
        categories = {}
        for exp in self.expenses:
            cat = exp.get("category", "Other")
            categories[cat] = categories.get(cat, 0) + exp['amount']
        
        print("\n" + "="*50)
        print(f"{'EXPENSE SUMMARY':<50}")
        print("="*50)
        print(f"Total Expenses: ₹{total:.2f}\n")
        
        print("Breakdown by Category:")
        for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total) * 100
            print(f"  • {cat:<20} ₹{amount:>8.2f} ({percentage:>5.1f}%)")
        
        print("="*50 + "\n")
    
    def summary_today(self):
        """Show expense summary for today."""
        today = datetime.now().strftime("%Y-%m-%d")
        today_expenses = [exp for exp in self.expenses if exp.get("date") == today]
        
        if not today_expenses:
            print(f"📭 No expenses for today ({today})!\n")
            return
        
        total = sum(exp['amount'] for exp in today_expenses)
        print(f"\n📅 Today's Expenses ({today}):")
        print(f"Total: ₹{total:.2f}")
        print(f"Number of transactions: {len(today_expenses)}\n")
    
    def summary_week(self):
        """Show expense summary for this week."""
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        week_start_str = week_start.strftime("%Y-%m-%d")
        
        week_expenses = [exp for exp in self.expenses 
                        if exp.get("date") >= week_start_str]
        
        if not week_expenses:
            print(f"📭 No expenses this week!\n")
            return
        
        total = sum(exp['amount'] for exp in week_expenses)
        print(f"\n📅 This Week's Expenses (from {week_start_str}):")
        print(f"Total: ₹{total:.2f}")
        print(f"Number of transactions: {len(week_expenses)}\n")
    
    def summary_month(self):
        """Show expense summary for this month."""
        today = datetime.now()
        month_start = today.replace(day=1).strftime("%Y-%m-%d")
        
        month_expenses = [exp for exp in self.expenses 
                         if exp.get("date") >= month_start]
        
        if not month_expenses:
            print(f"📭 No expenses this month!\n")
            return
        
        total = sum(exp['amount'] for exp in month_expenses)
        print(f"\n📅 This Month's Expenses (from {month_start}):")
        print(f"Total: ₹{total:.2f}")
        print(f"Number of transactions: {len(month_expenses)}\n")
    
    def delete_expense(self):
        """Delete an expense by index."""
        self.view_expenses()
        
        if not self.expenses:
            return
        
        try:
            index = int(input("Enter expense number to delete (starting from 1): ")) - 1
            if 0 <= index < len(self.expenses):
                deleted = self.expenses.pop(index)
                self.save_expenses()
                print(f"✅ Deleted: ₹{deleted['amount']} - {deleted['category']}\n")
            else:
                print("❌ Invalid expense number!\n")
        except ValueError:
            print("❌ Please enter a valid number!\n")
    
    def menu(self):
        """Display main menu and handle user choices."""
        while True:
            print("\n" + "="*50)
            print("💰 PERSONAL EXPENSE TRACKER")
            print("="*50)
            print("1.  ➕ Add Expense")
            print("2.  📋 View All Expenses")
            print("3.  🔍 Filter by Category")
            print("4.  📅 View by Date Range")
            print("5.  💹 Total & Summary")
            print("6.  📊 Today's Summary")
            print("7.  📊 Week's Summary")
            print("8.  📊 Month's Summary")
            print("9.  🗑️  Delete Expense")
            print("10. 🚪 Exit")
            print("="*50)
            
            choice = input("Choose an option (1-10): ").strip()
            
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.view_by_category()
            elif choice == "4":
                self.view_by_date_range()
            elif choice == "5":
                self.total_expenses()
            elif choice == "6":
                self.summary_today()
            elif choice == "7":
                self.summary_week()
            elif choice == "8":
                self.summary_month()
            elif choice == "9":
                self.delete_expense()
            elif choice == "10":
                print("\n👋 Thank you for using Expense Tracker. Goodbye!\n")
                break
            else:
                print("❌ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
