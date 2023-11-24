from datetime import datetime
from config import db, ma
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Milestones(db.Model):
    __tablename__ = 'milestones'

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    achievement = Column(String)
    description = Column(String)
    complete = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class MilestonesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Milestones
        sqla_session = db.session


