
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tpp_user_activity`
-- ----------------------------
DROP TABLE IF EXISTS `tpp_user_activity`;
CREATE TABLE `tpp_user_activity` (
  `uact_id` int(11) NOT NULL AUTO_INCREMENT,
  `uact_uacc_fk` int(11) NOT NULL,
  `uact_type` int(2) NOT NULL,
  `uact_uacc_target` int(11) NOT NULL,
  `uact_data` text NOT NULL,
  `uact_cdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`uact_uacc_fk`, `uact_type`, `uact_uacc_target`),
  UNIQUE KEY `uact_id` (`uact_id`),
  KEY `uact_uacc_fk` (`uact_uacc_fk`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;


-- user updates his profile info
-- user adds media video
-- user updates profile image
-- user follows someone
-- user leaves a recommendation
-- user updates stats

