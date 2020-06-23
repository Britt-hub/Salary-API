valid_states = ("FL", "CA", "NY", "NC", "TX")
expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}


def calculate_expected_salary(number_of_experience_years, user_information, number_of_edu_years, is_developer,
                              is_designer, users_coding_languages, user_software_programs):
    try:
        expected_salary = expected_salaries[user_information["state"].upper()]
        number_of_education_years_as_an_integer = int(number_of_edu_years)

    except KeyError:
        print(" INPUT ERROR: Please enter a valid state")
    except ValueError:
        print("***** INPUT ERROR: Please enter a valid number for years of learning experience")
    else:
        new_expected_salary = 0
        if number_of_experience_years == 1:
            new_expected_salary = expected_salary - 5000  # Deducting 5K because the user only has two years of experience.
        elif number_of_experience_years == 2:
            new_expected_salary = expected_salary - 3000  # Deducting 3K because the user only has two years of experience.
        elif number_of_experience_years == 3:
            new_expected_salary = expected_salary + 1000  # Adding 1K because the user has 3 years of experience.
        elif number_of_experience_years == 4:
            new_expected_salary = expected_salary + 5000  # Adding 5K because the user has 4 years of experience.

            print(10 + "*" + "Sorry, please enter one of the valid options" + 10 * "*")

        if is_developer == True:
            if len(users_coding_languages) < 3:
                new_expected_salary = new_expected_salary - 10000  # 65,000 - $10,000 = $55k
                print("Learn some more languages; deduct $10K form the expected salary.")

            elif len(users_coding_languages) > 3:
                new_expected_salary = new_expected_salary + 10000

            else:
                new_expected_salary = new_expected_salary + 5000

        # Below you could just do if is_designer and leave of True

        if is_designer == True:
            if len(user_software_programs) < 3:
                new_expected_salary = new_expected_salary - 10000  # 65,000 - $10,000 = $55k
                print("Learn more design tools; deduct $10K form the expected salary.")

            elif len(user_software_programs) > 3:
                new_expected_salary = new_expected_salary + 10000

            else:
                new_expected_salary = new_expected_salary - 5000

            print("Expect $" + str(new_expected_salary) + " for your level of experience.")
            for state in expected_salaries:
                salary = expected_salaries[state]
                print("Your starting salary living in " + state + " could have been $" + str(salary) + ".")

