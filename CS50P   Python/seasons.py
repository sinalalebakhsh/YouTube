from datetime import date
import re
import sys
import inflect

p = inflect.engine()



def main():
    birth_date = input("Date of birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid Date")
    date_of_birth = date(int(year), int(month), int(day))
    date_of_today = date.today()
    diffrents = date_of_today - date_of_birth
    total_minutes = diffrents.days * 24 * 60
    output = p.number_to_words(total_minutes, andword="")
    print(output.capitalize() + " minutes")


def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day



if __name__ == "__main__":
    main()
