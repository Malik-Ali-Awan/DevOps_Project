CREATE DATABASE quotes;

\c quotes;

CREATE TABLE quotes (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL
); 