import mongoengine

mongoengine.connect(
    db="Pollution",
    # username="root",
    # password="pollution4996",
    # authentication_source="admin",
    # host="localhost",
    # port=27017
)

class Incidents(mongoengine.Document):
    url = mongoengine.StringField(required=True)
    articleTitle = mongoengine.StringField(required=True)
    # eventDate = mongoengine.StringField(required=True)
    # chemicals = mongoengine.ListField(mongoengine.StringField(max_length=50))

    meta = {
        "indexes": ["articleTitle"],
        "ordering": ["date"]
    }

incident = Incidents(
    url="www.myUrl.com",
    articleTitle="article title"
).save()
