from flask_restx import Model, fields
from geoalchemy2.shape import to_shape


class Geometry(fields.Raw):

    def format(self, value):
        point = to_shape(value)
        return {
            'lat': point.y,
            'lng': point.x
        }


LatLng = Model('LatLng', {
    'lat': fields.Float(required=True),
    'lng': fields.Float(required=True)
})

GroceryStoreRequest = Model('GroceryStoreRequest', {
    'name': fields.String,
    'location': fields.Nested(LatLng),
    'addr': fields.String,
    'notes': fields.String,
    'phone': fields.Integer,
    'active': fields.Boolean,
    'zipcode': fields.Integer
})

GroceryStoreResponse = GroceryStoreRequest.clone('GroceryStoreResponse', {
    'id': fields.Integer,
    'location': Geometry
})
