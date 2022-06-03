
def test_get_stores_valid(
    flask_app_mock,
    get_all_stores_mock,
    store_object_mock
):
    """
    GIVEN a Flask application
    WHEN the '/stores' resource is requested (GET)
    THEN check the response is valid
    """
    # Create a test client using the Flask application configured for testing
    with flask_app_mock.test_client() as test_client:
        get_all_stores_mock.return_value = [store_object_mock]
        response = test_client.get('/stores/')
        assert response.status_code == 200
        assert response.json[0]['name'] == 'Test Store'


def test_get_store_valid(
    flask_app_mock,
    get_one_store_mock,
    store_object_mock
):
    """
    GIVEN a Flask application
    WHEN the '/stores/{id}' resource is requested (GET)
    THEN check the response is valid
    """
    # Create a test client using the Flask application configured for testing
    with flask_app_mock.test_client() as test_client:
        get_one_store_mock.return_value = store_object_mock
        response = test_client.get('/stores/1')
        assert response.status_code == 200
        assert response.json['name'] == 'Test Store'


def test_get_store_not_found(
    flask_app_mock,
    get_one_store_mock,
    store_object_mock
):
    """
    GIVEN a Flask application
    WHEN the '/stores/{id}' resource is requested (GET)
    THEN check the requested store is not found
    """
    # Create a test client using the Flask application configured for testing
    with flask_app_mock.test_client() as test_client:
        get_one_store_mock.return_value = None
        response = test_client.get('/stores/1')
        assert response.status_code == 404
        assert response.json['name'] is None


def test_post_store_valid(
    flask_app_mock,
    add_store_mock,
    store_object_mock
):
    """
    GIVEN a Flask application
    WHEN the '/stores/{id}' resource is requested (GET)
    THEN check the requested store is not found
    """
    # Create a test client using the Flask application configured for testing
    with flask_app_mock.test_client() as test_client:
        # add_store_mock.return_value = store_object_mock
        response = test_client.post('/stores/', json={
            'name': 'Test Store',
            'addr': '123 Test St',
            'location': {'lat': 1.0, 'lng': 1.0},
            'zipcode': 12345,
            'phone': 1234567890,
            'notes': 'Test Notes',
            'active': True
        })
        assert response.status_code == 200
        assert response.json['name'] == 'Test Store'
