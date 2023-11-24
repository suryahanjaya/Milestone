from config import db
from models import Milestones, MilestonesSchema
from flask import request, jsonify  
from datetime import datetime

milestones_schema = MilestonesSchema()

def get_all():
    milestones = Milestones.query.all()
    data = milestones_schema.dump(milestones,many=True)
    return data

def get_single(id):
    milestone = Milestones.query.filter(Milestones.id == id).one_or_none()
    if milestone is not None:
        data = milestones_schema.dump(milestone)
        return data
    else :
        return jsonify({'error': f"Milestones with id: {id} not found"}), 404

def create():
    data = request.json
    milestone = Milestones(
        topic=data['topic'],
        achievement=data['achievement'],
        description=data['description'],
        complete=data['complete'],
    )
    db.session.add(milestone)
    db.session.commit()
    data = milestones_schema.dump(milestone)
    return data
    
def update(id):
    data = request.json
    milestone = Milestones.query.filter(Milestones.id == id).one_or_none()
    
    if milestone is not None:
        milestone.topic=data['topic']
        milestone.achievement=data['achievement']
        milestone.description=data['description']
        milestone.complete=data['complete']
        milestone.updated_at=datetime.utcnow()
        db.session.commit()
        data = milestones_schema.dump(milestone)
        return data
    else:
        return jsonify({'error': f"Milestones with id : {id} not found"}), 404

    
def delete(id):
    milestone = Milestones.query.filter(Milestones.id == id).one_or_none()
    if milestone is not None:
        db.session.delete(milestone)
        db.session.commit()
        data = milestones_schema.dump(milestone)
        return data
    else :
        return jsonify({'error': f"Milestones with id : {id} not found"}), 404