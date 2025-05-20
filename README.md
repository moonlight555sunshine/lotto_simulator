# 🎲 Lottery Number Checker

This Python script simulates a simple lottery number game. The computer randomly selects 6 unique numbers between 1 and 49. The user is prompted to enter 6 unique numbers in the same range. The program then compares the two sets and shows how many numbers match.

## 📋 Features

- Input validation (numeric, integer, range 1–49, and uniqueness)
- Random number generation with no duplicates
- Comparison of user and computer numbers
- Sorted output for readability

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Save the script as `lottery.py`.
3. Run the script in your terminal or command prompt:

   ```bash
   python lottery.py
4. Follow the prompts to enter 6 numbers, one at a time.

## ✅ Example Output
```
Enter 1 number: 5
Enter 2 number: 12
Enter 3 number: 23
Enter 4 number: 34
Enter 5 number: 45
Enter 6 number: 49
Your numbers: [5, 12, 23, 34, 45, 49]
Computer numbers: [3, 12, 25, 34, 38, 49]
You have 3 numbers in common
```
## 💡 Notes
- The computer’s numbers are generated using random.sample() to ensure uniqueness.
- Input is thoroughly validated:
    - Must be a number
    - Must be an integer
    - Must be within the range 1–49
    - Must not be repeated

Enjoy testing your luck! 🍀

