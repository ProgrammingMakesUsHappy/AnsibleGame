CREATE DATABASE  IF NOT EXISTS `gamedb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `gamedb`;
-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: gamedb
-- ------------------------------------------------------
-- Server version	5.7.23

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
-- Table structure for table `fileSystemMonitor`
--

DROP TABLE IF EXISTS `fileSystemMonitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fileSystemMonitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FilePath` varchar(128) NOT NULL,
  `HostIP` varchar(45) NOT NULL,
  `HostName` varchar(45) NOT NULL,
  `FS` varchar(128) NOT NULL,
  `Volume` varchar(45) NOT NULL,
  `Usage` int(11) NOT NULL,
  `Time` varchar(45) NOT NULL DEFAULT 'now()',
  `Group` varchar(45) NOT NULL DEFAULT 'web',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fileSystemMonitor`
--

LOCK TABLES `fileSystemMonitor` WRITE;
/*!40000 ALTER TABLE `fileSystemMonitor` DISABLE KEYS */;
INSERT INTO `fileSystemMonitor` VALUES (1,'/usr/','192.168.3.1','qiushi-X270-W10DG','/dev/nvme0n1p4','136G',34,'2018-07-25 09:26:08',''),(2,'/var/','192.168.3.1','qiushi-X270-W10DG','/dev/nvme0n1p4','136G',34,'2018-07-25 09:26:27','host'),(3,'','192.168.3.1','qiushi-X270-W10DG','udev','3.9G',0,'2018-07-25 16:03:51','host'),(4,'/home/','192.168.3.1','qiushi-X270-W10DG','/dev/nvme0n1p4','136G',34,'2018-07-25 18:58:19','host');
/*!40000 ALTER TABLE `fileSystemMonitor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-31 19:21:09
