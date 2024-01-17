-- @block

CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    email VARCHAR(255) NOT NULL UNIQUE,
    bio Text, 
    country VARCHAR(2)
);

-- @block

INSERT INTO Users (email, bio, country)
VALUES(
    'helloworld@gmail.com',
    'this is a string in the bio section!',
    'EG'
)

-- @block

INSERT INTO Users (email, bio, country)
VALUES
    ('x@gmail.com', 'text', 'US'),
    ('y@gmail.com','foo', 'UK'),
    ('test@gmail.com','bar','EG')
;

-- @block

SELECT email, id, country FROM Users
WHERE country = 'EG'
AND id = '1'
ORDER BY id ASC
limit 2;



-- @block
CREATE TABLE Rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR (255),
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Users(id)
);

--@block
INSERT INTO Rooms (owner_id, street) VALUES
(1,' street 1'),
(1,'street 2'),
(1,'street 3'),
(1, 'street 4');

--@block
SELECT * FROM Users
RIGHT JOIN Rooms 
ON Rooms.owner_id = Users.id;



