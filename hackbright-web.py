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
    return render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
@app.route("/new-student")
def make_student():
    """Make a new student and store it in database."""
    first = request.args.get('first')
    last = request.args.get('last')
    github = request.args.get('github')
    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
