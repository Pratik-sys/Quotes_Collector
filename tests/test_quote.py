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

def test_update_quotes(client, app):
    response = client.put("/6579b1a7e8a77841ecd75f72/UpdateQ", json={"title" : "test case to update", "author":"pratik"})
    assert response.json[0]["Msg"] == "Quote is updated" 
    assert response.status_code == 200

def test_delete_quotes(client, app):
    response = client.delete("/6579b2a9a779266718a9be6d/DelQ")
    print(response.json)
    assert response.json["Msg"] == "Quote with 6579b2a9a779266718a9be6d deleted"
    assert response.status_code == 200