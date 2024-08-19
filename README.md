# Customer Banking Application

## Overview
This is a customer banking application, where the user inputs three values "Current Balance", "Interest Rate" and "Duration in Months" for the Savings and CD accounts. The application outputs the interest earned and the updated balance.

#### Code Layout
- Accounts.py
    - This contains the "class Accounts" which has the "set balance" and "set interest methods"
    - This is the file that drives the entire application.
- savings_account.py
    - This file contains the function "create_savings_account" which imports the class Accounts.
    - It calculates the interest earned and updated balance for the savings account.   
- cd_account.py
    - This file contains the function "create_cd_account" which imports the class Accounts.
    - It calculates the interest earned and updated balance for the CD account.     
- customer_banking.py
    - This file runs the program by requesting user input for "Current Balance", "Interest Rate" and "Duration in Months" for the Savings and CD accounts.
    - Based on the user input, the interest earned and the updated balance is printed.

#### Sample application view

