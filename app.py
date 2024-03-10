from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# JOBS = [
#     {
#         'id': 1,
#         'title': "Data Scientist",
#         'location': 'Bengaluru, India',
#         'salary': '10,00,000'
#     },
#     {
#         'id': 2,
#         'title': "Data Analyst",
#         'location': 'Pune, India',
#         'salary': '8,00,000'
#     },
#     {
#         'id': 3,
#         'title': "Python Developer",
#         'location': 'Hyderabad, India'
#     },
#     {
#         'id': 4,
#         'title': "ML Engineer",
#         'location': 'Delhi, India',
#         'salary': '15,00,000'
#     }
# ]

@app.route("/")
def helloworld():
    JOBS = load_jobs_from_db()
    return render_template("home.html", 
                           jobs=JOBS,
                           company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)

@app.route("/job/<id>") # dynamic route
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    return render_template('jobpage.html', job=job, company_name="Jovian")

@app.route("/api/job/<id>") # dynamic route
def api_job(id):
    job = load_job_from_db(id)
    return jsonify(job)

@app.route("/job/<id>/apply")
def apply_to_job(id):
    data = request.args
    # Store to DB
    # Send an email
    # display acknowledgement
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) # '0.0.0.0' is used to run local and debug to True for running continuously
