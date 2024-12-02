from data import load_country_data
from gui import run_app

if __name__ == "__main__":
    file_path = "country_languages.csv"
    countries = load_country_data(file_path)
    run_app(countries)
