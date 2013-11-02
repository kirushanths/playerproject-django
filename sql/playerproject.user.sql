/*
Navicat MySQL Data Transfer

Source Server         :  Localhost
Source Server Version : 50141
Source Host           : localhost:3306
Source Database       : flexi_auth_demo

Target Server Type    : MYSQL
Target Server Version : 50141
File Encoding         : 65001

Date: 2012-04-12 22:40:38
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `ci_sessions`
-- ----------------------------
DROP TABLE IF EXISTS `ci_sessions`;
CREATE TABLE `ci_sessions` (
  `session_id` varchar(40) NOT NULL DEFAULT '0',
  `ip_address` varchar(16) NOT NULL DEFAULT '0',
  `user_agent` varchar(120) DEFAULT NULL,
  `last_activity` int(10) unsigned NOT NULL DEFAULT '0',
  `user_data` text NOT NULL,
  PRIMARY KEY (`session_id`),
  KEY `last_activity` (`last_activity`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for `user_accounts`
-- ----------------------------
DROP TABLE IF EXISTS `user_accounts`;
CREATE TABLE `user_accounts` (
  `uacc_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uacc_group_fk` smallint(5) unsigned NOT NULL,
  `uacc_email` varchar(100) NOT NULL,
  `uacc_username` varchar(30) NOT NULL,
  `uacc_password` varchar(60) NOT NULL,
  `uacc_ip_address` varchar(40) NOT NULL,
  `uacc_salt` varchar(40) NOT NULL,
  `uacc_activation_token` varchar(40) NOT NULL,
  `uacc_forgotten_password_token` varchar(40) NOT NULL,
  `uacc_forgotten_password_expire` datetime NOT NULL,
  `uacc_update_email_token` varchar(40) NOT NULL,
  `uacc_update_email` varchar(100) NOT NULL,
  `uacc_active` tinyint(1) unsigned NOT NULL,
  `uacc_suspend` tinyint(1) unsigned NOT NULL,
  `uacc_fail_login_attempts` smallint(5) NOT NULL,
  `uacc_fail_login_ip_address` varchar(40) NOT NULL,
  `uacc_date_fail_login_ban` datetime NOT NULL COMMENT 'Time user is banned until due to repeated failed logins',
  `uacc_date_last_login` datetime NOT NULL,
  `uacc_date_added` datetime NOT NULL,
  PRIMARY KEY (`uacc_id`),
  UNIQUE KEY `uacc_id` (`uacc_id`),
  KEY `uacc_group_fk` (`uacc_group_fk`),
  KEY `uacc_email` (`uacc_email`),
  KEY `uacc_username` (`uacc_username`),
  KEY `uacc_fail_login_ip_address` (`uacc_fail_login_ip_address`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_accounts
-- ----------------------------
INSERT INTO `user_accounts` VALUES ('1', '3', 'admin@admin.com', 'admin', '$2a$08$BJKFG5G.1V8NdU2.CE1E2.p0TjhKSOaLGoBPla50nzmHhnuiHjG/u', '0.0.0.0', 'XKVT29q2Jr', '', '', '0000-00-00 00:00:00', '', '', '1', '0', '0', '', '0000-00-00 00:00:00', '2012-04-12 21:15:05', '2011-01-01 00:00:00');

-- ----------------------------
-- Table structure for `user_login_sessions`
-- ----------------------------
DROP TABLE IF EXISTS `user_login_sessions`;
CREATE TABLE `user_login_sessions` (
  `usess_uacc_fk` int(11) NOT NULL,
  `usess_series` varchar(40) NOT NULL,
  `usess_token` varchar(40) NOT NULL,
  `usess_login_date` datetime NOT NULL,
  PRIMARY KEY (`usess_token`),
  UNIQUE KEY `usess_token` (`usess_token`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_login_sessions
-- ----------------------------
