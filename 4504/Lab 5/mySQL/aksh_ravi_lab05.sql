-- Create db
CREATE DATABASE IF NOT EXISTS aksh_ravi_lab05 -- Q1: Create student info table with corresponding columns and datatypes
CREATE TABLE STUDENT_INFO (
    ID INT,
    NAME VARCHAR(100),
    DOB DATE,
    INCOME DECIMAL(10, 2),
    COURSE_ID INT(5)
);
-- Q2: Create course info table with corresponding columns and datatypes
CREATE TABLE COURSE_INFO (
    ID INT NOT NULL PRIMARY KEY,
    NAME VARCHAR(100),
    LOCATION VARCHAR(200),
    STARTDATE DATE,
    TYPE VARCHAR(100)
);
-- Q3: Add addr column to student info table
ALTER TABLE student_info
ADD ADDRESS VARCHAR(200) DEFAULT NULL;
-- Q4: Change name column to allow longer strings
ALTER TABLE student_info
MODIFY COLUMN NAME VARCHAR(200);
-- Q5/6: Rename both tables to drop _info from name
ALTER TABLE student_info
    RENAME to STUDENT;
ALTER TABLE course_info
    RENAME to COURSE;
-- Q7. Insert 3 rows into student table 
INSERT INTO STUDENT (ID, NAME, DOB, INCOME, COURSE_ID, ADDRESS)
VALUES (1, 'JOHN', '1998-05-01', 1200, 100, 'NORTH');
INSERT INTO STUDENT (ID, NAME, DOB, INCOME, COURSE_ID, ADDRESS)
VALUES (2, 'MIKE', '2000-08-15', 1100.15, 200, 'WEST');
INSERT INTO STUDENT (ID, NAME, DOB, INCOME, COURSE_ID, ADDRESS)
VALUES (3, 'SAM', '1997-11-01', 500, 100, 'SOUTH');
-- Q8. Insert 4 rows into COURSES
INSERT INTO course (ID, NAME, LOCATION, STARTDATE, TYPE)
VALUES (
        100,
        'Fundamentals of Web Development',
        'Azrieli Pavilion',
        '2023-09-10',
        'mandatory'
    );
INSERT INTO course (ID, NAME, LOCATION, STARTDATE, TYPE)
VALUES (
        300,
        'Analytical Methods',
        'Tory Building',
        '2023-09-17',
        'elective'
    );
INSERT INTO course (ID, NAME, LOCATION, STARTDATE, TYPE)
VALUES (
        500,
        'Java Programming',
        'Tory Building',
        '2023-09-17',
        'elective'
    );
INSERT INTO course (ID, NAME, LOCATION, STARTDATE, TYPE)
VALUES (
        700,
        'C++ Programming',
        'Patterson Hall',
        '2023-09-10',
        'elective'
    );
-- Q9. Update income for student 2
UPDATE student
SET INCOME = 1000
WHERE ID = 2;
-- Q10. Update location for course 100
UPDATE course
SET LOCATION = 'Patterson Hall'
WHERE ID = 100;
-- Q11/12. Delete table rows
DELETE FROM student
WHERE ID = 2;
DELETE FROM course
WHERE ID = 300;
-- Q13/14. Select all 
SELECT *
FROM student
SELECT *
FROM course;
-- Q15/16. Select specific
SELECT NAME,
    DOB,
    INCOME
FROM student;
SELECT COURSE_ID,
    NAME,
    LOCATION
FROM course;
-- Q17/18. Select Search
SELECT ID,
    NAME,
    DOB,
    INCOME
FROM student
WHERE INCOME > 600;
SELECT *
FROM course
WHERE LOCATION = 'Patterson Hall'
    AND TYPE = 'elective';
-- Q19. Select and join
SELECT student.ID AS STUDENT_ID,
    student.NAME,
    student.DOB,
    student.COURSE_ID AS COURSE_ID
FROM student;
INNER JOIN course ON course.ID = student.COURSE_ID;
-- Q20. Select and join
SELECT student.ID,
    student.NAME,
    student.DOB,
    course.NAME
FROM student
    INNER JOIN course ON course.ID = student.COURSE_ID
WHERE INCOME > 1000;
-- Q22. Truncate
TRUNCATE TABLE student;
SELECT * FROM student;
TRUNCATE TABLE course;
SELECT * FROM course;
-- Drop tables
DROP TABLE student; SELECT * FROM student;
DROP TABLE course; SELECT * FROM course;