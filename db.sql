/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.3.20-MariaDB : Database - food_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`food_management` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `food_management`;

/*Table structure for table `donor` */

DROP TABLE IF EXISTS `donor`;

CREATE TABLE `donor` (
  `donor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `idproof` varchar(500) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`donor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `donor` */

insert  into `donor`(`donor_id`,`login_id`,`name`,`place`,`phone`,`email`,`idproof`,`latitude`,`longitude`) values (1,2,'dfs sdfd','sdfd','9207163431','athulappu@gmail.com','static/images/7a17887b-3670-444e-b207-f1b5eb2e53bcnew3.jpg','9.982840260177271','76.29869062773896'),(2,3,'dfs sdfd','sdfd','9207163431','athulappu@gmail.com','static/images/cb68c0d1-3d38-491a-b1df-8ec4d8487bfcnew3.jpg','9.982840260177271','76.29869062773896'),(3,4,'dfs sdfd','sdfd','9207163431','athulappu@gmail.com','static/images/1f7c1db9-939d-4185-9032-d5309c9649ebnew3.jpg','9.982840260177271','76.29869062773896'),(4,5,'dfs sdfd','sdfd','9207163431','athulappu@gmail.com','static/images/fe7ac6c8-bce9-4bda-a531-8b46b888faffnew3.jpg','9.982840260177271','76.29869062773896'),(5,15,'sadad san kar','alpy','6238526459','sankarb.b00@gmail.com','static/images/271fa3bd-5caa-4115-a369-8c25a4301707team-1.png','9.982840260177271','76.29869062773896'),(6,16,'arjun','kochi','9207163431','athulappu@gmail.com','static/images/d6b68935-0b9c-4289-b187-c05876cb75a7testimonial-4.jpg','9.982840260177271','76.29869062773896');

/*Table structure for table `excess_food` */

DROP TABLE IF EXISTS `excess_food`;

CREATE TABLE `excess_food` (
  `excessfood_id` int(11) NOT NULL AUTO_INCREMENT,
  `donor_id` int(11) DEFAULT NULL,
  `foodname` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`excessfood_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `excess_food` */

insert  into `excess_food`(`excessfood_id`,`donor_id`,`foodname`,`quantity`,`status`) values (1,1,'sweets','20','available'),(2,1,'grains','20','available');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`sender_id`,`feedback`,`reply`,`date`) values (1,2,'i want to talk','pending','2022-09-01'),(2,12,'hello u there','pending','2022-09-02'),(3,11,'i am resc','pending','2022-09-02');

/*Table structure for table `forward_volunteer` */

DROP TABLE IF EXISTS `forward_volunteer`;

CREATE TABLE `forward_volunteer` (
  `forward_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `volunteer_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`forward_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `forward_volunteer` */

insert  into `forward_volunteer`(`forward_id`,`request_id`,`volunteer_id`,`status`) values (1,3,4,'delevered sucessfull'),(2,3,4,'delevered sucessfull');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (12,'vol','vol','volunteer'),(2,'donor1','donor','donor'),(3,'donor','donor','donor'),(4,'donor','donor','donor'),(5,'donor','donor','pending'),(13,'user','sa','pending'),(7,'sadad','sdadssad','pending'),(11,'rec','rec','recipient'),(9,'admin','admin','admin'),(14,'user','sda','pending'),(15,'nb','nbnb','pending'),(16,'don','don','donor'),(17,'recip','recip','recipient'),(18,'volu','volu','volunteer');

/*Table structure for table `recipient` */

DROP TABLE IF EXISTS `recipient`;

CREATE TABLE `recipient` (
  `recipient_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`recipient_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `recipient` */

insert  into `recipient`(`recipient_id`,`login_id`,`name`,`place`,`phone`,`email`,`latitude`,`longitude`) values (2,11,'athul','kochi','9207163431','athulappu@gmail.com','9.497873526242447','76.33888486285701'),(3,13,'sadad san kar','kochi','6238526459','sankarb.b00@gmail.com','9.497873526242447','76.33888486285701'),(4,17,'michal','Alappuzha','6238526459','sankarb.b00@gmail.com','9.497873526242447','76.33888486285701');

/*Table structure for table `requst` */

DROP TABLE IF EXISTS `requst`;

CREATE TABLE `requst` (
  `requst_id` int(11) NOT NULL AUTO_INCREMENT,
  `excessfood_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `recipient_id` int(11) DEFAULT NULL,
  `deliverytype` varchar(50) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`requst_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `requst` */

insert  into `requst`(`requst_id`,`excessfood_id`,`quantity`,`recipient_id`,`deliverytype`,`status`) values (3,1,'10',2,'By Volunteer','delevered sucessfull');

/*Table structure for table `volunteer` */

DROP TABLE IF EXISTS `volunteer`;

CREATE TABLE `volunteer` (
  `volunteer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `idproof` varchar(500) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`volunteer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `volunteer` */

insert  into `volunteer`(`volunteer_id`,`login_id`,`name`,`place`,`phone`,`email`,`idproof`,`latitude`,`longitude`) values (2,12,'athul','','9207163431','athulappu@gmail.com','static/images/f4856e5e-ee88-4889-aa19-a2039d2f8eb4photo-1522252234503-e356532cafd5.jpg','9.826108609809038','76.4361564280037'),(3,14,'sdad dasada','dasada','9207163431','athulappu@gmail.com','static/images/44407658-819b-4c45-8b31-c9ea93da2009team-2.png','9.826108609809038','76.4361564280037'),(4,18,'shalini','kottayam','6238526459','shalini.b00@gmail.com','static/images/b7f28f5c-2cd8-4729-b751-3bcbd76311cctestimonial-2.jpg','9.826108609809038','76.4361564280037');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
