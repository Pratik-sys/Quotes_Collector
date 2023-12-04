from Quote.models import Quotes
import responses


def test_get_quotes(client, app):
    client.get("/GetQ")

    with app.app_context():
        q = Quotes.objects.to_json()
        assert len(q) != 0

def test_add_quotes(client, app):
    client.post("/AddQ")
    data = {"Title":"Testing test cases", "Author" : "pytest"}
    
    with app.app_context(): 
        q = Quotes(Title="Helloji", Author="Pratik")
        q.save()
        assert Quotes.objects(Title="Helloji").first()

