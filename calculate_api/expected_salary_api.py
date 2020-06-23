from flask import Flask
from flask import render_template
from flask import request
from calculate_api.utility_functions import calculator

app = Flask(__name__)  # Activate the flask application


@app.route('/hello_world')
def hello_world():
    return 'Hello, Tribe!'


# export FLASK_ENV=development
# to run in local server type flask run in the terminal

@app.route('/')
def candidate_form():
    return render_template("index.html")


@app.route("/calculate_salary", methods=["POST"])
def calculate_salary():
    if request.method == "POST":
        profession = int(request.form["profession"])
        number_of_experience_years = int(request.form ["experience"])
        languages = request.form["languages"]
        users_coding_languages = languages.spilt(",")
        user_software_programs = request.form["designTools"]
        user_software_programs = user_software_programs.spilt(",")
        dob = request.form["dob"]
        full_name = request.form["fullName"]
        age = int(request.form["age"])
        country = request.form["country"]
        state = request.form["state"]
        number_of_education_years =int(request.form["educationYears"])

        is_developer = False
        is_designer = False

        if int(profession) == 1:
            is_developer = True
        else:
            is_designer = True

        users_info = {"dob": dob, "full_name": full_name, "country": country, "state": state, "is_active": True,
                      "number_of_education_years": number_of_education_years,
                      "age": int(age)}

        calculator.calculate_expected_salary(number_of_experience_years, users_info, number_of_education_years, is_developer, is_designer, users_coding_languages, user_software_programs)


    return "Thanks for submitting!"
