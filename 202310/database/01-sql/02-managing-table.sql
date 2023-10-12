CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);

-- 테이블 생성

PRAGMA table_info('examples');

-- 테이블 구조 (sqlite3용)
-- cid -> 컴럼아이디

ALTER TABLE
    examples
ADD COLUMN 
    Country VARCHAR(50) NOT NULL DEFAULT 1;


ALTER TABLE
    examples
ADD COLUMN 
    Age INTEGER NOT NULL DEFAULT "";

ALTER TABLE
    examples
ADD COLUMN 
    Address VARCHAR(100) NOT NULL DEFAULT "";


ALTER TABLE
    examples
RENAME COLUMN
    Address TO PostCode;


ALTER TABLE
    examples
DROP COLUMN
    PostCode;

-- 이름 변경
ALTER TABLE examples
RENAME TO new_examples;

DROP TABLE new_examples;


CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL
);

PRAGMA table_info("articles");

INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('title1', 'content1', '2023-10-10'),
    ('title2', 'content2', '2023-10-10'),
    ('title3', 'content3', '2023-10-10');

INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('title4', 'content4', DATE());


UPDATE
    articles
SET
    title = '바뀌나??'
WHERE
    id = 1;

UPDATE
    articles
SET
    title = 'update title'
WHERE
    id = 3;

UPDATE
    articles
SET
    content = 'update content'
WHERE
    id = 3;


SELECT
    *
FROM
    articles
ORDER BY
    id DESC;


DELETE FROM
    articles
WHERE
    id < 3;


DELETE FROM
    albums
WHERE
    AlbumId = 5;


DELETE FROM
    articles
WHERE id IN (
    SELECT id
    FROM articles 
    ORDER BY createdAt
    LIMIT 2
);

CREATE TABLE contacts (
    PK INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL
);

PRAGMA table_info("contacts");


CREATE TABLE users (
    PK INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL,
    phoneNumber NOT NULL,
    gender INTEGER
    address NOT NULL DEFAULT "no address"
);


ALTER TABLE
    users
RENAME COLUMN
    phoneNumber TO number;

DROP TABLE users;

PRAGMA table_info("users");