CURRENT_YEAR = 2024


def calculate_age(year_of_birth):
    if year_of_birth > CURRENT_YEAR:
        raise ValueError("Podany rok jest późniejszy od aktualnego")

    return CURRENT_YEAR - year_of_birth


print(calculate_age(2025))
