from flask import Flask, render_template, jsonify, request
from database import dbhelper

app = Flask(__name__)

@app.route('/')
def home_page():
    db = dbhelper()
    job_list = db.fetch_data()
    return render_template('home.html', jobs=job_list, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    db = dbhelper()
    job_list = db.fetch_data()
    return jsonify(job_list)

@app.route('/job/<id>')
def job_page(id):
    db = dbhelper()
    job_details = db.fetch_job_data(id)
    return render_template('job_page.html', job=job_details)

@app.route('/job/<id>/application', methods=['POST'])
def application_request(id):
    data = request.form
    db = dbhelper()
    job_details = db.fetch_job_data(id)

    db.submit_application(id, data)

    return render_template('application_submitted.html', application=data, job=job_details)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)