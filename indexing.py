# In this exercise, you will write a program that gets
 # a specific character from a phrase entered by the user.

# Project Title:Indexing_challange
# Instructions:
# Prerequisites: Python 3
# Built with: Atom text editor
# Thomas Maioli
# coded in Python 3.7
# date 2019-02-20
# Project name: Strings
# Issues and concerns: none
# Problem domain Strings


def main():
    phrase = str(input("Enter a phrase "))
    sentence = 'You entered \"{0}\"' .format(phrase)
    print(sentence)
    location = int(input("Which charater would you like to see? "))
    letter = phrase[location - 1]
    print(letter)

main()

```
Here's a clear, part-by-part breakdown of your code:

### 🔹 Line 1: `phrase = str(input("Enter a phrase "))`
| Part | What it does |
|------|--------------|
| `input("Enter a phrase ")` | Displays the prompt `"Enter a phrase "` to the user, waits for them to type something and press Enter, then returns what they typed. |
| `str(...)` | Converts the result to a string. **Note:** In Python 3, `input()` already returns a string, so `str()` is redundant but harmless. (It was more relevant in Python 2, where `input()` tried to evaluate the input as code.) |
| `phrase = ...` | Assigns the resulting string to a variable named `phrase` so you can use it later. |

### 🔹 Line 2: `sentence = 'You entered \"{0}\"' .format(phrase)`
| Part | What it does |
|------|--------------|
| `'You entered \"{0}\"'` | A string template. The `\"` are **escaped double quotes**, telling Python to treat them as literal quote characters instead of ending the string. `{0}` is a **placeholder** that will be replaced by the first argument passed to `.format()`. |
| `.format(phrase)` | A string method that replaces `{0}` with the value stored in `phrase`. |
| `sentence = ...` | Saves the final formatted string into a variable named `sentence`. |
| *(Note on spacing)* | The space before `.format()` is syntactically valid but unconventional. PEP 8 (Python's style guide) recommends attaching methods directly: `'.format(...)'` |

---

### 💡 Key Concepts Used
- **User Input**: `input()` pauses execution and captures keyboard input.
- **String Formatting**: `.format()` inserts variables into strings using `{}` placeholders. `{0}` refers to the first argument, `{1}` to the second, etc.
- **Escape Characters**: `\"` lets you include literal double quotes inside a string. (Though not strictly needed here since the outer quotes are single quotes.)

---

### ✅ Example Run
```text
Enter a phrase Hello World
```
After running:
- `phrase` → `"Hello World"`
- `sentence` → `'You entered "Hello World"'`

---

### 🛠️ Modern/Cleaner Alternatives
1. **Remove redundancy & unnecessary escaping:**
   ```python
   phrase = input("Enter a phrase ")
   sentence = 'You entered "{0}"'.format(phrase)
   ```

2. **Use f-strings (Python 3.6+, recommended):**
   ```python
   phrase = input("Enter a phrase ")
   sentence = f'You entered "{phrase}"'
   ```
   F-strings are more readable, faster, and the current Python best practice.

Let me know if you'd like to dive deeper into string formatting, input handling, or Python version differences!


```
