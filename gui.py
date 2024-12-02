import tkinter as tk
from tkinter import messagebox, simpledialog
from country import Country


class LanguageInfoApp:
    """
    Sets up gui.
    """

    def __init__(self, root: tk.Tk, countries: list[Country]):
        """
        Initializes the LanguageInfoApp gui.
        """
        self.root = root
        self.root.title("Country Language Information")
        self.countries = countries

        # GUI Components
        self.listbox = tk.Listbox(root, width=50, height=20)
        self.listbox.grid(row=0, column=0, rowspan=6, columnspan=3)

        self.refresh_button = tk.Button(root, text="Refresh Country List", command=self.refresh_country_list)
        self.refresh_button.grid(row=6, column=0)

        self.view_button = tk.Button(root, text="View Languages", command=self.view_languages)
        self.view_button.grid(row=6, column=1)

        self.search_button = tk.Button(root, text="Search by Country", command=self.search_country)
        self.search_button.grid(row=6, column=2)

        # Initial set of the country list
        self.refresh_country_list()

    def refresh_country_list(self):
        """
        Refreshes the country list displayed in the list.
        """
        self.listbox.delete(0, tk.END)
        for country in self.countries:
            self.listbox.insert(tk.END, country.name)

    def view_languages(self):
        """
        Displays the languages of the selected country.
        """
        try:
            selected_index = self.listbox.curselection()
            if not selected_index:
                raise ValueError("No country selected")

            selected_country = self.countries[selected_index[0]]
            languages = selected_country.get_languages()
            messagebox.showinfo("Languages", f"{selected_country.name} languages:\n{languages}")
        except ValueError as e:
            messagebox.showwarning("Selection Error", str(e))

    def search_country(self):
        """
        Searches for a country by name and displays its languages.
        """
        try:
            country_name = simpledialog.askstring("Search", "Enter country name:")
            if not country_name:
                raise ValueError("Country name cannot be empty.")

            found_country = next(
                (country for country in self.countries if country_name.lower() in country.name.lower()), None
            )
            if found_country:
                languages = found_country.get_languages()
                messagebox.showinfo("Country Found", f"{found_country.name} languages:\n{languages}")
            else:
                raise LookupError("Country not found")
        except (ValueError, LookupError) as e:
            messagebox.showinfo("Search Error", str(e))


def run_app(countries: list[Country]):
    """
    Runs the gui application.
    """
    root = tk.Tk()
    app = LanguageInfoApp(root, countries)
    root.mainloop()
