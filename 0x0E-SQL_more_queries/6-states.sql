-- script to create a database and its states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);