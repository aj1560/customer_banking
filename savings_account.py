"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    
    new_account = Account(balance, 0)
    #interest = 0 
    #float(interest)

    # Calculate interest earned
     # ADD YOUR CODE HERE

    new_interest_earned = balance * (interest_rate/100 *months/12)

    print(new_interest_earned)
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    
    new_balance = balance + new_interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    Final_Bal=new_account.set_balance(new_balance)
    print(Final_Bal)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    Final_Int_Earned=new_account.set_interest(new_interest_earned)
    print(Final_Int_Earned)
    # Return the updated balance and interest earned.
    return  Final_Bal, Final_Int_Earned
           # ADD YOUR CODE HERE
