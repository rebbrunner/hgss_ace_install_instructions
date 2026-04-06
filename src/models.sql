DROP TABLE IF EXISTS documentation;

CREATE TABLE documentation (
    id SERIAL PRIMARY KEY,
    pid INTEGER NULL,
    title TEXT,
    content TEXT,
    FOREIGN KEY(pid) REFERENCES documentation(id) ON DELETE SET NULL
);
