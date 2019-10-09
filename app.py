import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Machines, Jobs, Tasks, Tasks_queue

@app.route("/")
def hello():
    return render_template("homepage.html")

@app.route("/api/machines")
def get_all():
    try:
        machines=Machines.query.all()
        jsonify([e.serialize() for e in machines])
        return render_template("machines.html", machines=machines)
    except Exception as e:
	    return(str(e))
	
    
    
@app.route("/api/job/<id_>")
def get_by_id(id_):
    try:
        jobs=Jobs.query.filter_by(id=id_).all()
        jsonify([e.serialize() for e in jobs])
        return render_template("jobs.html", jobs=jobs)
    except Exception as e:
	    return(str(e))

@app.route("/add")
def add_job():
    name=request.args.get('name')
    try:
        job=Jobs(
            name=name
        )
        db.session.add(job)
        db.session.commit()
        return "Job added. job id={}".format(job.id)
    except Exception as e:
	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_job_form():
    if request.method == 'POST':
        name=request.form.get('name')
        try:
            job=Jobs(
                name=name
            )
            db.session.add(job)
            db.session.commit()
            return "Job added. job id={}".format(job.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

if __name__ == '__main__':
    app.run()
