from flask import Flask, render_template, jsonify, json

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Bangalore',
        'salary'  :  '600000 lacs per annum'
    },
    {
        'id' : 2,
        'title' : 'Senior Analyst',
        'location' : 'Hyderabad',
        'salary'  :  '900000 lacs per annum'
    },
    {
        'id' : 3,
        'title' : 'Business Manager',
        'location' : 'Delhi',
        # 'salary'  :  '500000 lacs per annum'
    },
    {
        'id' : 4,
        'title' : 'Software Engineer',
        'location' : 'Chennai',
        'salary'  :  '800000 lacs per annum'
    },
]

@app.route("/")
def hellow_world():
    return render_template('home.html', jobs=JOBS, company_name="YD")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)