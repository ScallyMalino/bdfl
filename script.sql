CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role VARCHAR(50) NOT NULL
);
CREATE TABLE Events (
    EventID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Location VARCHAR(255) NOT NULL,
    TicketPrice DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Tickets (
    TicketID INT PRIMARY KEY,
    EventID INT REFERENCES Events(EventID),
    UserID INT REFERENCES Users(UserID),
    Status VARCHAR(20) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Artists (
    ArtistID INT PRIMARY KEY,
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
    ManagerID INT PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    AdditionalManagerData VARCHAR(255) NOT NULL
);
CREATE TABLE EventOrganizers (
    OrganizerID INT PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    AdditionalOrganizerData VARCHAR(255) NOT NULL
);
CREATE TABLE SupportTeam (
    SupportID INT PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    AdditionalSupportData VARCHAR(255) NOT NULL
);
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    EventID INT REFERENCES Events(EventID),
    Text TEXT NOT NULL,
    Rating INT NOT NULL
);
CREATE TABLE SalesStatistics (
    StatID INT PRIMARY KEY,
    EventID INT REFERENCES Events(EventID),
    Date DATE NOT NULL,
    TicketsSold INT NOT NULL,
    Revenue DECIMAL(10, 2) NOT NULL
);
