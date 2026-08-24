# Changelog

All notable changes to the Personal Expense Tracker project will be documented in this file.

## [2.0.0] - 2026-08-24

### Added
- **Class-based Architecture**: Refactored entire codebase using OOP principles
- **JSON Storage**: Migrated from plain text to JSON for better data integrity
- **Date Tracking**: Every expense now includes a date field
- **Advanced Filtering**: Filter expenses by category or date range
- **Time-based Summaries**: View expenses by day, week, or month
- **Category Breakdown**: See spending percentages by category
- **Export Functionality**: Export to CSV, JSON, and text reports
- **Input Validation**: Improved error handling for user inputs
- **Unit Tests**: Comprehensive test suite with 8+ test cases
- **Utility Module**: Helper functions for validation and formatting
- **Enhanced Documentation**: Detailed README with examples and usage guide
- **Delete Functionality**: Remove incorrect expense entries
- **Improved UI**: Better formatted menu with emojis and tables

### Changed
- Renamed main file from `expense_tracker.py` to `expensestracker.py`
- Improved menu system with 10 options instead of 4
- Enhanced terminal output formatting
- Better error messages and user feedback

### Fixed
- Input validation for amounts and dates
- File handling edge cases
- Data persistence issues

## [1.0.0] - 2025-09-08

### Added
- Initial release
- Basic expense logging
- Category support (Food, Travel, Other)
- View all expenses
- Total expenses calculation
- Simple command-line menu
- Text file storage
