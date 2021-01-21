CREATE TABLE IF NOT EXISTS
    product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(120),
        price FLOAT,
        category VARCHAR(120),
        description TEXT,
        quantity INTEGER DEFAULT 0,
        active BOOLEAN DEFAULT TRUE
        );

INSERT INTO product(
                name,
                price,
                category,
                description,
                quantity)
        VALUES(
                "Flask",
                100.00,
                "Modules",
                "A microweb framework",
                100);
