from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
   
    today = date.today()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until = (birthday_this_year - today).days
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming

users = [
    {"name": "John Doe", "birthday": "1985.04.27"},
    {"name": "Jane Smith", "birthday": "1990.05.02"},
    {"name": "Alice Brown", "birthday": "1992.04.28"},
    {"name": "Bob Wilson", "birthday": "1988.05.03"},
    {"name": "Emma Davis", "birthday": "1995.04.30"},
    {"name": "Michael Taylor", "birthday": "1983.05.01"},
    {"name": "Olivia Martin", "birthday": "1991.07.15"},
    {"name": "James Anderson", "birthday": "1987.12.10"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
