from flask import make_response, abort, jsonify
from models import Firms, FirmsSchema
from config import db

def read_firms():
    firms = Firms.query.order_by(Firms.firmName).all()
    firm_schema = FirmsSchema(many=True)
    data = firm_schema.dump(firms).data
    return data


def read1(fid):

    firm = Firms.query.filter(Firms.fid == fid).one_or_none()

    if firm is not None:

        firm_schema = FirmsSchema()
        data = firm_schema.dump(firm).data
        return data

    else:
        abort(
            404,
            "Firm not found for Id: {fid}".format(fid = fid),
        )


def create(firm):

    firmName = firm.get("firmName")
    existing_firm = (
        Firms.query.filter(Firms.firmName == firmName)
        .one_or_none()
    )

    if existing_firm is None:

        schema = FirmsSchema()
        new_firm = schema.load(firm, session=db.session).data

        db.session.add(new_firm)
        db.session.commit()

        data = schema.dump(new_firm).data
        return data, 201

    else:
        abort(
            409,
            "Person {firmName}  exists already".format(
                firmName = firmName
            ),
        )


def update(fid, firm):
    update_firm = Firms.query.filter(
        Firms.fid == fid
    ).one_or_none()

    if update_firm is not None:

        schema = FirmsSchema()
        update = schema.load(firm, session=db.session).data

        update.id = update_firm.fid

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_firm).data

        return data, 200

    else:
        abort(
            404,
            "Firm not found for Id: {fid}".format(fid = fid),
        )

def delete(fid):
    firm = Firms.query.filter(Firms.fid == fid).one_or_none()

    if firm is not None:
        db.session.delete(firm)
        db.session.commit()

        return jsonify(make_response(
            "Firm {fid} deleted".format(fid = fid)
        )), 200
        

    else:
        abort(
            404,
            "Firm not found for Id: {fid}".format(fid = fid),
        )





