CREATE TABLE IF NOT EXISTS orders
(
    order_id   SERIAL PRIMARY KEY,
    user_id    INTEGER REFERENCES users (user_id),
    price    INTEGER REFERENCES items (product_id),
    created_at TIMESTAMP   NOT NULL DEFAULT NOW(),
    status     VARCHAR(50) NOT NULL
);
