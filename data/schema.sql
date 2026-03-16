-- Basic schema for synthetic test database
CREATE TABLE users (
    id VARCHAR(50) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    disabled BOOLEAN DEFAULT FALSE
);

CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) REFERENCES users(id),
    name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'queued'
);

CREATE TABLE applications (
    id UUID PRIMARY KEY,
    user_id VARCHAR(50) REFERENCES users(id),
    position VARCHAR(100),
    status VARCHAR(20) DEFAULT 'draft'
);
