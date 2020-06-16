# users_experience = input("How many years of experience do you have developing software?\n[1] Less than 1 year"
#                                  "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
#                                  "8+ years of experience \n")

# self represents the instance of the class. By using the “self” keyword we can
# access the attributes and methods of the class
# most class has getters and setters. If you want to update use set. If you want to get or call a class use get.
class UserProfile:

    def __init__(self, dob, full_name, country, state, number_of_education_years, age):
        self.password = "bad_password"
        self.email = None
        self.is_active = True

        self.dob = dob
        self.full_name = full_name
        self.country = country
        self.state = state
        self.number_of_education_years = number_of_education_years
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, new_password):
        self.password = new_password
