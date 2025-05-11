# Python Type Hints Examples

This repository contains examples and demonstrations of Python type hints, showing how they can improve code quality, readability, and help catch errors during development.

This repository is connected to the medium article [Coding Zen - Why Type Hints Are Worth Your Time](https://medium.com/@CodingZen/coding-zen-why-type-hints-are-worth-your-time-8c36b1144e83).

## Project Overview

Python type hints (introduced in PEP 484) allow developers to specify the expected types of variables, function parameters, and return values. This project demonstrates:

- Basic usage of type hints
- How type hints can catch errors during development
- Practical applications in real-world scenarios
- Benefits for code documentation and maintainability

## Files in the Repository

- `src/type_hints_examples.py`: Basic examples comparing functions with and without type hints, demonstrating how type checkers can catch errors.
- `src/type_hints_practical_example.py`: A more complex example showing how type hints can improve a statistical calculation function, with proper error handling and documentation.
- `requirements.txt`: Dependencies required for the project, including typing-related packages.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd CodingZen-Type-Hints-Article
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the examples:
   ```
   python src/type_hints_examples.py
   python src/type_hints_practical_example.py
   ```

5. To see type checking in action, install and run mypy:
   ```
   pip install mypy
   mypy src/type_hints_examples.py
   mypy src/type_hints_practical_example.py
   ```

## Why Use Type Hints?

- **Catch errors earlier**: Identify type-related bugs during development rather than at runtime
- **Improve IDE support**: Better code completion, refactoring, and navigation
- **Self-documenting code**: Make your code more readable and understandable
- **Easier maintenance**: Clearer interfaces between components