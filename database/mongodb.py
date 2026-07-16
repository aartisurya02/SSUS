from pymongo import MongoClient

try:
    MONGO_URI = "mongodb+srv://aartigsp25_db_user:Aarti9340@cluster0.cxq6s8d.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)

    client.andmin.command("ping")
    
    db = client["ssus1234"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_report"]

    print("MongoDB connected Successfully!")
except Exception as e:
    print("MongoDB error:",e)
