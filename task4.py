from datetime import datetime, timedelta
users = [
    {"name": "Daria",
     "birthday": "2026.10.30"},
     {"name": "Sarah",
     "birthday": "2025.10.31"},
     {"name": "Maria",
     "birthday": "2026.06.12"}
]

def change_birthday_year(date, year):
    """Return date moved to year.

    A 29 February birthday becomes 28 February in non-leap years
    """
    try:
        return date.replace(year=year)
    except ValueError:
        return date.replace(year=year, day=28)

def get_upcoming_birthdays(users):
    """Return the users whose birthday falls within the next 7 days (today included).

    Returns:
        A list of dicts with the keys - name and congratulation_date - ("YYYY.MM.DD").
        If a birthday falls on a weekend the congratulation date is moved
        to the following Monday. Users with an invalid birthday are skipped
    """
    next_week_bd = []
    today = datetime.today().date()
    for user in users:
        try:
            user_bd = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            print(user["birthday"] + " ---> invalid date")
            continue
        user_bd_thisyear = change_birthday_year(user_bd, today.year)
        if user_bd_thisyear < today:
            user_bd_thisyear = change_birthday_year(user_bd, today.year + 1)
        
        dif = (user_bd_thisyear - today).days
        if 0 <= dif <= 6:
            congratulation_date = user_bd_thisyear
            if congratulation_date.weekday() >= 5 :
                congratulation_date +=  timedelta(days=(7 - congratulation_date.weekday()))
            

            next_week_bd.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })
            
    return next_week_bd
if __name__ == "__main__":
    print(get_upcoming_birthdays(users))


