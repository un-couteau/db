CREATE TABLE IF NOT EXISTS items
(
    product_id  SERIAL PRIMARY KEY,
    name        VARCHAR(255)   NOT NULL,
    description TEXT,
    price       DECIMAL(10, 2) NOT NULL,
    image_url   VARCHAR(255)   NOT NULL,
    created_at  TIMESTAMP      NOT NULL DEFAULT NOW()
);
