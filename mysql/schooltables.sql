use school;

DROP TABLE IF EXISTS StudentCourses; 
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Students;

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

INSERT INTO Courses (CourseName, TeacherID) values ("Business", 1);
INSERT INTO Courses (CourseName, TeacherID) values ("Physics", 2);
INSERT INTO Courses (CourseName, TeacherID) values ("Art", 3);
INSERT INTO Courses (CourseName, TeacherID) values ("Math", 2);

INSERT INTO StudentCourses values (1,1);
INSERT INTO StudentCourses values (1,2);
INSERT INTO StudentCourses values (1,3);
INSERT INTO StudentCourses values (2,1);
INSERT INTO StudentCourses values (2,2);
INSERT INTO StudentCourses values (2,3);
INSERT INTO StudentCourses values (2,4);
INSERT INTO StudentCourses values (2,5);
INSERT INTO StudentCourses values (2,6);
INSERT INTO StudentCourses values (4,4);
INSERT INTO StudentCourses values (2,7);
INSERT INTO StudentCourses values (2,8);