from datetime import datetime, timedelta


def add_days_to_date_entered(user_input, days_to_add):

    date_format = "%m-%d-%Y"
    date_object = datetime.strptime(user_input, date_format)


    result_date = date_object + timedelta(days=days_to_add)


    return result_date.strftime("%m-%d-%Y")


def Menstrual_Cycle():
    print("Welcome To Your Menstruation App")
    print("This App helps you Calculate your next Cycle, Your Safe Day, And Your Not Safe Day")


    last_menstrual_cycle = input("Enter Date of Last Menstrual cycle (MM-dd-yyyy): ")
    length_menstrual_cycle = int(input("How Long Did Last Menstrual Cycle Last for: "))


    result = add_days_to_date_entered(last_menstrual_cycle, length_menstrual_cycle)
    end_of_safe_day = add_days_to_date_entered(result, 7)
    not_safe_day = add_days_to_date_entered(result, 8)


    print(f"Your Next Menstrual Cycle would Most Likely begin on: {result}")
    print(
        f"According to research starting from the 1st day to 7th day, you are considered not to be fertile and less likely to get pregnant.")
    print(f"So you can have fun from {result} to {end_of_safe_day}")
    print(
        f"According to research starting from the 8th day to 19th day, you are considered to be fertile which could lead to pregnancy.")
    print(f"So you would want to abstain from sex on: {not_safe_day}")
