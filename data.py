import csv
from country import Country


def load_country_data(file_path: str) -> list[Country]:
    """
    Loads data from csv file
    """
    countries = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                country_name = row.get("Country", "Unknown")
                main_languages = row.get("Main Languages", "Unknown")
                minority_languages = row.get("Minority Languages", "None")
                country = Country(country_name, main_languages, minority_languages)
                countries.append(country)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return countries
