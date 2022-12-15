CREATE TABLE users (
    Username TEXT PRIMARY KEY,
    Password TEXT NOT NULL
);

INSERT INTO users (Username, Password) 
VALUES ("AdminLogin", "45961da9ce13da68788eac0836edf79c1a0b510746b26bb471acf8c53a9dd63e");

SELECT * FROM users;