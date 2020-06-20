# users_experience = input("How many years of experience do you have developing software?\n[1] Less than 1 year"
#                                  "\n[2] 1-3 years of experience \n[3] 3-8 years of experience \n[4] "
#                                  "8+ years of experience \n")

# self represents the instance of the class. By using the “self” keyword we can
# access the attributes and methods of the class
# most class has getters and setters. If you want to update use set. If you want to get or call a class use get.
# class Product:
#     def __init__(self):
#         self.price = 0.0
#         self.description ="Some Product"

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

    def set_age(self, new_age):
        self.age = new_age

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email

    def create_unique_id(self):
        random_id = id(self.full_name)
        return random_id


class Developer(UserProfile):
    def __init__(self, dob, full_name, country, state, number_of_education_years, age):
        super().__init__(dob, full_name, country, state, number_of_education_years, age)


class Designer(UserProfile):
    def __init__(self, dob, full_name, country, state, number_of_education_years, age):
        super().__init__(dob, full_name, country, state, number_of_education_years, age)
