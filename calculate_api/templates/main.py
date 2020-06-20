from UserProfile import UserProfile

# users_experience = input("How many years of experience do you have developing software?\n[1] Less than 1 year"
#                                  "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
#                                  "8+ years of experience \n")

# self represents the instance of the class. By using the “self” keyword we can
# access the attributes and methods of the class
# most class has getters and setters. If you want to update use set. If you want to get or call a class use get.
# UserProfile
# class UserProfile:

    # def __init__(self, dob, full_name, country, state, number_of_education_years, age):
    #     self.password = "bad_password"
    #     self.email = None
    #     self.is_active = True
    #
    #     self.dob = dob
    #     self.full_name = full_name
    #     self.country = country
    #     self.state = state
    #     self.number_of_education_years = number_of_education_years
    #     self.age = age
    #
    # def get_age(self):
    #     return self.age
    #
    # def set_age(self, new_password):
    #     self.password = new_password


valid_states = ("FL", "CA", "NY", "NC", "TX")
expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}

def calculate_expected_salary(number_of_experience_years,user_information, number_of_edu_years ):
    try:
        expected_salary = expected_salaries[users_info["state"].upper()]
        number_of_education_years_as_an_integer = int(number_of_edu_years)

    except KeyError:
        print(" INPUT ERROR: Please enter a valid state")
    except ValueError:
        print("***** INPUT ERROR: Please enter a vlaid number for years of learning experience")
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

        if len(users_coding_languages) < 3:
            new_expected_salary = new_expected_salary - 10000  # 65,000 - $10,000 = $55k
            print("Learn some more languages; deduct $10K form the expected salary.")
        elif len(users_coding_languages) > 3:
            new_expected_salary = new_expected_salary + 10000
        else:
            new_expected_salary = new_expected_salary + 5000
        if number_of_education_years_as_an_integer > 3:
            new_expected_salary = new_expected_salary + 10000
        else:
            new_expected_salary = new_expected_salary - 5000

            print("Expect $" + str(new_expected_salary) + " for your level of experience.")
            for state in expected_salaries:
                salary = expected_salaries[state]
                print("Your starting salary living in " + state + " could have been $" + str(salary) + ".")

# def create_unique_id(user_name):
#     random_id = id(user_name)
#     return random_id
create_a_candidate = True

while create_a_candidate:
    try:
        users_experience = input("How many years of experience do you have developing software?\n[1] Less than 1 year"
                                 "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
                                 "8+ years of experience \n")



        users_experience = int(users_experience)

        users_coding_languages = input("What languages do you know? (seperate by using commas)")

        if users_coding_languages == '':
            raise ValueError
        users_coding_languages = users_coding_languages.split(",")

        dob = input("Please enter you Date of Birth (MM/DD/YYYY)): \n")

        full_name = input("Please enter your full name: \n")

        age = input("Please enter your age: \n")

        country = input("Please enter your country: \n")

        for state in valid_states:
            print(state)

        state = input("Choose your state (use the 2 letter abbreviation): \n")

        is_active = True

        number_of_education_years = input("Please enter how many years you have been coding? \n")
# this is a dict
        users_info = {"dob": dob, "full_name": full_name, "country": country, "state": state, "is_active": is_active,
                      "number_of_education_years": number_of_education_years,
                      "age": int(age)}

        user_profile = UserProfile(dob, full_name, country, state, number_of_education_years, age)
        user_password = user_profile.get_password()
        print("Your initial password was", user_password)

        new_password = input("Enter your new password \n")

        user_profile.set_password(new_password)

        user_password = user_profile.get_password()

        print("Your new password is", new_password)

        user_id = user_profile.create_unique_id()
        print("Your conformation ID is", user_id)
        calculate_expected_salary(users_experience,users_info, number_of_education_years)

        another_candidate = input("Would you like to create another candidate? Y/N \n")

        if another_candidate == "Y":

            create_a_candidate
        else:
            create_a_candidate = False

    except ValueError:
        print("Please enter all valid values")


