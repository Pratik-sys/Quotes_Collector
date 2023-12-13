from Quote.models import Quotes


def test_get_quotes(client, app):
    response = client.get("/GetQ")
    with app.app_context():
        q = Quotes.objects.to_json()
        assert len(q) >= 2
        assert response.status_code == 200


def test_add_quotes(client, app):
    response = client.post(
        "/AddQ", json={"title": "Unit Testing in Flask", "author": "Flask"}
    )
    assert response.json[0]["Msg"] == "Quote added"
    assert response.status_code == 200
