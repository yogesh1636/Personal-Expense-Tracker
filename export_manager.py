"""
Export functionality for Personal Expense Tracker.
Supports exporting expenses to CSV format.
"""

import csv
import json
from datetime import datetime


class ExportManager:
    """Manages exporting expense data to various formats."""
    
    def __init__(self, expenses):
        """Initialize with expense data."""
        self.expenses = expenses
    
    def export_to_csv(self, filename="expenses_export.csv"):
        """Export expenses to CSV file."""
        if not self.expenses:
            print("❌ No expenses to export!\n")
            return False
        
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['Date', 'Category', 'Amount', 'Description']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for expense in self.expenses:
                    writer.writerow({
                        'Date': expense.get('date', 'N/A'),
                        'Category': expense.get('category', 'N/A'),
                        'Amount': f"₹{expense['amount']:.2f}",
                        'Description': expense.get('description', '')
                    })
            
            print(f"✅ Expenses exported successfully to {filename}!\n")
            return True
        except IOError as e:
            print(f"❌ Error exporting to CSV: {e}\n")
            return False
    
    def export_to_json(self, filename="expenses_export.json"):
        """Export expenses to JSON file."""
        if not self.expenses:
            print("❌ No expenses to export!\n")
            return False
        
        try:
            with open(filename, 'w') as jsonfile:
                json.dump(self.expenses, jsonfile, indent=2)
            
            print(f"✅ Expenses exported successfully to {filename}!\n")
            return True
        except IOError as e:
            print(f"❌ Error exporting to JSON: {e}\n")
            return False
    
    def export_summary_report(self, filename="expense_report.txt"):
        """Export a summary report of expenses."""
        if not self.expenses:
            print("❌ No expenses to export!\n")
            return False
        
        try:
            total = sum(exp['amount'] for exp in self.expenses)
            categories = {}
            
            for exp in self.expenses:
                cat = exp.get('category', 'Other')
                categories[cat] = categories.get(cat, 0) + exp['amount']
            
            with open(filename, 'w') as f:
                f.write("="*60 + "\n")
                f.write("EXPENSE TRACKER SUMMARY REPORT\n")
                f.write("="*60 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Expenses: ₹{total:.2f}\n")
                f.write(f"Number of Transactions: {len(self.expenses)}\n")
                f.write("\nBreakdown by Category:\n")
                f.write("-"*60 + "\n")
                
                for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
                    percentage = (amount / total) * 100
                    f.write(f"{cat:<20} ₹{amount:>10.2f} ({percentage:>5.1f}%)\n")
                
                f.write("="*60 + "\n")
            
            print(f"✅ Summary report exported successfully to {filename}!\n")
            return True
        except IOError as e:
            print(f"❌ Error exporting summary: {e}\n")
            return False
