# ask the user to input their experience.
# use an if/else/elif statement to check if the user chose option 1,2,3,4
# else if the


users_experience = input("How many years of experience do you have developing software?\n[1] Less than 1 year" 
                         "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
                          "8+ years of experience \n")

users_experience = int(users_experience)

users_coding_languages = input("What languages do you know?")
print("Before Split():" + users_coding_languages)

users_coding_languages = users_coding_languages.split(",")
print("After Split():" + str(users_coding_languages))

if users_experience == 1:
    print("Expect between $40,000 and $60,000 of your level of experience.")
    if len(users_coding_languages) < 3:
        print("Learn some more languages: deduct $10K form the expected salary.")

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

users_info = input("What is your date of birth?")


#users_info = int(users_info)


#print("DOB is: " + DOB)

#users_name = input("What is your name?")

#users_state = input("What is your state?")

#users_country = input("What is your country?")

user_isActive = input("If you are an active code type 1 if you are not type 2")

user_isActive_bool = user_isActive == "1"

print(user_isActive_bool)

# else:
#     print(10*"*" + "You must insert one of the value options." + 10*"*")

