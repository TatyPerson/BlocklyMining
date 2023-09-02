# ************************************************************
# Sequel Pro SQL dump
# Versión 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.23)
# Base de datos: BlockyMiningDatabase
# Tiempo de Generación: 2023-09-02 15:50:42 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Volcado de tabla Issue
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Issue`;

CREATE TABLE `Issue` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `block_id` varchar(10000) NOT NULL DEFAULT '',
  `issue_type` varchar(10000) NOT NULL DEFAULT '',
  `project_id` varchar(100) NOT NULL DEFAULT '',
  `screen_name` varchar(100) NOT NULL DEFAULT '',
  `block_type` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `screen_id` (`project_id`,`screen_name`),
  CONSTRAINT `screen_id` FOREIGN KEY (`project_id`, `screen_name`) REFERENCES `Screen` (`project_id`, `name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Volcado de tabla Project
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Project`;

CREATE TABLE `Project` (
  `id` varchar(100) NOT NULL DEFAULT '',
  `name` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Volcado de tabla Screen
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Screen`;

CREATE TABLE `Screen` (
  `project_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL DEFAULT '',
  `blocks_number` int(100) unsigned NOT NULL,
  PRIMARY KEY (`project_id`,`name`),
  CONSTRAINT `project` FOREIGN KEY (`project_id`) REFERENCES `Project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
