DROP TABLE IF EXISTS documentation

CREATE TABLE documentation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pid INTEGER,
    title TEXT,
    content TEXT,
    FOREIGN KEY(pid) REFERENCES documentation(id)
)
