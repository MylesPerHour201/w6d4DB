CREATE TABLE users( 
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INT,
    gender TEXT,
    address TEXT,
);