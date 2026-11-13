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
def get_days_from_today(date):
    """Returns the number of days as an int (positive if the date is in the past,
        negative if it is in the future) or None if the date is invalid
    """
    today = datetime.today()
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        
    except ValueError:
        return None
    
    return (today.date() - date.date()).days

    
def get_date(string, character):
    """Convert "YYYY<character>M<character>D" into the string "YYYY-M-D" """
    year, month, day = string.split(character)
    return f"{year}-{month}-{day}"
     
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
            new_date = date
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
                new_date = date_arr[2] + "-"+ str(month) +"-"+ date_arr[0]

        if new_date:
            diff = get_days_from_today(new_date)
            if diff is not None:
                print(diff)
                break
        print("Enter a valid date.")

