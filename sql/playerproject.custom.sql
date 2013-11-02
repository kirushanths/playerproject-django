
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `demo_user_address`
-- ----------------------------
DROP TABLE IF EXISTS `tpp_user_address`;
CREATE TABLE `tpp_user_address` (
  `uadd_id` int(11) NOT NULL AUTO_INCREMENT,
  `uadd_uacc_fk` int(11) NOT NULL,
  `uadd_alias` varchar(50) NOT NULL,
  `uadd_recipient` varchar(100) NOT NULL,
  `uadd_phone` varchar(25) NOT NULL,
  `uadd_company` varchar(75) NOT NULL,
  `uadd_address_01` varchar(100) NOT NULL,
  `uadd_address_02` varchar(100) NOT NULL,
  `uadd_city` varchar(50) NOT NULL,
  `uadd_county` varchar(50) NOT NULL,
  `uadd_post_code` varchar(25) NOT NULL,
  `uadd_country` varchar(50) NOT NULL,
  PRIMARY KEY (`uadd_id`),
  UNIQUE KEY `uadd_id` (`uadd_id`),
  KEY `uadd_uacc_fk` (`uadd_uacc_fk`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for `demo_user_profiles`
-- ----------------------------
DROP TABLE IF EXISTS `tpp_user_profiles`;
CREATE TABLE `tpp_user_profiles` (
  `upro_id` int(11) NOT NULL AUTO_INCREMENT,
  `upro_uacc_fk` int(11) NOT NULL,
  `upro_acc_type` int(2) NOT NULL,
  `upro_company` varchar(50) NOT NULL,
  `upro_first_name` varchar(50) NOT NULL,
  `upro_last_name` varchar(50) NOT NULL,
  `upro_status_msg` varchar(50) NOT NULL,
  `upro_phone` varchar(25) NOT NULL,
  `upro_birthday` date NOT NULL DEFAULT 0,
  `upro_raw_url` varchar(100) NOT NULL,
  `upro_thumb_url_128` varchar(100) NOT NULL,
  `upro_featured` tinyint(1) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`upro_id`),
  UNIQUE KEY `upro_id` (`upro_id`),
  KEY `upro_uacc_fk` (`upro_uacc_fk`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for `tpp_user_stats`
-- ----------------------------
DROP TABLE IF EXISTS `tpp_user_stats`;
CREATE TABLE `tpp_user_stats` (
  `ustat_id` int(11) NOT NULL AUTO_INCREMENT,
  `ustat_uacc_fk` int(11) NOT NULL,
  `ustat_goals` int(11) NOT NULL DEFAULT 0,
  `ustat_assists` int(11) NOT NULL DEFAULT 0,
  `ustat_points` int(11) NOT NULL DEFAULT 0,   
  `ustat_penalty_mins` int(11) NOT NULL DEFAULT 0,
  `ustat_plus_minus` int(11) NOT NULL DEFAULT 0,
  `ustat_wins` int(11) NOT NULL DEFAULT 0,
  `ustat_losses` int(11) NOT NULL DEFAULT 0,
  `ustat_ties` int(11) NOT NULL DEFAULT 0,
  `ustat_ot_losses` int(11) NOT NULL DEFAULT 0,
  `ustat_gaa` decimal(6,3) NOT NULL DEFAULT 0,
  `ustat_save_percent` decimal(5,3) NOT NULL DEFAULT 0,
  `ustat_saves` int(11) NOT NULL DEFAULT 0,
  `ustat_position` int(2) NOT NULL DEFAULT 0,
  PRIMARY KEY (`ustat_id`),
  UNIQUE KEY `ustat_id` (`ustat_id`),
  KEY `ustat_uacc_fk` (`ustat_uacc_fk`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

