from datetime import datetime

def get_days_from_today(date: str) -> int | None:

    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - input_date).days
    except ValueError:
        return None

print(get_days_from_today("2020-10-09"))
