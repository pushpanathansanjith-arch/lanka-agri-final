import firebase_admin
from firebase_admin import credentials, firestore

# Connect to Firebase
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def update():
    # These are the new prices the robot will push
    market_data = [
        {"name": "Carrot", "price": "290", "center": "Dambulla", "trend": "up"},
        {"name": "Leeks", "price": "210", "center": "N'Eliya", "trend": "up"},
        {"name": "Green Chilli", "price": "380", "center": "Meegoda", "trend": "down"}
    ]
    
    for item in market_data:
        db.collection("market_prices").document(item['name']).set(item)
    
    print("Mass! Prices updated for the 8:00 AM Robot.")

if __name__ == "__main__":
    update()
