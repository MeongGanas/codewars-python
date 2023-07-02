def calculate_age(year_of_birth, current_year):
    # your code here
    key = {1: "year"}
    age = current_year - year_of_birth
    return f"You are {age} {key.get(age, 'years')} old." if age > 0 else f"You will be born in {age*-1} {key.get(age, 'years')}." if age < 0 else "You were born this very year!"
