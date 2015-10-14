from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    # print github
    first, last, github = hackbright.get_student_by_github(github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)

    student_projects = hackbright.get_grades_by_github(github)

    return render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            projects=student_projects)


@app.route("/new-student-form")
def get_new_student_form():
    """Show the form that will be used to add new student."""
    return render_template("add_student.html")


@app.route("/student-add", methods=['POST'])
def make_student():
    """Make a new student and store it in database."""
    first = request.form.get('firstname')
    last = request.form.get('lastname')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)
    return render_template("new_student_confirmation.html", github=github)



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
