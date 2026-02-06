# Todo Console App - Constitution

## Project Principles

### 1. Code Quality
- Follow PEP 8 Python style guidelines
- Use type hints for all functions
- Write clear, self-documenting code
- Keep functions small and focused (< 20 lines)

### 2. Architecture
- Use object-oriented design
- Separate concerns: UI, Business Logic, Data Storage
- Single Responsibility Principle for each class

### 3. Data Management
- Store tasks in memory using Python list/dict
- Each task must have: id, title, description, completed status
- Use unique integer IDs (auto-incrementing)

### 4. User Experience
- Clear command-line interface
- Helpful error messages
- Input validation for all user inputs
- Confirmation messages for all actions

### 5. Testing Philosophy
- Code must be testable
- Use defensive programming
- Handle edge cases (empty lists, invalid IDs)

## Technology Constraints

- **Python Version:** 3.13+
- **Package Manager:** UV
- **No External Dependencies:** Pure Python only for Phase 1
- **Storage:** In-memory (no files or databases)

## Project Structure