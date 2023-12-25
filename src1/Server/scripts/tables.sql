CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);
CREATE TABLE users(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Password VARCHAR(255),
    Role INTEGER,
    FOREIGN KEY(Role)
        REFERENCES posts(id)
            ON DELETE NO ACTION
);
CREATE TABLE Events (
    EventID INTEGER PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Date VARCHAR(50) NOT NULL,
    Time VARCHAR(50) NOT NULL,
    Location VARCHAR(255) NOT NULL,
    TicketPrice DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Tickets (
    TicketID INTEGER PRIMARY KEY,
    EventID INT REFERENCES Events(EventID),
    UserID INT REFERENCES Users(UserID),
    Status VARCHAR(20) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Artists (
    ArtistID INTEGER PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Genre VARCHAR(100) NOT NULL,
    ContractDetails VARCHAR(255) NOT NULL
);
CREATE TABLE Admins (
    AdminID INT PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    AdditionalAdminData VARCHAR(255) NOT NULL
);
CREATE TABLE SalesManagers (
    ManagerID INTEGER PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    AdditionalManagerData VARCHAR(255) NOT NULL
);
CREATE TABLE EventOrganizers (
    OrganizerID INTEGER PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    AdditionalOrganizerData VARCHAR(255) NOT NULL
);
CREATE TABLE SupportTeam (
    SupportID INTEGER PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    AdditionalSupportData VARCHAR(255) NOT NULL
);
CREATE TABLE Reviews (
    ReviewID INTEGER PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    EventID INT REFERENCES Events(EventID),
    Text VARCHAR(255) NOT NULL,
    Rating INT NOT NULL
);
CREATE TABLE SalesStatistics (
    StatID INTEGER PRIMARY KEY,
    EventID INT REFERENCES Events(EventID),
    Date VARCHAR(50) NOT NULL,
    TicketsSold INT NOT NULL,
    Revenue DECIMAL(10, 2) NOT NULL
);
CREATE TABLE concert_venues (
    concert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);
