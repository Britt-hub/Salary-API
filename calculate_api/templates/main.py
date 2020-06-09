# ask the user to input their experience.
# use an if/else/elif statement to check if the user chose option 1,2,3,4
# else if the

valid_states = ("FL", "CA", "NY", "NC", "TX")
expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}

users_experience = input("How many years of experience do you have developing software?\n[1] Less than 1 year"
                         "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
                         "8+ years of experience \n")

users_experience = int(users_experience)

users_coding_languages = input("What languages do you know? (seperate by using commas)")

users_coding_languages = users_coding_languages.split(",")

dob = input("Please enter you Date of Birth (MM/DD/YYYY)): \n")

full_name = input("Please enter your full name: \n")

country = input("Please enter your country: \n")

print(valid_states[0])
print(valid_states[1])
print(valid_states[2])
print(valid_states[3])
print(valid_states[4])

state = input("Choose your state (use the 2 letter abbreviation): \n")

is_active = True

number_of_education_years = input("Please enter how many years you have been coding? \n")

users_info = {"dob": dob, "full_name": full_name, "country": country, "state": state, "is_active": is_active,
              "number_of_education_years": number_of_education_years}

if users_experience == 1:
    # FIRST WE WILL TRY SOME CODE. IF IT DOESN'T WORK THEN WE WILL TRY THIS CODE'
    try:
        expected_salary = expected_salaries[users_info["state"]]
    except KeyError:
        print(" INPUT ERROR: Please enter a valid state")
    else:

        new_expected_salary = expected_salary - 5000  # 70,000 - 5,000 = $65,000

        if len(users_coding_languages) < 3:
            new_expected_salary = new_expected_salary - 10000  # 65,000 - $10,000 = $55k
            print("Learn some more languages; deduct $10K form the expected salary.")
        elif len(users_coding_languages) > 3:
            new_expected_salary = new_expected_salary + 10000
        else:
            new_expected_salary = new_expected_salary + 5000
        if int(number_of_education_years) > 3:
            new_expected_salary = new_expected_salary + 5000
        else:
            new_expected_salary = new_expected_salary - 5000
            print("Expect $" + str(new_expected_salary) + " for your level of experience.")


elif users_experience == 2:
    print("Expect between $60,000 and $80,000 of your level of experience.")
    if len(users_coding_languages) < 3:
        print("Learn some more languages: deduct $5K form the expected salary.")
    elif len(users_coding_languages) > 5:
        print("You're in good shape!")

elif users_experience == 3:
    print("Expect between $80,000 and $120,000 for your level of experience.")
    if len(users_coding_languages) < 3:
        print("Learn some more languages: deduct $2K form the expected salary.")
    elif len(users_coding_languages) > 5:
        print("You're in good shape!")


elif users_experience == 4:
    print("Expect between $130,000 for your level of experience.")
    if len(users_coding_languages) < 3:
        print("Learn some more languages: deduct $1K form the expected salary.")
    elif len(users_coding_languages) > 5:
        print("You're in good shape!")

# users_info = input("What is your date of birth?")


# users_info = int(users_info)


# print("DOB is: " + DOB)

# users_name = input("What is your name?")

# users_state = input("What is your state?")

# users_country = input("What is your country?")

# user_isActive = input("If you are an active code type 1 if you are not type 2")
#
# user_isActive_bool = user_isActive == "1"
#
# print(user_isActive_bool)

# else:
#     print(10*"*" + "You must insert one of the value options." + 10*"*")

