
CREATE TABLE disaster_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    population_density REAL,
    infrastructure_score REAL,
    previous_disasters INTEGER,
    alert_level REAL
);

INSERT INTO disaster_data (location, population_density, infrastructure_score, previous_disasters, alert_level)
VALUES ('Zone A', 900, 4.2, 2, 7.5),
       ('Zone B', 1200, 3.8, 5, 8.1),
       ('Zone C', 700, 4.6, 1, 6.9);
