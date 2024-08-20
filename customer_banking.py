# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your savings account balance? '))
    if savings_balance > 0:
        savings_interest = float(input('What is your savings account interest rate? '))
        if savings_interest > 0:
            savings_maturity = int(input('What is the duration for your savings account in months? Please enter a whole number greater than zero. '))
            if savings_maturity > 0:
            # Call the create_savings_account function and pass the variables from the user.
                updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
                # Print out the interest earned and updated savings account balance with interest earned for the given months.
                # ADD YOUR CODE HERE
                print(f'\nThe interest earned for the duration of {savings_maturity} months on the savings account is: ${interest_earned :,.2f}')
                print(f'The updated savings account balance including the interest earned is : ${updated_savings_balance :,.2f}\n')
                # Prompt the user to set the CD balance, interest rate, and months for the CD account.
                # ADD YOUR CODE HERE
                cd_balance = float(input('What is your CD account balance? '))
                if cd_balance > 0:
                    cd_interest = float(input('What is your CD account interest rate? '))
                    if cd_interest > 0:
                        cd_maturity = int(input('What is the duration for your CD account in months? Please enter a whole number greater than zero. '))
                        if cd_maturity > 0:  
                          # Call the create_cd_account function and pass the variables from the user.
                            updated_cd_balance, CD_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
                        # Print out the interest earned and updated CD account balance with interest earned for the given months.
                        # ADD YOUR CODE HERE
                            print(f'\nThe interest earned for the duration of {cd_maturity} months on the CD account is: ${CD_interest_earned :,.2f}')
                            print(f'The updated CD account balance including the interest earned is : ${updated_cd_balance :,.2f}\n')
                        else:
                            print("CD maturity duration should be an integer greater than zero. Exiting the program!")
                    else:
                        print("CD Interest rate should be greater than zero. Exiting the program!")
                else:
                    print("CD Balance should be greater than zero. Exiting the program!")
            else:
                print("Savings maturity duration should be an integer greater than zero. Exiting the program!")
        else:
            print("Savings interest rate should be a  greater than zero. Exiting the program!")
    else:
        print("Savings balance should be  greater than zero. Exiting the program!")
            
if __name__ == "__main__":
    # Call the main function.
    main()
