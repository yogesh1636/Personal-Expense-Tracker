# Contributing to Personal Expense Tracker

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome feedback and criticism gracefully
- Focus on the code, not the person

## How to Contribute

### 1. **Reporting Bugs**
- Use the GitHub issue tracker
- Provide a clear title and description
- Include steps to reproduce the bug
- Attach relevant error messages or screenshots

### 2. **Suggesting Enhancements**
- Check existing issues first to avoid duplicates
- Explain the use case and benefits
- Provide code examples if applicable

### 3. **Submitting Pull Requests**

#### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/yogesh1636/Personal-Expense-Tracker.git
cd Personal-Expense-Tracker

# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Run tests
python -m unittest test_expensestracker.py -v

# Commit and push
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

#### PR Guidelines
- Use a clear, descriptive title
- Reference related issues
- Include a summary of changes
- Add/update tests as needed
- Update documentation if applicable
- Keep commits atomic and well-organized

### 4. **Code Style**

Follow PEP 8 guidelines:
```python
# Use descriptive variable names
total_expenses = sum(exp['amount'] for exp in expenses)

# Use docstrings for functions
def calculate_total(expenses):
    """
    Calculate total of all expenses.
    
    Args:
        expenses (list): List of expense dictionaries
        
    Returns:
        float: Sum of all amounts
    """
    return sum(exp['amount'] for exp in expenses)

# Use type hints where applicable
def validate_amount(amount: str) -> tuple[bool, float]:
    """Validate and convert amount string to float."""
    pass
```

### 5. **Testing**

Write unit tests for new features:
```python
def test_new_feature(self):
    """Test description of what is being tested."""
    # Arrange
    test_data = ...
    
    # Act
    result = function_to_test(test_data)
    
    # Assert
    self.assertEqual(result, expected_value)
```

## Development Workflow

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes
4. Write/update tests
5. Update documentation
6. Submit a pull request with a clear description

## Areas for Contribution

- 🐛 Bug fixes
- ✨ New features (e.g., budget alerts, recurring expenses)
- 📚 Documentation improvements
- 🧪 Test coverage expansion
- ♻️ Code refactoring
- 🎨 UI/UX improvements
- 🌍 Translations

## Potential Feature Ideas

- [ ] Budget limit alerts
- [ ] Recurring expenses
- [ ] Data visualization (charts/graphs)
- [ ] Multiple currencies support
- [ ] Cloud backup
- [ ] Mobile app
- [ ] Web interface
- [ ] Email reports

## Questions?

- Open an issue for general questions
- Check existing issues and discussions
- Contact the maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to make this project better! 🙌
