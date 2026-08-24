"""
Utility functions for Personal Expense Tracker.
Contains helper functions for validation and formatting.
"""

from datetime import datetime


def validate_amount(amount_str):
    """
    Validate and convert amount string to float.
    
    Args:
        amount_str (str): User input for amount
        
    Returns:
        tuple: (is_valid, amount) where is_valid is bool and amount is float or None
    """
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, None
        return True, amount
    except ValueError:
        return False, None


def validate_date(date_str, format="%Y-%m-%d"):
    """
    Validate date string format.
    
    Args:
        date_str (str): Date string to validate
        format (str): Expected date format
        
    Returns:
        tuple: (is_valid, date_string)
    """
    if not date_str:
        return True, datetime.now().strftime(format)
    
    try:
        datetime.strptime(date_str, format)
        return True, date_str
    except ValueError:
        return False, None


def format_currency(amount):
    """
    Format amount as Indian currency.
    
    Args:
        amount (float): Amount to format
        
    Returns:
        str: Formatted currency string
    """
    return f"₹{amount:,.2f}"


def format_date(date_str, from_format="%Y-%m-%d", to_format="%d %B %Y"):
    """
    Convert date format for display.
    
    Args:
        date_str (str): Date string to format
        from_format (str): Current format
        to_format (str): Desired format
        
    Returns:
        str: Formatted date or original if invalid
    """
    try:
        date_obj = datetime.strptime(date_str, from_format)
        return date_obj.strftime(to_format)
    except ValueError:
        return date_str


def calculate_percentage(part, total):
    """
    Calculate percentage.
    
    Args:
        part (float): Part value
        total (float): Total value
        
    Returns:
        float: Percentage (0-100)
    """
    if total == 0:
        return 0
    return (part / total) * 100


def is_date_in_range(date_str, start_str, end_str):
    """
    Check if date falls within range.
    
    Args:
        date_str (str): Date to check (YYYY-MM-DD)
        start_str (str): Start date (YYYY-MM-DD)
        end_str (str): End date (YYYY-MM-DD)
        
    Returns:
        bool: True if date is in range
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        start = datetime.strptime(start_str, "%Y-%m-%d")
        end = datetime.strptime(end_str, "%Y-%m-%d")
        return start <= date <= end
    except ValueError:
        return False
