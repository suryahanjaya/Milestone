import os
from config import db
from models import Milestones
from app import connex_app
from datetime import datetime

MILESTONES = [
    {'topic': 'FGD/Skill Test', 'achievement': 'Accepted as DnC Volunteer', 'description': 'Passed the FGD/Skill test in order to become batch 4 DnC Volunteer in Indonesia Youth Foundation', 'complete': False,},
    {'topic': 'Introduction to Backend Engineering', 'achievement': 'Finshing Final Project', 'description': 'Create CRUD to record Milestones API form using Flash & Swagger UI', 'complete': True,},
    {'topic': 'PTN', 'achievement': 'Successfully passed SNBP', 'description': 'Successfully passed the National Selection based on Achievement', 'complete': True,},
]

if os.path.exists('milestones.db'):
    os.remove('milestones.db')

with connex_app.app.app_context():
    db.create_all()

    for milestone_data in MILESTONES:
        m = Milestones(
            topic=milestone_data['topic'],
            achievement=milestone_data['achievement'],
            description=milestone_data['description'],
            complete=milestone_data['complete'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(m)

    db.session.commit()
