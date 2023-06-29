DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'shop') THEN
        CREATE DATABASE shop;
    END IF;
END
$$;
