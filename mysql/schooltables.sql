use school;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS StudentCourses; 

CREATE TABLE IF NOT EXISTS Teachers (
	TeacherID int AUTO_INCREMENT PRIMARY KEY,
    TeacherName varchar(30) 
);
    
CREATE TABLE IF NOT EXISTS Students (
	StudentID int AUTO_INCREMENT PRIMARY KEY,
    StudentName varchar(30) 
);

CREATE TABLE IF NOT EXISTS Courses (
	CourseID int AUTO_INCREMENT PRIMARY KEY,
    CourseName varchar(30),
    TeacherID int,
    FOREIGN KEY (TeacherID) references Teachers(TeacherID)
);

CREATE TABLE IF NOT EXISTS StudentCourses (
	CourseID int,
    StudentID int,
    PRIMARY KEY(CourseID, StudentID),
    foreign key(CourseID) references Courses(CourseID),
    foreign key(StudentID) references Students(StudentID)
);

INSERT INTO Teachers (TeacherName) values("John Smith");
INSERT INTO Teachers (TeacherName) values("Charles Xavier");
INSERT INTO Teachers (TeacherName) values("Duncan Darryl");
INSERT INTO Teachers (TeacherName) values("Samantha Willinger");

INSERT INTO Students (StudentName) values("Bob Mark");
INSERT INTO Students (StudentName) values("Ethan Stanley");
INSERT INTO Students (StudentName) values("Calvin Mon");
INSERT INTO Students (StudentName) values("Hugh Jazz");
INSERT INTO Students (StudentName) values("Raphael De'La'Ghetto");
INSERT INTO Students (StudentName) values("Steven Stevenson");
INSERT INTO Students (StudentName) values("Pat Riley");
INSERT INTO Students (StudentName) values("Ruben Studdard");
INSERT INTO Students (StudentName) values("Franklin Roosevelt");