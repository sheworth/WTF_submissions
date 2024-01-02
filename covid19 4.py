from urllib.request import urlopen
from datetime import datetime


def get_data(date=None, iso=None):
    url = BASE_URL + "reports/total?date=" + date
    if iso:
        url += "&iso=" + iso
    print("Fetching data...")
    with urlopen(url) as response:
        data = response.read()
    data = eval(data)
    data = data["data"]
    if not data:
        print("No data found for the given date and country code")
        return
    print("Total Confirmed Cases: ", data["confirmed"])
    print("Total Active Cases: ", data["active"])
    print("Total Deaths: ", data["deaths"])
    print("New Cases: ", data["confirmed_diff"])
    print("New Deaths: ", data["deaths_diff"])
    print("Total Recovered: ", data["recovered"])


BASE_URL = "https://covid-api.com/api/"


def covid19():
    print("Welcome to the COVID-19 Tracker App")
    print("Please select from the following options:")
    print("1. Global Data")
    print("2. Country Data")
    print("3. See the list of countries")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "4":
        exit()
    elif choice == "3":
        # Get list of countries
        with urlopen(BASE_URL + "regions") as resp:
            body = resp.read()
        countries = eval(body)["data"]
        for country in countries:
            print(f'{country["iso"]}: {country["name"]}')
    elif choice == "1":
        date_input = input("Enter the date in YYYY-MM-DD forma(default to current date): ") or datetime.now().strftime(
            "%Y-%m-%d")
        # Get global data
        get_data(date_input)
    elif choice == "2":
        date_input = input("Enter the date in YYYY-MM-DD forma(default to current date): ") or datetime.now().strftime(
            "%Y-%m-%d")
        # Get country data
        country_iso = input("Enter the country code(NGA for Nigeria): ")
        get_data(date_input, country_iso)

if __name__ == "__main__":
    while True:
        covid19()
        print("\n")
        cont = input("Do you want to continue(y/n): ")
        if cont.lower() == "n":
            break
    
