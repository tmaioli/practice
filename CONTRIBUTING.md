# Contributing to Python Practice Repository

This is a learning repository documenting my Python programming journey. While this is primarily a personal practice project, I welcome feedback and suggestions!

## How to Contribute

### Reporting Issues
If you find bugs or have suggestions for improvement:
1. Check if the issue already exists
2. Create a new issue with:
   - Clear description
   - Expected vs actual behavior
   - Steps to reproduce (if applicable)

### Suggesting Improvements
Feel free to suggest:
- Better algorithms
- Code optimization
- Additional features
- Documentation improvements

## Code Style Guidelines

When modifying existing code or adding new scripts:

### Naming Conventions
- Use `snake_case` for variables and functions
- Use `UPPER_CASE` for constants
- Use descriptive names (e.g., `number_of_people` not `nop`)

### Functions
- Keep functions focused on a single task
- Add docstrings explaining purpose, parameters, and return values
- Example:
```python
def calculate_average(grades):
    """Calculate the average of a list of grades.
    
    Args:
        grades: List of numeric grade values
        
    Returns:
        float: The average grade
    """
    return sum(grades) / len(grades)
```

### Comments
- Explain **why**, not just **what**
- Remove commented-out code before committing
- Update comments when modifying code

### Error Handling
- Validate user input
- Handle edge cases (negative numbers, empty strings, etc.)
- Provide clear error messages

## Adding New Scripts

When adding a new practice script:

1. **File naming**: Use descriptive lowercase names with underscores
2. **Header comments**: Include project info at the top
3. **Main function**: Wrap executable code in a `main()` function
4. **Entry point**: Use `if __name__ == "__main__":` guard

### Template for New Scripts
```python
"""
# Project Title: [Descriptive Name]
# Version: 1.0
# Author: Thomas Maioli
# Date: YYYY-MM-DD
# Description: Brief description of what this script does
"""

def main():
    """Main function."""
    # Your code here
    pass


if __name__ == "__main__":
    main()
```

## Testing

Before submitting changes:
- Test your code with various inputs
- Check edge cases
- Ensure no syntax errors
- Verify expected output

## Questions?

Feel free to open an issue for any questions about the project structure or code!
