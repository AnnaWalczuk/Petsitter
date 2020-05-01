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
-- Temporary view structure for view `v_walks_admin`
--

DROP TABLE IF EXISTS `v_walks_admin`;
/*!50001 DROP VIEW IF EXISTS `v_walks_admin`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_walks_admin` AS SELECT 
 1 AS `id_dog`,
 1 AS `dog_name`,
 1 AS `id_emp`,
 1 AS `first_name`,
 1 AS `walk_in_minutes`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_walks`
--

DROP TABLE IF EXISTS `v_walks`;
/*!50001 DROP VIEW IF EXISTS `v_walks`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_walks` AS SELECT 
 1 AS `nb`,
 1 AS `dog_name`,
 1 AS `walk_length`,
 1 AS `employee`,
 1 AS `emp_user_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_walks_admin`
--

/*!50001 DROP VIEW IF EXISTS `v_walks_admin`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_walks_admin` AS select `w`.`id_dog` AS `id_dog`,`d`.`dog_name` AS `dog_name`,`w`.`id_emp` AS `id_emp`,`e`.`first_name` AS `first_name`,`d`.`walk_in_minutes` AS `walk_in_minutes` from ((`walks` `w` join `dogs` `d` on((`w`.`id_dog` = `d`.`id_dog`))) join `employees` `e` on((`w`.`id_emp` = `e`.`id_employee`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_walks`
--

/*!50001 DROP VIEW IF EXISTS `v_walks`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_walks` AS select `w`.`id_walk` AS `nb`,`d`.`dog_name` AS `dog_name`,`d`.`walk_in_minutes` AS `walk_length`,`e`.`first_name` AS `employee`,`el`.`user_name` AS `emp_user_name` from (((`walks` `w` join `dogs` `d` on((`w`.`id_dog` = `d`.`id_dog`))) join `employees` `e` on((`w`.`id_emp` = `e`.`id_employee`))) join `emp_login` `el` on((`w`.`id_emp` = `el`.`id_employee`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-16  8:58:56
