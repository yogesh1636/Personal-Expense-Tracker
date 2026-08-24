# Configuration file for Personal Expense Tracker

# Default data file location
DATA_FILE = "expenses.json"

# Supported expense categories
CATEGORIES = [
    "Food",
    "Travel",
    "Entertainment",
    "Utilities",
    "Shopping",
    "Healthcare",
    "Education",
    "Other"
]

# Date format
DATE_FORMAT = "%Y-%m-%d"

# Currency symbol
CURRENCY_SYMBOL = "₹"

# Enable/disable features
FEATURES = {
    "export_csv": True,
    "export_json": True,
    "generate_reports": True,
    "delete_expenses": True,
    "category_breakdown": True,
    "date_filtering": True
}

# UI Settings
UI = {
    "show_emojis": True,
    "table_width": 80,
    "date_display_format": "%d %B %Y"  # 24 August 2026
}
