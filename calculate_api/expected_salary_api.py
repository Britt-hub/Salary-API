from flask import Flask
from flask import render_template
from flask import request
from calculate_api.utilities import calculator

app = Flask(__name__)  # Activate the flask application

import json


@app.route('/hello_world')
def hello_world():
    return 'Hello, Tribe!'


# export FLASK_ENV=development
# to run in local server type flask run in the terminal

@app.route('/')
def candidate_form():
    return render_template("index.html")


@app.route('/open-jobs')
def open_jobs():
    f = open("data.json", "r")  # Opens the file in read mode
    data_content = f.read()  # Read data from file & store in a var as raw txt
    jobs_as_json = json.loads(data_content)  # this will turn raw txt into a python object

    result_message = ""
    for job in jobs_as_json:  # this loops over the list of job dicts
        print(job)
        print(job["job_title"])
        print(job["location"])
        result_message = result_message + job["job_title"] + "\n"

    return render_template("result.html", message=result_message)

    return result_message


@app.route("/calculate_salary", methods=["POST"])
def calculate_salary():
    # capture the API request!!!
    if request.method == "POST":
        f = open("my_db.txt", "a")
        profession = request.form['profession']
        f.write("profession:" + profession)
        f.write("\n")

        number_of_experience_years = int(request.form['experience'])
        f.write("Year of Experience:" + str(number_of_experience_years))
        f.write("\n")

        languages = request.form['languages']
        users_coding_languages = languages.split(",")
        f.write("List of Coding Languages:" + str(users_coding_languages))
        f.write("\n")

        f.close()

        user_software_programs = request.form['designTools']
        user_software_programs = user_software_programs.split(",")

        dob = request.form['dob']
        full_name = request.form['fullName']

        age = int(request.form['age'])

        country = request.form['country']
        state = request.form['state']
        number_of_edu_years = int(request.form['educationYears'])

        is_developer = False
        is_designer = False

        if int(profession) == 1:
            is_developer = True
        else:
            is_designer = True

        users_info = {"dob": dob, "full_name": full_name, "number_of_experience_years": number_of_experience_years,
                      "country": country, "state": state, "is_active": True,
                      "number_of_education_years": number_of_edu_years,
                      "age": int(age)
                      }

        result_message = calculator.calculate_expected_salary(number_of_experience_years, users_info,
                                                              number_of_edu_years,
                                                              is_developer, is_designer, users_coding_languages,
                                                              user_software_programs)

        f = open("data.json", "r")
        file_content = f.read()

        final_message = result_message + "\n" + file_content + "\n"
        # The API response
        return render_template("result.html", message=final_message)

    else:

        return "Please submit a POST request."

# "a" means to append at the end of the file
