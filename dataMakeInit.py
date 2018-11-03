import os
from models import Firms
from config import db

Firms_some = [
    { "firmName": "MS"},
    { "firmName": "GS"},
]

dbPath = "./data/firms.db"
if os.path.exists(dbPath):
    os.remove(dbPath)

db.create_all()

for firm in Firms_some:
    f = Firms(firmName=firm.get("firmName"))
    db.session.add(f)

db.session.commit()
