from Quote.models import Quotes
import responses


def test_add_quotes(client, app):
    client.get("/AddQ")

    with app.app_context(): 
        q = Quotes(Title="Helloji", Author="Pratik")
        q.save()
        assert Quotes.objects(Title="Helloji").first()

