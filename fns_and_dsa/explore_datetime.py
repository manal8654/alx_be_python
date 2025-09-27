from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    # عرض التاريخ والوقت بالصيغة: YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    # عرض التاريخ فقط: YYYY-MM-DD
    print("Future date:", future_date.strftime("%Y-%m-%d"))


def main():
    # الجزء الأول: عرض التاريخ والوقت الحالي
    display_current_datetime()

    # الجزء الثاني: حساب التاريخ المستقبلي
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
