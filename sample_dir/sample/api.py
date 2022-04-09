import datetime as dt

CONST_VALUE = 'THIS IS TEST!'
def show_today():
    date = dt.date.today()
    print(date)
    return None

if __name__ == "__main__":
    print(show_today())