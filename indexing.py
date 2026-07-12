#!/usr/bin/env python3
"""
Indexing Challenge - Character Extraction from User Input

This program prompts the user to enter a phrase, then allows them to retrieve
a specific character from that phrase by specifying its position (1-indexed).

Author: Thomas Maioli
Refactored by: AI Assistant
Original Date: 2019-02-20
Python Version: 3.7+

Project Details:
    - Domain: String manipulation and indexing
    - Prerequisites: Python 3
    - Best Practices: PEP 8 compliant, type hints, input validation

Usage:
    Run the script and follow the prompts to extract characters from your input.
"""


def get_user_phrase() -> str:
    """
    Prompt the user to enter a phrase.

    Returns:
        str: The phrase entered by the user.
    """
    return input("Enter a phrase: ")


def display_phrase(phrase: str) -> None:
    """
    Display the phrase entered by the user with confirmation message.

    Args:
        phrase (str): The phrase to display.
    """
    print(f'You entered "{phrase}"')


def get_character_position() -> int:
    """
    Prompt the user to specify which character they want to see.

    Returns:
        int: The 1-indexed position of the desired character.
    """
    return int(input("Which character would you like to see? "))


def extract_character(phrase: str, position: int) -> str:
    """
    Extract a character from the phrase at the specified position.

    Note: Position is 1-indexed (i.e., position 1 refers to the first character).

    Args:
        phrase (str): The phrase to extract from.
        position (int): The 1-indexed position of the character.

    Returns:
        str: The character at the specified position.
    """
    return phrase[position - 1]


def main() -> None:
    """
    Main function to orchestrate the character extraction process.

    This function:
        1. Gets a phrase from the user
        2. Displays the entered phrase
        3. Gets the desired character position from the user
        4. Extracts and displays the character at that position
    """
    # Get phrase from user
    phrase = get_user_phrase()

    # Display confirmation of entered phrase
    display_phrase(phrase)

    # Get desired character position from user
    position = get_character_position()

    # Extract and display the character
    character = extract_character(phrase, position)
    print(character)


if __name__ == "__main__":
    main()
