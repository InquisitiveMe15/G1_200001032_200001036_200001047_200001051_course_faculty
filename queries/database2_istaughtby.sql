-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: database2
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `istaughtby`
--

DROP TABLE IF EXISTS `istaughtby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
  CONSTRAINT `courses` FOREIGN KEY (`courseID`) REFERENCES `courses` (`courseID`) ON DELETE CASCADE,
  CONSTRAINT `faculty` FOREIGN KEY (`facultyId`) REFERENCES `faculty` (`facultyId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `istaughtby`
--

LOCK TABLES `istaughtby` WRITE;
/*!40000 ALTER TABLE `istaughtby` DISABLE KEYS */;
INSERT INTO `istaughtby` VALUES (104,5,2009,NULL,'M,T,W','10:00','1'),(105,7,2009,NULL,'M,T,S','11:00','2'),(106,4,2009,NULL,'M,T,W','12:00','3'),(156,3,2009,NULL,'M,T,W','10:00','4'),(201,2,2009,NULL,'M,T,W','11:00','5'),(203,8,2009,NULL,'M,T,W','10:00','5'),(207,1,2009,NULL,'M,T,W','12:00','5');
/*!40000 ALTER TABLE `istaughtby` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-13 12:40:51
