from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Data Scientist",
        'location': 'Bengaluru, India',
        'salary': '10,00,000'
    },
    {
        'id': 2,
        'title': "Data Analyst",
        'location': 'Pune, India',
        'salary': '8,00,000'
    },
    {
        'id': 3,
        'title': "Python Developer",
        'location': 'Hyderabad, India'
    },
    {
        'id': 4,
        'title': "ML Engineer",
        'location': 'Delhi, India',
        'salary': '15,00,000'
    }
]

@app.route("/")
def helloworld():
    return render_template("home.html", 
                           jobs=JOBS,
                           company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) # '0.0.0.0' is used to run local and debug to True for running continuously
