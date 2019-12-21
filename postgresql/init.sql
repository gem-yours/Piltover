ALTER ROLE u_gem SET client_encoding TO 'utf8';
ALTER ROLE u_gem SET default_transaction_isolation TO 'read committed';
ALTER ROLE u_gem SET timezone TO 'Asia/Tokyo';
GRANT ALL PRIVILEGES ON DATABASE velkoz TO u_gem;