-- users Table:
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    userpass varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

-- workout_tracker Table:
CREATE TABLE IF NOT EXISTS workout_tracker (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    workout_date date NOT NULL,
    workout varchar(50) NOT NULL,
    calories int NOT NULL,
    PRIMARY KEY (id)
);

-- meal_tracker Table:
CREATE TABLE IF NOT EXISTS meal_tracker (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    meal_date date NOT NULL,
    meal varchar(50) NOT NULL,
    calories int NOT NULL,
    PRIMARY KEY (id)
);