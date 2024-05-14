// Création de la base de données devops
db = db.getSiblingDB('devops');

// Insertion des données JSON dans la collection users de la base de données devops
db.users.insertMany([
  {
      "_id": 1,
      "firstName": "Alice",
      "lastName": "Smith",
      "age": 25,
      "email": "alice.smith@example.com"
  },
  {
      "_id": 2,
      "firstName": "Bob",
      "lastName": "Johnson",
      "age": 35,
      "email": "bob.johnson@example.com"
  },
  {
      "_id": 3,
      "firstName": "Emma2",
      "lastName": "Brown",
      "age": 28,
      "email": "emma.brown@example.com"
  }
]);
