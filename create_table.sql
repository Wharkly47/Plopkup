-- create_table.sql

-- Assurez-vous d'utiliser le bon chemin si nécessaire
ATTACH DATABASE 'phone_data.db' AS db;

-- Création de la table
CREATE TABLE IF NOT EXISTS db.phone_data (
    id INTEGER PRIMARY KEY,
    phone_number TEXT,
    name TEXT,
    address TEXT
);

-- Détacher la base de données
DETACH DATABASE db;