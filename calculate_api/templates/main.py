#
# from calculate_api.templates.Models import Developer, Designer
#
# # def create_unique_id(user_name):
# #     random_id = id(user_name)
# #     return random_id
# create_a_candidate = True
# is_developer = False
# is_designer = False
#
# while create_a_candidate:
#     try:
#
#         candidate_type = input(
#             "What is your profession? \n Type '1' if you are a Developer \n Type '2' if you are a Designer.")
#
#         if int(candidate_type) == 1:
#             is_developer = True
#             is_designer = True
#             users_experience = input(
#                 "How many years of experience do you have developing software?\n[1] Less than 1 year"
#                 "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
#                 "8+ years of experience \n")
#         elif int(candidate_type) == 2:
#             is_designer = True
#             is_designer = False
#             users_experience = input(
#                 "How many years of experience do you have designing?\n[1] Less than 1 year"
#                 "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
#                 "8+ years of experience \n")
#         else:
#             raise ValueError
#
#         users_experience = int(users_experience)
#
#         if is_developer:
#             users_coding_languages = input("What languages do you know? (seperate by using commas) \n")
#
#             if users_coding_languages == '':
#                 raise ValueError
#
#             users_coding_languages = users_coding_languages.split(",")
#
#         else:
#             user_software_programs = input("What software design tools do you use? (separate by using commas)")
#
#         if is_designer:
#             user_software_programs = input ("What software programs (design tools) do you know? (seperate by using commas) \n")
#
#             if user_software_programs == ',':
#                 raise ValueError
#
#             user_software_programs = user_software_programs.split(",")
#
#         dob = input("Please enter you Date of Birth (MM/DD/YYYY)): \n")
#
#         full_name = input("Please enter your full name: \n")
#
#         age = input("Please enter your age: \n")
#
#         country = input("Please enter your country: \n")
#
#         for state in valid_states:
#             print(state)
#
#         state = input("Choose your state (use the 2 letter abbreviation): \n")
#
#         is_active = True
#
#         number_of_education_years = input("Please enter how many years you have been learning this skill set? \n")
#
#         # this is a dict
#         users_info = {"dob": dob, "full_name": full_name, "country": country, "state": state, "is_active": is_active,
#                       "number_of_education_years": number_of_education_years,
#                       "age": int(age)}
#
#         # if is_developer:
#         #     user_profile = Developer(dob, full_name, country, state, number_of_education_years, age, users_coding_languages)
#         #
#         # elif is_designer:
#         #     user_profile = Designer(dob, full_name, country, state, number_of_education_years, age, user_software_programs)
#         #
#         # # user_profile = UserProfile(dob, full_name, country, state, number_of_education_years, age)
#         # user_password = user_profile.get_password()
#         # print("Your initial password was", user_password)
#         #
#         # new_password = input("Enter your new password \n")
#         #
#         # user_profile.set_password(new_password)
#         #
#         # user_password = user_profile.get_password()
#         #
#         # print("Your new password is", new_password)
#         #
#         # user_id = user_profile.create_unique_id()
#         # print("Your conformation ID is", user_id)
#
#         calculate_expected_salary(users_experience, users_info, number_of_education_years, is_developer, is_designer)
#
#         another_candidate = input("Would you like to create another candidate? Y/N \n")
#
#         if another_candidate == "Y":
#
#             create_a_candidate
#         else:
#             create_a_candidate = False
#             print("Thank you for sharing this information. We will be in touch!")
#
#     except ValueError:
#         print("Please enter all valid values")
#
#
