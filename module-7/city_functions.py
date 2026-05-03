def city_country(city, country, population=None, language=None):
    """Return a city and country, with optional population and language."""

    if population is not None and language is not None:
        return f"{city}, {country} - Population {population}, {language}"

    elif population is not None:
        return f"{city}, {country} - Population {population}"

    elif language is not None:
        return f"{city}, {country} - Language {language}"

    else:
        return f"{city}, {country}"


location = city_country("Santiago", "Chile")
locationPop = city_country("Bellevue", "United States", 750000)
locationLang = city_country("Venice", "Italy", 2000000, "Italian")

print(location)
print(locationPop)
print(locationLang)