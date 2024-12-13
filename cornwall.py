def computeRate(days, meal_plan_code=None):
    """
    Computes the rate for the stay at Cornwall's Country Inn.
    :param days: Number of days of stay
    :param meal_plan_code: Optional meal plan code (A, C, or None)
    :return: Total cost for the stay
    """
    if meal_plan_code is None:
        rate_per_day = 99.99 
    elif meal_plan_code.upper() == "A":
        rate_per_day = 169.00  
    elif meal_plan_code.upper() == "C":
        rate_per_day = 112.00  
    else:
        return -1  
    
    return rate_per_day * days

def main():
    rate = 0.00
    dayString = input("How many days do you plan to stay? ")
    days = int(dayString)
    
    question = input("Do you want a meal plan? Y or N: ").strip().upper()
    
    if question == "Y":
        meal_plan_code = input("Enter meal plan code (A for all meals, C for breakfast only): ").strip().upper()
        rate = computeRate(days, meal_plan_code)
    else:
        rate = computeRate(days)
    
    if rate == -1:
        print("Invalid meal plan code. Please try again.")
    else:
        print(f"The total cost for your stay is ${rate:.2f}")

main()
