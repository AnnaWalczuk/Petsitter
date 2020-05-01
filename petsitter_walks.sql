-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: petsitter
-- ------------------------------------------------------
-- Server version	5.7.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `walks`
--

DROP TABLE IF EXISTS `walks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `walks` (
  `id_walk` int(11) NOT NULL AUTO_INCREMENT,
  `id_dog` int(11) NOT NULL,
  `id_emp` int(11) NOT NULL,
  PRIMARY KEY (`id_walk`),
  UNIQUE KEY `id_walk_UNIQUE` (`id_walk`),
  UNIQUE KEY `id_dog_UNIQUE` (`id_dog`),
  KEY `id_employee_idx` (`id_emp`),
  KEY `dog_idx` (`id_dog`),
  CONSTRAINT `dog` FOREIGN KEY (`id_dog`) REFERENCES `dogs` (`id_dog`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `employee` FOREIGN KEY (`id_emp`) REFERENCES `employees` (`id_employee`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `walks`
--

LOCK TABLES `walks` WRITE;
/*!40000 ALTER TABLE `walks` DISABLE KEYS */;
INSERT INTO `walks` VALUES (1,1,1),(2,7,3),(3,2,1),(4,5,8),(5,21,4),(6,6,2),(7,9,5),(8,13,6),(9,16,7),(10,4,2),(11,10,4),(12,11,5),(13,17,6),(14,20,7),(15,26,2),(16,3,5),(17,8,1),(18,12,7),(19,14,4),(20,15,3),(21,18,8),(22,19,6),(23,22,5),(24,23,4),(25,24,8),(26,25,3);
/*!40000 ALTER TABLE `walks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-16  8:58:55
