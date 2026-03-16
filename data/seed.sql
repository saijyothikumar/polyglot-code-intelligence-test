INSERT INTO users (id, email, password_hash, disabled) VALUES
  ('alice', 'alice@example.com', 'hash123', false),
  ('bob', 'bob@example.com', 'hash456', false),
  ('carol', 'carol@example.com', 'hash789', true);

INSERT INTO jobs (user_id, name, status) VALUES
  ('alice', 'email_receipt', 'done'),
  ('bob', 'cleanup', 'queued');

INSERT INTO applications (id, user_id, position, status) VALUES
  (gen_random_uuid(), 'alice', 'Engineer', 'submitted'),
  (gen_random_uuid(), 'bob', 'Designer', 'draft');
