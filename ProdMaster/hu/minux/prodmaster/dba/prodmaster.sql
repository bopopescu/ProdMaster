-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: prodmaster
-- ------------------------------------------------------
-- Server version	5.5.37-0+wheezy1

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
-- Table structure for table `additive`
--

DROP TABLE IF EXISTS `additive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `additive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci NOT NULL,
  `additive_group_id` int(11) NOT NULL,
  `e_number` varchar(16) COLLATE utf8_hungarian_ci NOT NULL,
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `fk_additives_1` (`additive_group_id`),
  CONSTRAINT `fk_additives_1` FOREIGN KEY (`additive_group_id`) REFERENCES `additive_group` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additive`
--

LOCK TABLES `additive` WRITE;
/*!40000 ALTER TABLE `additive` DISABLE KEYS */;
/*!40000 ALTER TABLE `additive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `additive_group`
--

DROP TABLE IF EXISTS `additive_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `additive_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci NOT NULL DEFAULT '',
  `group_nr` smallint(6) NOT NULL,
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additive_group`
--

LOCK TABLES `additive_group` WRITE;
/*!40000 ALTER TABLE `additive_group` DISABLE KEYS */;
INSERT INTO `additive_group` VALUES (1,'Színezékek',1,'100-181'),(2,'Tartósítószerek',2,'200-297'),(3,'Antioxidánsok és savanyúságot szabályzó anyagok',3,'300-386'),(4,'Sűrítőanyagok, stabilizátorok és emulgeálószerek',4,'400-495'),(5,'Savanyúságot szabályzó anyagok és csomósodást gátló anyagok',5,'500-585'),(6,'Ízfokozók',6,'600-671'),(7,'Antibiotikumok',7,'700-772'),(8,'Egyéb adalékanyagok',9,'900-999'),(9,'Kiegészítő anyagok',10,'1000-1520');
/*!40000 ALTER TABLE `additive_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `is_root` tinyint(1) NOT NULL DEFAULT '0',
  `weight` tinyint(4) NOT NULL DEFAULT '0',
  `parent` varchar(16) COLLATE utf8_hungarian_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'FILE',1,0,''),(2,'EXIT',0,0,'FILE'),(3,'EDIT',1,0,''),(4,'DATA',1,0,''),(5,'PARTNERS',0,0,'DATA'),(6,'ADDITIVE_GROUPS',0,100,'DATA'),(7,'ADDITIVES',0,50,'DATA'),(8,'RAW_MATERIALS',0,25,'DATA'),(9,'PRODUCTS',0,35,'DATA'),(10,'MOVEMENTS',1,0,''),(11,'ROUNDTRIP_SALES',0,100,'MOVEMENTS'),(12,'STOCKS',0,120,'DATA'),(13,'MOVEMENT_TYPES',0,127,'DATA');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movement_type`
--

DROP TABLE IF EXISTS `movement_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movement_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci NOT NULL,
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movement_type`
--

LOCK TABLES `movement_type` WRITE;
/*!40000 ALTER TABLE `movement_type` DISABLE KEYS */;
INSERT INTO `movement_type` VALUES (1,'Túrajárat értékesítés',''),(2,'Csere vevőnél',''),(3,'Visszáru','A vevőtől visszavásárolt tétel'),(4,'Helyi készpénzes értékesítés',''),(5,'Raktárközi átadás','Telephelyen belüli készletmozgás');
/*!40000 ALTER TABLE `movement_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partner`
--

DROP TABLE IF EXISTS `partner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `partner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci NOT NULL,
  `reg_number` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `bank_account` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `head_city` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `head_zip` varchar(16) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `head_address` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `is_customer` tinyint(1) NOT NULL DEFAULT '0',
  `is_supplier` tinyint(1) NOT NULL DEFAULT '0',
  `remark` text COLLATE utf8_hungarian_ci,
  `is_enabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partner`
--

LOCK TABLES `partner` WRITE;
/*!40000 ALTER TABLE `partner` DISABLE KEYS */;
INSERT INTO `partner` VALUES (1,'Minux Bt.','aszám','','Gárdony-Agárd','2484','Marx tér 11.',0,0,'Fekete Zoltán, képviselő\n\n\n',1),(4,'Hakaba Consulting Kft.','','szla','Gárdony','2483','Paál László u. 10.',0,0,'Somossy Eszter, ügyvezető\n\n\n\n\n',1),(5,'Ostya 84 Bt.','','','','','',0,0,'ostya',1),(6,'Valagvári KKT.','','','','','',0,0,'\n',0),(7,'Puskás és Tsa.','','','','','',0,0,'\n',0),(8,'C retek kft.','','','','','',0,0,'\n\n',0),(9,'Gárdony Város és Térsége Turisztikai Egyesület','','','Gárdony','2483','Szabadság út 20-22.',0,0,'\n',0),(10,'zabheygi','','','','','',0,0,'\n',0),(11,'zalahús 1','','','','','',0,0,'\n',0),(12,'Alba Régia Állami Építőipari Vállalat','1234567-8-90','bankszámlaszám','Székesfehérvár','8001','Seregélyesi út 120-122.',0,0,'\'egy aprócska\' \"kalapocska\" \'\'\'benne csacska\'\'\'\nMacsó mocska\n\n',0),(13,'Fafejű Kft.','12345','','','','',0,0,'\n\n',0),(15,'Gyökér Egyesület új 1','','','','','',0,0,'\n\n',1),(16,'Ragyamenti MgTSZ','','','','','',0,0,'\ntéeszcsé\n',0),(17,'Ilosvay Selyem Út KKT.','','','','','',0,0,'\n',0),(19,'Mucsa Bt.','','','','','',0,0,'\n',0),(20,'Ragyamanti MGTSZ','','','','','',0,0,'\n',0),(21,'Újj kft 1','','','','','',0,0,'\n',0),(22,'Surc Kalagám Kkt.','','','','','',0,0,'',0),(23,'AAA Kft.','','','','','',0,0,'',0),(24,'AAABB Kft.','','','','','',0,0,'',0),(25,'bbbb','','','','','',0,0,'',0);
/*!40000 ALTER TABLE `partner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `partner_id` int(11) NOT NULL,
  `address` text COLLATE utf8_hungarian_ci,
  `phone` text COLLATE utf8_hungarian_ci,
  `email` text COLLATE utf8_hungarian_ci,
  `remark` text COLLATE utf8_hungarian_ci,
  `weight` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`partner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (53,'Fekete Zoli',1,'','','','ügyvezető',0),(58,'Zoli',5,'','','','',0),(59,'Móni',5,'','','','',1),(60,'Anyu',5,'','','','',3),(61,'Bélánk',6,'','','','',0),(62,'Surc Ottó',0,'','','',' ügyvezető',0),(63,'Aranka',0,'','','','',0),(64,'cxcxyfc',0,'','','','',0),(65,'xvcxvyv',23,'','','','',0);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci NOT NULL,
  `is_endproduct` tinyint(1) NOT NULL DEFAULT '0',
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Fehérvári ostya lédig',1,'első és legjobb termékünk ever'),(2,'Fehérvári ostya 200 g - kakaós',1,'AUCHAN'),(3,'Fehérvári ostya 200 g - vaníliás',1,''),(4,'Fehérvári ostya 200 g - capuccino',1,'');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_recipe`
--

DROP TABLE IF EXISTS `product_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_recipe` (
  `product_contents` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `percentage` tinyint(4) NOT NULL DEFAULT '0',
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`product_contents`),
  KEY `fk_product_recipe_1` (`product_id`),
  CONSTRAINT `fk_product_recipe_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_recipe`
--

LOCK TABLES `product_recipe` WRITE;
/*!40000 ALTER TABLE `product_recipe` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_material`
--

DROP TABLE IF EXISTS `raw_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raw_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci NOT NULL,
  `is_composite` tinyint(1) NOT NULL DEFAULT '0',
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_material`
--

LOCK TABLES `raw_material` WRITE;
/*!40000 ALTER TABLE `raw_material` DISABLE KEYS */;
INSERT INTO `raw_material` VALUES (3,'Kristálycukor',0,'');
/*!40000 ALTER TABLE `raw_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_material_contents`
--

DROP TABLE IF EXISTS `raw_material_contents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raw_material_contents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `raw_material_id` int(11) NOT NULL,
  `weight` smallint(6) NOT NULL DEFAULT '0',
  `percentage` tinyint(4) DEFAULT NULL,
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`),
  KEY `fk_raw_material_contents_1` (`raw_material_id`),
  CONSTRAINT `fk_raw_material_contents_1` FOREIGN KEY (`raw_material_id`) REFERENCES `raw_material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_material_contents`
--

LOCK TABLES `raw_material_contents` WRITE;
/*!40000 ALTER TABLE `raw_material_contents` DISABLE KEYS */;
/*!40000 ALTER TABLE `raw_material_contents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `site`
--

DROP TABLE IF EXISTS `site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `partner_id` int(11) NOT NULL,
  `city` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `zip` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `address` varchar(64) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `phone` text COLLATE utf8_hungarian_ci,
  `email` text COLLATE utf8_hungarian_ci,
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`,`partner_id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `site`
--

LOCK TABLES `site` WRITE;
/*!40000 ALTER TABLE `site` DISABLE KEYS */;
/*!40000 ALTER TABLE `site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_hungarian_ci NOT NULL,
  `remark` text COLLATE utf8_hungarian_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES (1,'Alapanyagraktár 1.','Fő épületben, a konyha előtt'),(2,'Lisztraktár 1.','Fő épületben a masszakeverőnél'),(3,'Készáru raktár','Külön épületben'),(4,'Alkatrész raktár 1.','\"Benizs\" raktár '),(5,'Csomagolóanyag raktár 1.','Új csomagolóépület üvegablakos'),(6,'Tisztítószer raktár 1.','Fő épületben');
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-06-26 15:30:39
