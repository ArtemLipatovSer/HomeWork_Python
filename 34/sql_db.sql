create table if not exists posts(
    id integer primary key autoincrement,
    title text not null,
    author text not null,
    url text not null,
    textPost text not null
);

--DELETE FROM posts;
--UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'posts';
