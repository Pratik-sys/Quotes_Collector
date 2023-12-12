from Quote.models import Quotes

# import responses


def test_get_quotes(client, app):
    response = client.get("/GetQ")
    with app.app_context():
        q = Quotes.objects.to_json()
        assert len(q) >= 2


def test_add_quotes(client, app):
    response = client.post(
        "/AddQ", data={"Title": "Unit Testing in Flask", "Author": "Flask"}
    )

    with app.app_context():
        # assert response.status_code == 200
        print(response.data)
        # assert str("Unit Testing in Flask") in response.data
