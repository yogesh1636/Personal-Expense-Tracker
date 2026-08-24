# Personal Expense Tracker

A comprehensive, beginner-friendly Python CLI application for tracking daily expenses, categorizing spending, and generating financial summaries.

## 🎯 Features

### Core Features
- ✅ **Add Expenses** - Log expenses with amount, category, and description
- ✅ **View All Expenses** - Display all expenses in a formatted table
- ✅ **Filter by Category** - View expenses for specific categories
- ✅ **Filter by Date Range** - Search expenses between two dates
- ✅ **Total & Summary** - See total spending with category breakdown
- ✅ **Daily Summary** - View today's expenses
- ✅ **Weekly Summary** - View this week's expenses
- ✅ **Monthly Summary** - View this month's expenses
- ✅ **Delete Expense** - Remove incorrect entries
- ✅ **Persistent Storage** - All data saved to `expenses.json`

### Advanced Features
- 📊 **Category Breakdown** - Visualize spending by category with percentages
- 📅 **Date Tracking** - Track expenses with specific dates
- 💾 **Export to CSV** - Export data for spreadsheet analysis
- 💾 **Export to JSON** - Export raw data for programmatic use
- 📄 **Generate Reports** - Create summary reports in text format
- ✔️ **Input Validation** - Ensure data integrity with validation checks

## 🛠️ Technical Concepts

This project teaches:
- **File Handling** - JSON file operations (`open`, `read`, `write`)
- **Object-Oriented Programming** - Class-based architecture
- **Data Structures** - Lists and dictionaries for data organization
- **Date/Time Handling** - Python's `datetime` module
- **Input Validation** - Error handling and user input verification
- **Module Organization** - Separating concerns into different modules
- **Unit Testing** - Writing and running tests with `unittest`
- **CSV/JSON Handling** - Data export in multiple formats

## 📋 Requirements

- Python 3.7 or higher
- No external dependencies (uses Python standard library only)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yogesh1636/Personal-Expense-Tracker.git
cd Personal-Expense-Tracker
```

### 2. Run the Application
```bash
python expensestracker.py
```

### 3. Follow the Menu
```
💰 PERSONAL EXPENSE TRACKER
==================================================
1.  ➕ Add Expense
2.  📋 View All Expenses
3.  🔍 Filter by Category
4.  📅 View by Date Range
5.  💹 Total & Summary
6.  📊 Today's Summary
7.  📊 Week's Summary
8.  📊 Month's Summary
9.  🗑️  Delete Expense
10. 🚪 Exit
==================================================
```

## 📖 Usage Examples

### Adding an Expense
```
Choose an option (1-10): 1

Enter expense amount (₹): 500
📂 Categories: Food, Travel, Entertainment, Utilities, Shopping, Healthcare, Other
Enter category: Food
Enter description (optional): Lunch at cafe
Enter date (YYYY-MM-DD) or press Enter for today: 

✅ Expense saved successfully!
```

### Viewing All Expenses
```
Choose an option (1-10): 2

================================================================================
Date         Category        Amount       Description
================================================================================
2026-08-24   Food            ₹500.00      Lunch at cafe
2026-08-24   Travel          ₹200.00      Taxi fare
2026-08-23   Entertainment   ₹150.00      Movie tickets
================================================================================
```

### Filtering by Category
```
Choose an option (1-10): 3

📂 Available Categories:
   1. Entertainment
   2. Food
   3. Travel

Enter category name: Food

📊 Expenses in 'Food' category:
================================================================================
Date         Amount       Description
================================================================================
2026-08-24   ₹500.00      Lunch at cafe
================================================================================
Category Total:  ₹500.00
```

### Viewing Summary
```
Choose an option (1-10): 5

==================================================
EXPENSE SUMMARY
==================================================
Total Expenses: ₹850.00

Breakdown by Category:
  • Food                 ₹500.00 (58.8%)
  • Travel               ₹200.00 (23.5%)
  • Entertainment        ₹150.00 (17.6%)
==================================================
```

## 🧪 Running Tests

```bash
python -m unittest test_expensestracker.py
```

Or with verbose output:
```bash
python -m unittest test_expensestracker.py -v
```

## 📤 Exporting Data

The `export_manager.py` module provides export functionality:

```python
from expensestracker import ExpenseTracker
from export_manager import ExportManager

tracker = ExpenseTracker()
exporter = ExportManager(tracker.expenses)

# Export to CSV
exporter.export_to_csv("my_expenses.csv")

# Export to JSON
exporter.export_to_json("my_expenses.json")

# Export summary report
exporter.export_summary_report("expense_report.txt")
```

## 📁 Project Structure

```
Personal-Expense-Tracker/
├── expensestracker.py       # Main application with ExpenseTracker class
├── export_manager.py        # Export functionality (CSV, JSON, TXT)
├── test_expensestracker.py  # Unit tests
├── expenses.json            # Data storage (auto-created)
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── LICENSE                 # MIT License
```

## 🔄 Data Storage

Expenses are stored in `expenses.json` with the following structure:

```json
[
  {
    "amount": 500.0,
    "category": "Food",
    "description": "Lunch at cafe",
    "date": "2026-08-24",
    "timestamp": "2026-08-24T12:30:45.123456"
  }
]
```

## 🎓 Learning Outcomes

By exploring this project, you'll learn:
- How to structure Python applications with classes
- File I/O operations and JSON handling
- Date and time manipulation
- Input validation and error handling
- Writing unit tests
- Organizing code into modules
- Data export and formatting

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Write/update tests
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/improvement`)
7. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ��� Support

If you have any questions or issues, please:
1. Check the existing GitHub issues
2. Create a new issue with a clear description
3. Include example usage and error messages if applicable

## 🔗 Links

- Repository: [GitHub](https://github.com/yogesh1636/Personal-Expense-Tracker)
- Author: [yogesh1636](https://github.com/yogesh1636)

---

Happy Expense Tracking! 💰📊
