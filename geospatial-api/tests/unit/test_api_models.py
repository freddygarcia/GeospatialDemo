from app.api.models import GroceryStore
from geoalchemy2.shape import to_shape


def test_parse_location_value():
    location_dict = {"lat": "40.7128", "lng": "-74.0060"}
    point = GroceryStore.dict_to_point(location_dict)

    assert to_shape(point).y == 40.7128
    assert to_shape(point).x == -74.0060


def test_store_to_string():
    store = GroceryStore()
    store.name = "Test Store"
    assert str(store) == '<GroceryStore id=None name=Test Store>'
    assert store.__repr__() == '<GroceryStore id=None name=Test Store>'
