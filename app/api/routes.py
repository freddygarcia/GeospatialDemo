from flask_restx import Namespace, Resource
from .models import GroceryStore as Model
from .serializers import GroceryStoreRequest, GroceryStoreResponse, LatLng

api_namespace = Namespace('stores', description='Stores')

api_namespace.models['LatLng'] = LatLng
api_namespace.models['GroceryStoreRequest'] = GroceryStoreRequest
api_namespace.models['GroceryStoreResponse'] = GroceryStoreResponse


@api_namespace.route('/')
class GroceryStores(Resource):

    @api_namespace.marshal_with(GroceryStoreResponse, as_list=True)
    def get(self):
        return Model.get_all_stores()

    @api_namespace.marshal_with(GroceryStoreResponse)
    @api_namespace.expect(GroceryStoreRequest)
    def post(self):
        payload = api_namespace.payload

        point = Model.dict_to_point(payload['location'])

        store = Model(
            name=api_namespace.payload['name'],
            addr=api_namespace.payload['addr'],
            notes=api_namespace.payload['notes'],
            phone=api_namespace.payload['phone'],
            active=api_namespace.payload['active'],
            zipcode=api_namespace.payload['zipcode'],
            location=point
        )

        return Model.add_store(store)


@api_namespace.route('/<int:id>')
class GroceryStore(Resource):

    @api_namespace.marshal_with(GroceryStoreResponse)
    def get(self, id):
        store = Model.get_store(id)
        if store is None:
            return 'Not found', 404
        return store
