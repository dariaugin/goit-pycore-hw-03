from datetime import datetime
import re
months = {
    "january": 1,
    "february": 2,
    "march":3,
    "april":4,
    "may": 5,
    "june":6,
    "july":7,
    "august":8,
    "september":9,
    "october":10,
    "november":11,
    "december":12
}
def get_days_from_today(date_par):
    """Return the number of days between the given date and today.

    The result is positive if the given date is in the past
    and negative if it is in the future
    """

    today = datetime.today()
    return (today.date() - date_par.date()).days

def check_date(year,month,day):
    """Return a datetime for the given parts or None if the date doesn't exist"""
    try:
        date = datetime(year = int(year), month = int(month), day = int(day))
        return date
    except ValueError:
        return None
    
def get_date(string, character):
     """Split string by character into year, month and day and validate it.

        Returns a datetime or None if the date doesn't exist
     """
     
     splt_str = string.split(character)
     return check_date(splt_str[0], splt_str[1], splt_str[2])
     
# possible formats for input:

#   2025-03-12
#   2025 03 12
#   2025.03.12
#   2025/03/12
#   12 march 2025

if __name__ == "__main__":
    while True:
        date = input("Input your date: ").strip()
        new_date = None
        if re.fullmatch( r"\d{4}-\d{1,2}-\d{1,2}", date):
            new_date = get_date(date,"-")
        elif re.fullmatch(r"\d{4}\.\d{1,2}\.\d{1,2}", date):
            new_date = get_date(date,".")
        elif re.fullmatch(r"\d{4}/\d{1,2}/\d{1,2}", date):
            new_date = get_date(date,"/")
        elif re.fullmatch(r"\d{4} \d{1,2} \d{1,2}", date):
            new_date = get_date(date," ")
        elif re.fullmatch(r"\d{1,2} [a-zA-Z]+ \d{4}", date):
            date_arr = date.split()
            month = months.get(date_arr[1].lower())
            if month:
                new_date = check_date(date_arr[2], month, date_arr[0] )

        if new_date:
            diff = get_days_from_today(new_date)
            print(diff)
            break
        print("Enter a valid date.")

