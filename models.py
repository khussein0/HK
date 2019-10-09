from app import db

class Machines(db.Model):
    __tablename__ = 'Machine'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    enabled = db.Column(db.Boolean)
    type = db.Column(db.String())

    def __init__(self, name, enabled, type):
        self.name = name
        self.enabled = enabled
        self.type = type

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'enabled': self.enabled,
            'type':self.type
        }

class Jobs(db.Model):
    __tablename__ = 'Job'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = nameS

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class Tasks(db.Model):
    __tablename__ = 'Task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    job_id = db.Column(db.Integer)
    sequence = db.Column(db.Integer)

    def __init__(self, name, job_id, sequence):
        self.name = name
        self.job_id = job_id
        self.sequence = sequence

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'job_id': self.job_id,
            'sequence': self.sequence
        }


class Tasks_queue(db.Model):
    __tablename__ = 'Task_queue'

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer)
    task_id = db.Column(db.Integer)
    status = db.Column(db.String())

    def __init__(self, machine_id, task_id, status):
        self.machine_id = machine_id
        self.task_id = task_id
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'machine_id': self.machine_id,
            'task_id': self.task_id,
            'status': self.status
        }
