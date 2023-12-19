from pymongo import MongoClient
from bson.objectid import ObjectId


    
class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:46725/AAC' %("aacuser", "password"))
        self.database = self.client['AAC']
        print ("Connection successful")

    # Complete this create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            if insert!=0:
                return True
            else:
                return False    
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
            
    # Complete this create method to implement the R in CRUD
    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id":False})
            
        else:
            data = self.database.animals.find({}, {"_id":False})
            
        return data
        
            
    
    # Create a method to implment U in CRUD
    def update(self, search, data):
        if search is not None:
            result = self.database.animals.update_many(search, {"$set": data})
        else:
            return "{}"
        #returning result 
        return result.modified_count
    
    # Create a mthod to implment D in CRUD
    
    def delete(self, delete):
        if delete is not None:
            result = self.database.animals.delete_many(delete)
        else:
            return "{}"
        #returning result 
        return result.deleted_count
