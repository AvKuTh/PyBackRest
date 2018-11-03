from datetime import datetime
from config import db, ma


class Firms(db.Model):
    __tablename__ = "Firms"
    fid = db.Column(db.Integer, primary_key=True)
    firmName = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class FirmsSchema(ma.ModelSchema):
    class Meta:
        model = Firms
        sqla_session = db.session
