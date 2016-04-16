#select * from Students;
#select * from Teachers;
#select * from Courses;
#select * from StudentCourses;
select s.StudentID, s.StudentName, count(sc.CourseID) from StudentCourses sc right join Students s on s.StudentID = sc.StudentID group by s.StudentID;
select StudentName, count(CourseID) from StudentCourses right join Students on StudentCourses.StudentID = Students.StudentID group by StudentName;
select * from StudentCourses sc join Students s on sc.StudentID = s.StudentID;
select * from StudentCourses sc join Courses c on sc.CourseID = c.CourseID join Teachers t on t.TeacherID = c.TeacherID;
select t.TeacherID, t.TeacherName, count(sc.studentID) from StudentCourses sc join Courses c on sc.CourseID = c.CourseID right join Teachers t on t.TeacherID = c.TeacherID group by t.TeacherID;