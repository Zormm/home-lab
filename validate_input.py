#!/usr/bin/env python3
"""
Simple input validation utility for home lab configurations.
"""

def validate_input(value):
    """
    Validates input to ensure it's not empty or just whitespace.
    
    Args:
        value: The input value to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if value is None:
        return False
    
    if isinstance(value, str) and len(value.strip()) == 0:
        return False
    
    return True


if __name__ == "__main__":
    # Example usage
    test_cases = [
        ("x", True),
        ("", False),
        ("   ", False),
        (None, False),
        ("valid input", True),
    ]
    
    print("Running input validation tests:")
    for test_input, expected in test_cases:
        result = validate_input(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} validate_input({repr(test_input)}) = {result} (expected {expected})")
