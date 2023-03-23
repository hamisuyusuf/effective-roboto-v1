from flask import Flask, render_template, jsonify

app = Flask(__name__ ,static_url_path='/static')

JOBS = [
  {
    'id' : 1,
    'title': 'Data Scienticst',
    'location': 'Abuja',
    'salary': '120,000.000'
  },
   {
    'id' : 2,
    'title': 'Data Analyst',
    'location': 'Abuja',
    'salary': '80,000.000'
  },
 {
    'id' : 3,
    'title': 'Network Engineer',
    'location': 'Remote',
    'salary': '75,000.000'
  },
 {
    'id' : 4,
    'title': 'Product Designer',
    'location': 'Abuja',
    'salary': '70,000.000'
  }
]

@app.route("/")
def hello():
    return render_template('Home.html', 
                           jobs=JOBS,
                          company_name='nRyde')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
