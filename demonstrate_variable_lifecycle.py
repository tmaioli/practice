import sys

def demonstrate_variable_lifecycle():
    """
    Demonstrates dynamic variable unpacking and explicit memory management
    using the del keyword to clean up a reference scope.
    """
    # Unpack multiple values into distinct variables cleanly
    item_one, item_two, item_three = 100, 200, 300
    print(f"Initial variables: {item_one}, {item_two}, {item_three}")
    
    # Explicitly remove the reference to the first variable
    del item_one
    
    # Verify the remaining variables persist in the current scope
    print(f"Remaining variables after deletion: {item_two}, {item_three}")


def demonstrate_nested_lists():
    """
    Demonstrates how to construct, inspect, and evaluate multi-dimensional
    nested list structures in Python.
    """
    letter_list = ['a', 'b', 'c']
    number_list = [1, 2, 3]
    
    # Create a two-dimensional matrix containing both sublists
    matrix = [letter_list, number_list]
    print(f"Combined nested matrix: {matrix}")
    print(f"First sublist element: {matrix[0]}")
    
    # Determine the structural length of the outer list container
    matrix_length = len(matrix)
    print(f"Total elements in the outer matrix list: {matrix_length}")


def extract_text_between_bounds(source_text: str, target_char: str) -> str:
    """
    Extracts and returns the substring starting from the first occurrence 
    of a target character up to, but excluding, the second occurrence.
    
    Args:
        source_text: The complete string sequence to be searched.
        target_char: The single character delimiter used to establish bounds.
        
    Returns:
        The extracted substring slice between the target positions.
        
    Raises:
        ValueError: If the target character does not appear at least twice.
    """
    # Locate the initial occurrence of the delimiter
    first_index = source_text.find(target_char)
    if first_index == -1:
        raise ValueError(f"The delimiter '{target_char}' was not found in the text.")
        
    # Locate the subsequent occurrence by starting the search immediately after the first
    second_index = source_text.find(target_char, first_index + 1)
    if second_index == -1:
        raise ValueError(f"The delimiter '{target_char}' must appear at least twice.")
        
    # Return the clean structural slice between the two found positions
    return source_text[first_index:second_index]


def main():
    """
    Acts as the main execution entry point for the script, running
    each demonstration routine sequentially.
    """
    print("--- Execution Step 1: Variable Lifecycle ---")
    demonstrate_variable_lifecycle()
    print("\n--- Execution Step 2: Nested Lists ---")
    demonstrate_nested_lists()
    
    print("\n--- Execution Step 3: Optimized String Parsing ---")
    sample_word = "juxtaposition"
    search_character = "t"
    print(f"Analyzing source word: '{sample_word}' for target: '{search_character}'")
    
    try:
        resulting_slice = extract_text_between_bounds(sample_word, search_character)
        print(f"Successfully extracted substring: '{resulting_slice}'")
    except ValueError as error:
        print(f"Data processing error: {error}", file=sys.stderr)


if __name__ == "__main__":
    main()
