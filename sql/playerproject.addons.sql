
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tpp_user_media`
-- ----------------------------
DROP TABLE IF EXISTS `tpp_user_media`;
CREATE TABLE `tpp_user_media` (
  `umedi_id` int(11) NOT NULL AUTO_INCREMENT,
  `umedi_uacc_fk` int(11) NOT NULL,
  `umedi_caption` varchar(100) NOT NULL,
  `umedi_type` int(2) NOT NULL DEFAULT 0,
  `umedi_hidden` int(2) NOT NULL DEFAULT 0,
  `umedi_thumb_url` varchar(100) NOT NULL,
  `umedi_source` varchar(100) NOT NULL,
  PRIMARY KEY (`umedi_id`),
  UNIQUE KEY `umedi_id` (`umedi_id`),
  KEY `umedi_uacc_fk` (`umedi_uacc_fk`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;


-- ----------------------------
-- Table structure for `tpp_user_following`
-- ----------------------------
DROP TABLE IF EXISTS `tpp_user_following`;
CREATE TABLE `tpp_user_following` (
  `ufoll_id` int(11) NOT NULL AUTO_INCREMENT, 
  `ufoll_uacc_fk` int(11) NOT NULL,
  `ufoll_uacc_target` int(11) NOT NULL,
  `ufoll_approved` int(2) NOT NULL DEFAULT 0,
  `ufoll_blocked` int(2) NOT NULL DEFAULT 0,
  `ufoll_type` int(2) NOT NULL DEFAULT 0,
  `ufoll_cdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ufoll_uacc_fk`, `ufoll_uacc_target`),
  UNIQUE KEY `ufoll_id` (`ufoll_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for `tpp_user_comments`
-- ----------------------------
DROP TABLE IF EXISTS `tpp_user_comments`;
CREATE TABLE `tpp_user_comments` (
  `ucomm_id` int(11) NOT NULL AUTO_INCREMENT, 
  `ucomm_uacc_fk` int(11) NOT NULL,
  `ucomm_uacc_target` int(11) NOT NULL,
  `ucomm_approved` int(2) NOT NULL DEFAULT 0,
  `ucomm_hidden` int(2) NOT NULL DEFAULT 0,
  `ucomm_type` int(2) NOT NULL DEFAULT 0,
  `ucomm_meta` varchar(50) NOT NULL DEFAULT 0,
  `ucomm_body` text NOT NULL,
  `ucomm_cdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ucomm_uacc_fk`, `ucomm_uacc_target`),
  UNIQUE KEY `ucomm_id` (`ucomm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

