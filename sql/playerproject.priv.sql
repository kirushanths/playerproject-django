
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `user_groups`;
CREATE TABLE `user_groups` (
  `ugrp_id` smallint(5) NOT NULL AUTO_INCREMENT,
  `ugrp_name` varchar(20) NOT NULL,
  `ugrp_desc` varchar(100) NOT NULL,
  `ugrp_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`ugrp_id`),
  UNIQUE KEY `ugrp_id` (`ugrp_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_groups
-- ----------------------------
INSERT INTO `user_groups` VALUES ('1', 'Public', 'Public User : has no admin access rights.', '0');
INSERT INTO `user_groups` VALUES ('2', 'Moderator', 'Admin Moderator : has partial admin access rights.', '1');
INSERT INTO `user_groups` VALUES ('3', 'Master Admin', 'Master Admin : has full admin access rights.', '1');
INSERT INTO `user_groups` VALUES ('4', 'Public: Free', 'Free Acc: has no admin access rights.', '0');
INSERT INTO `user_groups` VALUES ('5', 'Public: Paid', 'Paid Acc: has no admin access rights.', '0');

-- ----------------------------
-- Table structure for `user_privileges`
-- ----------------------------
DROP TABLE IF EXISTS `user_privileges`;
CREATE TABLE `user_privileges` (
  `upriv_id` smallint(5) NOT NULL AUTO_INCREMENT,
  `upriv_name` varchar(20) NOT NULL,
  `upriv_desc` varchar(100) NOT NULL,
  PRIMARY KEY (`upriv_id`),
  UNIQUE KEY `upriv_id` (`upriv_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_privileges
-- ----------------------------
INSERT INTO `user_privileges` VALUES ('1', 'View Users', 'User can view user account details.');
INSERT INTO `user_privileges` VALUES ('2', 'View User Groups', 'User can view user groups.');
INSERT INTO `user_privileges` VALUES ('3', 'View Privileges', 'User can view privileges.');
INSERT INTO `user_privileges` VALUES ('4', 'Insert User Groups', 'User can insert new user groups.');
INSERT INTO `user_privileges` VALUES ('5', 'Insert Privileges', 'User can insert privileges.');
INSERT INTO `user_privileges` VALUES ('6', 'Update Users', 'User can update user account details.');
INSERT INTO `user_privileges` VALUES ('7', 'Update User Groups', 'User can update user groups.');
INSERT INTO `user_privileges` VALUES ('8', 'Update Privileges', 'User can update user privileges.');
INSERT INTO `user_privileges` VALUES ('9', 'Delete Users', 'User can delete user accounts.');
INSERT INTO `user_privileges` VALUES ('10', 'Delete User Groups', 'User can delete user groups.');
INSERT INTO `user_privileges` VALUES ('11', 'Delete Privileges', 'User can delete user privileges.');
INSERT INTO `user_privileges` VALUES ('12', 'View Full Profile', 'User can view full profiles');
INSERT INTO `user_privileges` VALUES ('13', 'RMS', 'User can use RMS system');

-- ----------------------------
-- Table structure for `user_privilege_users`
-- ----------------------------
DROP TABLE IF EXISTS `user_privilege_users`;
CREATE TABLE `user_privilege_users` (
  `upriv_users_id` smallint(5) NOT NULL AUTO_INCREMENT,
  `upriv_users_uacc_fk` int(11) NOT NULL,
  `upriv_users_upriv_fk` smallint(5) NOT NULL,
  PRIMARY KEY (`upriv_users_id`),
  UNIQUE KEY `upriv_users_id` (`upriv_users_id`) USING BTREE,
  KEY `upriv_users_uacc_fk` (`upriv_users_uacc_fk`),
  KEY `upriv_users_upriv_fk` (`upriv_users_upriv_fk`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_privilege_users
-- ----------------------------
INSERT INTO `user_privilege_users` VALUES ('1', '3', '1');
INSERT INTO `user_privilege_users` VALUES ('2', '3', '2');

-- ----------------------------
-- Table structure for `user_privilege_groups`
-- ----------------------------
DROP TABLE IF EXISTS `user_privilege_groups`;
CREATE TABLE `user_privilege_groups` (
  `upriv_groups_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `upriv_groups_ugrp_fk` smallint(5) unsigned NOT NULL,
  `upriv_groups_upriv_fk` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`upriv_groups_id`),
  UNIQUE KEY `upriv_groups_id` (`upriv_groups_id`) USING BTREE,
  KEY `upriv_groups_ugrp_fk` (`upriv_groups_ugrp_fk`),
  KEY `upriv_groups_upriv_fk` (`upriv_groups_upriv_fk`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;


-- ----------------------------
-- Records of user_privilege_groups
-- ----------------------------
INSERT INTO `user_privilege_groups` VALUES(1, 3, 1);
INSERT INTO `user_privilege_groups` VALUES(2, 3, 2);
INSERT INTO `user_privilege_groups` VALUES(3, 3, 3);
INSERT INTO `user_privilege_groups` VALUES(4, 3, 4);
INSERT INTO `user_privilege_groups` VALUES(5, 3, 5);
INSERT INTO `user_privilege_groups` VALUES(6, 3, 6);
INSERT INTO `user_privilege_groups` VALUES(7, 3, 7);
INSERT INTO `user_privilege_groups` VALUES(8, 3, 8);
INSERT INTO `user_privilege_groups` VALUES(9, 3, 9);
INSERT INTO `user_privilege_groups` VALUES(10, 3, 10);
INSERT INTO `user_privilege_groups` VALUES(11, 3, 11);
INSERT INTO `user_privilege_groups` VALUES(12, 3, 12);
INSERT INTO `user_privilege_groups` VALUES(13, 3, 13);

INSERT INTO `user_privilege_groups` VALUES(14, 2, 2);
INSERT INTO `user_privilege_groups` VALUES(15, 2, 4);
INSERT INTO `user_privilege_groups` VALUES(16, 2, 5);




