 CREATE DATABASE  IF NOT EXISTS `database2`;
 USE `database2`;
 DROP TABLE IF EXISTS `courses`;
 CREATE TABLE `courses` (
  `courseID` int NOT NULL,
  `courseName` varchar(45) NOT NULL,
  `deapartmentID` int DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`courseID`),
  KEY `department` (`deapartmentID`),
  CONSTRAINT `department` FOREIGN KEY (`deapartmentID`) REFERENCES `department` (`departmentID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `courses` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `faculty`;
CREATE TABLE `faculty` (
  `facultyId` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `emailID` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  PRIMARY KEY (`facultyId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `faculty` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `records`;
CREATE TABLE `records` (
  `Year` int NOT NULL,
  PRIMARY KEY (`Year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `records` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `departmentID` int NOT NULL,
  `departmentName` varchar(45) NOT NULL,
  PRIMARY KEY (`departmentID`),
  UNIQUE KEY `departmentName_UNIQUE` (`departmentName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `department` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `istaughtby`;
CREATE TABLE `istaughtby` (
  `courseID` int NOT NULL,
  `facultyId` int NOT NULL,
  `startingYear` int DEFAULT NULL,
  `endYear` int DEFAULT NULL,
  `day` varchar(45) NOT NULL,
  `timing` varchar(45) NOT NULL,
  `roomNo` varchar(45) NOT NULL,
  PRIMARY KEY (`courseID`,`facultyId`),
  KEY `faculty` (`facultyId`),
  CONSTRAINT `courses` FOREIGN KEY (`courseID`) REFERENCES `courses` (`courseID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `faculty` FOREIGN KEY (`facultyId`) REFERENCES `faculty` (`facultyId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `istaughtby` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `associated`;
CREATE TABLE `associated` (
  `departmentID` int NOT NULL,
  `facultyId` int NOT NULL,
  PRIMARY KEY (`departmentID`,`facultyId`),
  KEY `facultyId` (`facultyId`),
  CONSTRAINT `departmentID` FOREIGN KEY (`departmentID`) REFERENCES `department` (`departmentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `facultyId` FOREIGN KEY (`facultyId`) REFERENCES `faculty` (`facultyId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `associated` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `registeredstudents`;
CREATE TABLE `registeredstudents` (
  `courseID` int NOT NULL,
  `year` int NOT NULL,
  `noOfRegisteredStudents` int(10) unsigned zerofill NOT NULL,
  PRIMARY KEY (`courseID`,`year`),
  KEY `year` (`year`),
  CONSTRAINT `course` FOREIGN KEY (`courseID`) REFERENCES `courses` (`courseID`),
  CONSTRAINT `year` FOREIGN KEY (`year`) REFERENCES `records` (`Year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `registeredstudents` WRITE;
UNLOCK TABLES;


INSERT into courses (courseID, courseName, semester) values (207, 'Database Management System',3);
INSERT into courses (courseID, courseName, semester) values (203, 'Data Structure and Algorithmns',3);
UPDATE courses SET deapartmentID = 1;
INSERT into courses (courseID, courseName, deapartmentID, semester) values (156, 'Physics',3,2);
INSERT into courses (courseID, courseName, deapartmentID, semester) values (104, 'Basics of Electrical Engineering', 2, 2);
INSERT into courses (courseID, courseName, deapartmentID, semester) values (106, 'Basics of Mechanical Engineering', 4, 2);
INSERT into courses (courseID, courseName, deapartmentID, semester) values (103, 'Chemistry', 5, 1);
INSERT into courses (courseID, courseName, deapartmentID, semester) values (105, 'Calculus', 6, 1);
INSERT into courses (courseID, courseName, deapartmentID, semester) values (153, 'Engineering Drawing', 7, 1);
INSERT into courses (courseID, courseName, deapartmentID, semester) values (251, 'Basics of Metallurgy', 8, 2);
INSERT into courses (courseID, courseName, deapartmentID, semester) values (201, 'Discrete Mathematical Structures', 1, 3);
SELECT * FROM courses;

INSERT INTO department (departmentID, departmentName) values (1,'Computer Science and Engineering');
INSERT INTO department (departmentID, departmentName) values (2,'Electrical Engineering');
INSERT INTO department (departmentID, departmentName) values (3,'Physics');
INSERT INTO department (departmentID, departmentName) values (4,'Mechanical Engineering');
INSERT INTO department (departmentID, departmentName) values (5,'Chemistry');
INSERT INTO department (departmentID, departmentName) values (6,'Mathematics');
INSERT INTO department (departmentID, departmentName) values (7,'Civil Engineering');
INSERT INTO department (departmentID, departmentName) values (8,'Metallurgy');
SELECT * FROM department;

INSERT INTO faculty (facultyId, name, emailID, address) values(1, 'Nagendra Kumar', 'nagendra@iiti.ac.in', 'Indore');
INSERT INTO faculty (facultyId, name, emailID, address) values(2, 'Narendra Chaudhari', 'nsc@iiti.ac.in', 'Indore');
INSERT INTO faculty (facultyId, name, emailID, address) values(3, 'Ankhi Roy', 'ankhi@iiti.ac.in', 'Indore');
INSERT INTO faculty (facultyId, name, emailID, address) values(4, 'Ankur Miglani', 'amiglani@iiti.ac.in', 'Indore');
INSERT INTO faculty (facultyId, name, emailID, address) values(5, 'Abhinav Kranti', 'akranti@iiti.ac.in', 'Indore');
INSERT INTO faculty (facultyId, name, emailID, address) values(6, 'Abhishek Srivastava', 'asrivastava@iiti.ac.in', 'Indore');
INSERT INTO faculty (facultyId, name, emailID, address) values(7, 'Vinay Kumar Gupta', 'vkg@iiti.ac.in', 'Indore');
INSERT INTO faculty (facultyId, name, emailID, address) values(8, 'Puneet Gupta', 'puneet@iiti.ac.in', 'Indore');
SELECT * FROM faculty;

INSERT INTO associated (departmentID, facultyId) values (1, 1);
INSERT INTO associated (departmentID, facultyId) values (1, 2);
INSERT INTO associated (departmentID, facultyId) values (6, 2);
INSERT INTO associated (departmentID, facultyId) values (4, 4);
INSERT INTO associated (departmentID, facultyId) values (2, 1);
INSERT INTO associated (departmentID, facultyId) values (2, 5);
INSERT INTO associated (departmentID, facultyId) values (3, 3);
INSERT INTO associated (departmentID, facultyId) values (1, 6);
INSERT INTO associated (departmentID, facultyId) values (6, 7);
INSERT INTO associated (departmentID, facultyId) values (1, 8);

SELECT * FROM associated;

INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (104,5,2009,"M,T,W","10:00","1");
INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (105,7,2009,"M,T,S","11:00","2");
INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (106,4,2009,"M,T,W","12:00","3");
INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (156,3,2009,"M,T,W","10:00","4");
INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (201,2,2009,"M,T,W","11:00","5");
INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (207,1,2009,"M,T,W","12:00","5");
INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (201,1,2009,"M,T,W","12:00","5");
INSERT INTO istaughtby (courseID, facultyId, startingYear, day, timing, roomNO) VALUES (203,8,2009,"M,T,W","10:00","5");
UPDATE istaughtby SET endYear = 2011 WHERE courseID = 201;

SELECT * FROM istaughtby;
