-- disable foreign key constraint check
PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

-- WARN: DROP OLD SCHEMAS ONLY
-- DROP TABLE film_person;
-- DROP TABLE film_planet;
-- DROP TABLE film_species;
-- DROP TABLE film_starship;
-- DROP TABLE film_vehicle;

CREATE TABLE IF NOT EXISTS film_person(
    film_person_id INTEGER PRIMARY KEY,
    film_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY (film_id)
        REFERENCES film (film_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (person_id)
        REFERENCES person (person_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION --,
    -- PRIMARY KEY (film_id, person_id)
);

CREATE TABLE IF NOT EXISTS film_planet(
    film_planet_id INTEGER PRIMARY KEY,
    film_id INTEGER NOT NULL,
    planet_id INTEGER NOT NULL,
    FOREIGN KEY (film_id)
        REFERENCES film (film_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (planet_id)
        REFERENCES planet (planet_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION --,
    -- PRIMARY KEY (film_id, planet_id)
);

CREATE TABLE IF NOT EXISTS film_species(
    film_species_id INTEGER PRIMARY KEY,
    film_id INTEGER NOT NULL,
    species_id INTEGER NOT NULL,
    FOREIGN KEY (film_id)
        REFERENCES film (film_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (species_id)
        REFERENCES species (species_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION --,
    -- PRIMARY KEY (film_id, species_id)
);

CREATE TABLE IF NOT EXISTS film_starship(
    film_starship_id INTEGER PRIMARY KEY,
    film_id INTEGER NOT NULL,
    starship_id INTEGER NOT NULL,
    FOREIGN KEY (film_id)
        REFERENCES film (film_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (starship_id)
        REFERENCES starship (starship_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION --,
    -- PRIMARY KEY (film_id, starship_id)
);

CREATE TABLE IF NOT EXISTS film_vehicle(
    film_vehicle_id INTEGER PRIMARY KEY,
    film_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    FOREIGN KEY (film_id)
        REFERENCES film (film_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (vehicle_id)
        REFERENCES vehicle (vehicle_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION --,
    -- PRIMARY KEY (film_id, vehicle_id)
);

-- commit transaction
COMMIT;

-- enable foreign key constraint check
PRAGMA foreign_keys=on;
