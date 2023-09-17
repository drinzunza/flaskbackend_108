import pymongo
import certifi

developer = {
    "first": "Sergio",
    "last": "Inzunza",
    "age": 37,
    "email": "sinzunza@sdgku.edu",
    "hobbies": ["code", "fishing"],
    "address": {
        "num": 741,
        "street": "evergreen",
        "city": "springfield"
    }
}




con_str = "mongodb+srv://ch40:Test1234@cluster0.uhdn1af.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("organika")