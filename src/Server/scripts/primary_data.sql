
INSERT INTO clients (Name, Email, Password, Role)
VALUES
    ('John Doe', 'password123', 'password123', 1),
    ('Jane Smith', 'jane.smith@example.com', 'securepass', 0);

INSERT INTO Events (EventID, Name, Date, Time, Location, TicketPrice)
VALUES
    (1, 'Concert 2023', '2023-05-15', '19:30', 'Concert Hall', 29.99),
    (2, 'Festival 2023', '2023-07-20', '15:00', 'Outdoor Venue', 49.99);


INSERT INTO Tickets (TicketID, EventID, UserID, Status, Price)
VALUES
    (1, 1, 1, 'Booked', 29.99),
    (2, 2, 2, 'Confirmed', 49.99);


INSERT INTO Artists (ArtistID, Name, Genre, ContractDetails)
VALUES
    (1, 'Artist 1', 'Pop', 'details for Artist 1'),
    (2, 'Artist 2', 'Rock', 'details for Artist 2');

INSERT INTO concert_venues (concert_id, name, location)
VALUES
    (1, 'Venue 1', 'Location 1'),
    (2, 'Venue 2', 'Location 2'),
    (3, 'Venue 3', 'Location 3');

INSERT INTO users(login, password, post_id)
VALUES ('admin', 'admin', 1);

INSERT INTO posts(name)
VALUES('Администратор'), ('Менеджер'), ('Посетитель');

