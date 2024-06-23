from pymongo import MongoClient, errors

class CRUD:
    """CRUD operations for a specified MongoDB collection."""

    def __init__(self, user, password, host, port, db_name, collection_name):
        """Initialize the MongoClient and access the MongoDB databases and collections."""
        try:
            self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
            print("MongoDB connection established.")
        except errors.ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")

    def create(self, document):
        """Insert a document into the specified MongoDB collection."""
        if document is not None and isinstance(document, dict):
            try:
                self.collection.insert_one(document)
                return True
            except Exception as e:
                print(f"An error occurred while inserting data: {e}")
                return False
        else:
            print("Invalid document. Please provide a dictionary.")
            return False

    def read(self, query):
        """Query for documents in the specified MongoDB collection."""
        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                return list(cursor) if cursor else []
            except Exception as e:
                print(f"An error occurred while querying data: {e}")
                return []
        else:
            print("Invalid query. Please provide a dictionary.")
            return []

    def update(self, query, new_values):
        """Update documents in the specified MongoDB collection."""
        if query is not None and isinstance(query, dict) and new_values is not None and isinstance(new_values, dict):
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred while updating data: {e}")
                return 0
        else:
            print("Invalid input. Please provide dictionaries for query and new values.")
            return 0

    def delete(self, query):
        """Delete documents from the specified MongoDB collection."""
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred while deleting data: {e}")
                return 0
        else:
            print("Invalid query. Please provide a dictionary.")
            return 0

# Example usage:
if __name__ == "__main__":
    USER = 'aacuser'
    PASS = 'SNHU1234'
    HOST = 'nv-desktop-services.apporto.com'
    PORT = 31111
    DB = "AAC"
    COL = 'animals'

    crud = CRUD(USER, PASS, HOST, PORT, DB, COL)
    
    # Example of creating multiple documents with latitude and longitude
    new_animals = [
        {"age_upon_outcome": "1 year",
         "animal_id": "A812350",
         "breed": "Labrador Retriever Mix", 
         "color": "Black/White",
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Female", 
         "name": "Bella", 
         "location_lat": 30.75, 
         "location_long": -97.48},
        
        {"age_upon_outcome": "2 years", 
         "animal_id": "A812351", 
         "breed": "German Shepherd", 
         "color": "Brown/Black", 
         "date_of_birth": "2018-01-01", 
         "datetime": "2020-02-10 16:30:00",
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Max", 
         "location_lat": 30.76,
         "location_long": -97.49},
        
        {"age_upon_outcome": "3 years",
         "animal_id": "A812352", 
         "breed": "Doberman Pinscher", 
         "color": "Black/Tan", 
         "date_of_birth": "2017-01-01", 
         "datetime": "2020-03-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Rocky", 
         "location_lat": 30.77,
         "location_long": -97.50},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812353", 
         "breed": "Golden Retriever", 
         "color": "Golden", 
         "date_of_birth": "2019-01-01", 
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male",
         "name": "Buddy", 
         "location_lat": 30.78, 
         "location_long": -97.51},
        
        {"age_upon_outcome": "2 years",
         "animal_id": "A812354",
         "breed": "Bloodhound", 
         "color": "Brown",
         "date_of_birth": "2018-01-01", 
         "datetime": "2020-02-10 16:30:00",
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male",
         "name": "Duke", 
         "location_lat": 30.79, 
         "location_long": -97.52},
        
        {"age_upon_outcome": "1 year", 
         "animal_id": "A812355", 
         "breed": "Alaskan Malamute",
         "color": "Gray/White", 
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Female",
         "name": "Luna", 
         "location_lat": 30.80, 
         "location_long": -97.53},
        
        {"age_upon_outcome": "3 years",
         "animal_id": "A812356",
         "breed": "Siberian Husky",
         "color": "White/Gray", 
         "date_of_birth": "2017-01-01", 
         "datetime": "2020-03-10 16:30:00",
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male",
         "name": "Zeus",
         "location_lat": 30.81, 
         "location_long": -97.54},
        
        {"age_upon_outcome": "4 years", 
         "animal_id": "A812357",
         "breed": "Old English Sheepdog", 
         "color": "Gray/White", 
         "date_of_birth": "2016-01-01", 
         "datetime": "2020-04-10 16:30:00",
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male", 
         "name": "Oscar", 
         "location_lat": 30.82,
         "location_long": -97.55},
        
        {"age_upon_outcome": "1 year", 
         "animal_id": "A812358", 
         "breed": "Chesapeake Bay Retriever", 
         "color": "Brown", 
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Female",
         "name": "Sadie", 
         "location_lat": 30.83, 
         "location_long": -97.56},
        
        {"age_upon_outcome": "2 years",
         "animal_id": "A812359", 
         "breed": "Newfoundland",
         "color": "Black", 
         "date_of_birth": "2018-01-01", 
         "datetime": "2020-02-10 16:30:00",
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Female",
         "name": "Molly", 
         "location_lat": 30.84, 
         "location_long": -97.57},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812360", 
         "breed": "Rottweiler", 
         "color": "Black/Tan",
         "date_of_birth": "2019-01-01", 
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Bear", 
         "location_lat": 30.85, 
         "location_long": -97.58},
        
        {"age_upon_outcome": "2 years", 
         "animal_id": "A812361", 
         "breed": "German Shepherd", 
         "color": "Black/Tan", 
         "date_of_birth": "2018-01-01", 
         "datetime": "2020-02-10 16:30:00",
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male",
         "name": "Toby",
         "location_lat": 30.86, 
         "location_long": -97.59},
        
        {"age_upon_outcome": "3 years",
         "animal_id": "A812362",
         "breed": "Labrador Retriever Mix",
         "color": "Yellow",
         "date_of_birth": "2017-01-01", 
         "datetime": "2020-03-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Female", 
         "name": "Ruby",
         "location_lat": 30.87,
         "location_long": -97.60},
        
        {"age_upon_outcome": "4 years", 
         "animal_id": "A812363", 
         "breed": "Golden Retriever",
         "color": "Golden", 
         "date_of_birth": "2016-01-01",
         "datetime": "2020-04-10 16:30:00",
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male",
         "name": "Cooper",
         "location_lat": 30.88, 
         "location_long": -97.61},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812364", 
         "breed": "Bloodhound",
         "color": "Black/Tan",
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male",
         "name": "Hunter",
         "location_lat": 30.89, 
         "location_long": -97.62},
        
        {"age_upon_outcome": "2 years", 
         "animal_id": "A812365",
         "breed": "Alaskan Malamute", 
         "color": "Gray/White",
         "date_of_birth": "2018-01-01",
         "datetime": "2020-02-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Female", 
         "name": "Daisy",
         "location_lat": 30.90,
         "location_long": -97.63},
        
        {"age_upon_outcome": "3 years", 
         "animal_id": "A812366",
         "breed": "Siberian Husky",
         "color": "White/Black", 
         "date_of_birth": "2017-01-01",
         "datetime": "2020-03-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male",
         "name": "Riley",
         "location_lat": 30.91, 
         "location_long": -97.50},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812350", 
         "breed": "Labrador Retriever Mix",
         "color": "Black/White", 
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Female",
         "name": "Bella",
         "location_lat": 30.75, 
         "location_long": -97.48},
        
        {"age_upon_outcome": "2 years", 
         "animal_id": "A812351", 
         "breed": "German Shepherd", 
         "color": "Brown/Black", 
         "date_of_birth": "2018-01-01",
         "datetime": "2020-02-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Max", 
         "location_lat": 30.76, 
         "location_long": -97.49},
        
        {"age_upon_outcome": "3 years",
         "animal_id": "A812352", 
         "breed": "Doberman Pinscher",
         "color": "Black/Tan", 
         "date_of_birth": "2017-01-01",
         "datetime": "2020-03-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male", 
         "name": "Rocky",
         "location_lat": 30.77, 
         "location_long": -97.50},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812353", 
         "breed": "Golden Retriever", 
         "color": "Golden",
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male",
         "name": "Buddy", 
         "location_lat": 30.78, 
         "location_long": -97.51},
        
        {"age_upon_outcome": "2 years",
         "animal_id": "A812354",
         "breed": "Bloodhound", 
         "color": "Brown", 
         "date_of_birth": "2018-01-01",
         "datetime": "2020-02-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male", 
         "name": "Duke", 
         "location_lat": 30.79, 
         "location_long": -97.52},
        
        {"age_upon_outcome": "1 year", 
         "animal_id": "A812355", 
         "breed": "Alaskan Malamute",
         "color": "Gray/White", 
         "date_of_birth": "2019-01-01", 
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Female", 
         "name": "Luna", "location_lat": 30.80, 
         "location_long": -97.53},
        
        {"age_upon_outcome": "3 years", 
         "animal_id": "A812356", 
         "breed": "Siberian Husky",
         "color": "White/Gray", 
         "date_of_birth": "2017-01-01", 
         "datetime": "2020-03-10 16:30:00",
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Zeus",
         "location_lat": 30.81, 
         "location_long": -97.54},
        
        {"age_upon_outcome": "4 years",
         "animal_id": "A812357", 
         "breed": "Old English Sheepdog", 
         "color": "Gray/White", 
         "date_of_birth": "2016-01-01",
         "datetime": "2020-04-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male",
         "name": "Oscar", 
         "location_lat": 30.82, 
         "location_long": -97.55},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812358", 
         "breed": "Chesapeake Bay Retriever", 
         "color": "Brown", 
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00",
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Female", 
         "name": "Sadie", 
         "location_lat": 30.83, 
         "location_long": -97.56},
        
        {"age_upon_outcome": "2 years",
         "animal_id": "A812359",
         "breed": "Newfoundland",
         "color": "Black", 
         "date_of_birth": "2018-01-01",
         "datetime": "2020-02-10 16:30:00",
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Female",
         "name": "Molly",
         "location_lat": 30.84,
         "location_long": -97.57},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812360", 
         "breed": "Rottweiler", 
         "color": "Black/Tan",
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male", 
         "name": "Bear", 
         "location_lat": 30.85,
         "location_long": -97.58},
        
        {"age_upon_outcome": "2 years", 
         "animal_id": "A812361", 
         "breed": "German Shepherd", 
         "color": "Black/Tan",
         "date_of_birth": "2018-01-01",
         "datetime": "2020-02-10 16:30:00",
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Toby", 
         "location_lat": 30.86, 
         "location_long": -97.59},
        
        {"age_upon_outcome": "3 years",
         "animal_id": "A812362", 
         "breed": "Labrador Retriever Mix", 
         "color": "Yellow", 
         "date_of_birth": "2017-01-01", 
         "datetime": "2020-03-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Female", 
         "name": "Ruby", "location_lat": 30.87, 
         "location_long": -97.60},
        
        {"age_upon_outcome": "4 years", 
         "animal_id": "A812363", 
         "breed": "Golden Retriever",
         "color": "Golden", 
         "date_of_birth": "2016-01-01", 
         "datetime": "2020-04-10 16:30:00",
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Male",
         "name": "Cooper", 
         "location_lat": 30.88, 
         "location_long": -97.61},
        
        {"age_upon_outcome": "1 year",
         "animal_id": "A812364",
         "breed": "Bloodhound", 
         "color": "Black/Tan", 
         "date_of_birth": "2019-01-01",
         "datetime": "2020-01-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Hunter", 
         "location_lat": 30.89, 
         "location_long": -97.62},
        
        {"age_upon_outcome": "2 years", 
         "animal_id": "A812365", 
         "breed": "Alaskan Malamute",
         "color": "Gray/White",
         "date_of_birth": "2018-01-01", 
         "datetime": "2020-02-10 16:30:00", 
         "outcome_type": "Adoption",
         "sex_upon_outcome": "Intact Female", 
         "name": "Daisy",
         "location_lat": 30.90,
         "location_long": -97.63},
        
        {"age_upon_outcome": "3 years", 
         "animal_id": "A812366", 
         "breed": "Siberian Husky", 
         "color": "White/Black", 
         "date_of_birth": "2017-01-01", 
         "datetime": "2020-03-10 16:30:00", 
         "outcome_type": "Adoption", 
         "sex_upon_outcome": "Intact Male", 
         "name": "Riley", 
         "location_lat": 30.91, 
         "location_long": -97.55},
    ]

    for animal in new_animals:
        result = crud.create(animal)
        print(f"Insert successful for {animal['animal_id']}: {result}")

    # Example of reading documents
    query = {"animal_id": {"$in": ["A812350", "A812351", "A812352", "A812353", "A812354", "A812355", "A812356", "A812357", "A812358", "A812359", "A812360", "A812361", "A812362", "A812363", "A812364", "A812365", "A812366", "A812367"]}}
    animals = crud.read(query)
    print("Query result:", animals)