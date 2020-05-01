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
-- Table structure for table `dogs`
--

DROP TABLE IF EXISTS `dogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dogs` (
  `id_dog` int(11) NOT NULL AUTO_INCREMENT,
  `dog_name` varchar(20) NOT NULL,
  `male_female` varchar(1) NOT NULL,
  `age` decimal(10,0) NOT NULL,
  `breed` varchar(45) NOT NULL,
  `food` varchar(45) NOT NULL,
  `walk_in_minutes` int(3) NOT NULL,
  `id_food` int(3) DEFAULT NULL,
  PRIMARY KEY (`id_dog`),
  UNIQUE KEY `id_dog_UNIQUE` (`id_dog`),
  KEY `id_food_idx` (`id_food`),
  CONSTRAINT `id_food` FOREIGN KEY (`id_food`) REFERENCES `food` (`id_food`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dogs`
--

LOCK TABLES `dogs` WRITE;
/*!40000 ALTER TABLE `dogs` DISABLE KEYS */;
INSERT INTO `dogs` VALUES (1,'Suzi','f',3,'mixed-breed','Chappi',120,1),(2,'Max','m',9,'york','Chappi',30,1),(3,'Azor','m',5,'beagle','Pedigree',30,3),(4,'Rex','m',7,'mixed-breed','Chappi',60,1),(5,'Aki','m',4,'mixed-breed','Chappi',120,1),(6,'Nala','f',4,'border collie','Pedigree',90,3),(7,'Brita','f',1,'doberman','Bosch Junior',30,2),(8,'Kapsel','m',7,'york','Chappi',30,1),(9,'Bianka','f',8,'spaniel','Chappi',90,1),(10,'Ellie','f',3,'mixed-breed','Pedigree',60,3),(11,'Cookie','f',5,'jack russel terrier','Chappi',60,1),(12,'Benio','m',5,'bulldog','Chappi',30,1),(13,'Dino','m',8,'labrador','Pedigree',90,3),(14,'Figa','f',2,'dachshund','Bosch Junior',30,2),(15,'Dolar','m',4,'mixed-breed','Pedigree',30,3),(16,'Gaja','f',3,'mixed-breed','Pedigree',90,3),(17,'Zara','f',1,'husky','Bosch Junior',60,2),(18,'Excel','m',3,'york','Pedigree',30,3),(19,'Fuks','m',3,'beagle','Pedigree',30,3),(20,'Humus','m',6,'mixed-breed','Pedigree',60,3),(21,'Iman','m',5,'rottweiler','Pedigree',120,3),(22,'Tatra','f',8,'mixed-breed','Pedigree',30,3),(23,'Samantha','f',1,'doberman','Bosch Junior',30,2),(24,'Fabio','m',2,'york','Bosch Junior',30,2),(25,'Krakers','m',7,'maltese','Chappi',30,1),(26,'Sissi','f',6,'spaniel','Pedigree',60,3);
/*!40000 ALTER TABLE `dogs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-16  8:58:56
