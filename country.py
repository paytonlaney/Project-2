class Country:
    """
    Represents a country and its language data.
    """
    def __init__(self, name: str, main_languages: str, minority_languages: str):
        self.__name = name
        self.__main_languages = main_languages
        self.__minority_languages = minority_languages

    @property
    def name(self) -> str:
        """
        Returns the name of the country.
        """
        return self.__name

    def get_languages(self) -> str:
        """
        Returns a string of the main and minority languages of the country.
        """
        languages = f"Main Languages: {self.__main_languages}\n"
        if self.__minority_languages and self.__minority_languages.lower() != "none":
            languages += f"Minority Languages: {self.__minority_languages}"
        else:
            languages += "No documented minority languages."
        return languages

    def __str__(self) -> str:
        return self.__name
