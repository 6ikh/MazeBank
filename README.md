# Maze Bank User Management System

This is a Python project that simulates a user management system for Maze Bank. The project consists of two classes, `User` and `MZBANK`, which handle user information and banking operations. Users can create accounts, deposit and withdraw funds, and apply for loans.

## Getting Started

To use the Maze Bank User Management System, follow these steps:

1. Clone the repository to your local machine or download the Python script.

2. Open the Python script in your preferred development environment.

3. Run the script to start the Maze Bank application.

## User Class

The `User` class is used to create and display user information. It has the following attributes:

- `name`: User's name
- `age`: User's age
- `gender`: User's gender

It also has a method `displayInfo()` to display user information.

## MZBANK Class

The `MZBANK` class inherits from the `User` class and extends it with banking functionalities. It has the following additional attributes and methods:

Attributes:

- `balance`: User's account balance
- `creditLimit`: User's credit limit

Methods:

- `deposit(amount)`: Deposit funds into the account.
- `withdraw(amount)`: Withdraw funds from the account, with overdraft protection.
- `loanapplication(creditscore, incomeAmount)`: Apply for a loan based on credit score and income.

## Usage

1. When you run the script, you will be prompted to enter your name, age, and gender to create a Maze Bank account.

2. After account creation, you can choose from the following options:
   - `[1] Make A Deposit`
   - `[2] Make A Withdrawal`
   - `[3] Apply For A Loan Application`
   - `[4] End The Program`

3. Select the desired option by entering the corresponding number.

### Option 1: Make A Deposit
- Enter the amount you want to deposit.

### Option 2: Make A Withdrawal
- Enter the amount you want to withdraw, and overdraft protection will be applied if necessary.

### Option 3: Apply For A Loan Application
- Enter your credit score and annual income to apply for a loan. The system will calculate your credit limit and notify you of the result.

### Option 4: End The Program
- Select this option to exit the Maze Bank application.

## Notes

- Your account balance and loan status will be displayed after each transaction or application.

- If your credit score is below 500, your loan application will be declined.

Enjoy your experience with Maze Bank!
