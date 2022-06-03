import pytest
from flask import Flask
from app.api.models import GroceryStore
from app import create_app
from app.settings import TestingConfig

@pytest.fixture
def flask_app_mock():
    flask_app = create_app(TestingConfig())
    return flask_app


@pytest.fixture
def store_object_mock():
    store = GroceryStore()
    store.id = 1
    store.name = 'Test Store'
    store.addr = '123 Test St'
    store.phone = 1234567890
    store.notes = 'Test Notes'
    store.active = True
    store.zipcode = 12345
    store.location = GroceryStore.dict_to_point({'lat': 1.0, 'lng': 1.0})
    return store

@pytest.fixture
def get_all_stores_mock(mocker):
    mock = mocker.patch(
        'sqlalchemy.orm.query.Query.all',
        return_value=mocker.Mock()
    )
    return mock

@pytest.fixture
def get_one_store_mock(mocker, store_object_mock):
    mock = mocker.patch(
        'sqlalchemy.orm.query.Query.get',
        return_value=store_object_mock
    )
    return mock

@pytest.fixture
def add_store_mock(mocker, store_object_mock):
    mocker.patch(
        'sqlalchemy.orm.session.Session.add',
        return_value=None
    )
    mocker.patch(
        'sqlalchemy.orm.session.Session.commit',
        return_value=None
    )
    mocker.patch(
        'sqlalchemy.orm.session.Session.refresh',
        return_value=None
    )
