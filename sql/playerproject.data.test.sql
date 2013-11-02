
START TRANSACTION;

INSERT INTO `user_accounts` VALUES ('120', '1', 'james.reimer@tpp.com', 'j.reimer.test', '$2a$08$BVOlYrZedkIHf95Y9bRyQOu5mbJ6OIvoGGVUjg9T6YjGHxCpc7Fe.', '0.0.0.0', 'WknzHwK7K7', '', '', '0000-00-00 00:00:00', '', '', '1', '0', '0', '', '0000-00-00 00:00:00', '2012-04-12 21:15:05', '2011-01-01 00:00:00');
INSERT INTO `user_accounts` VALUES ('121', '1', 'wayne.gretzky@tpp.com', 'w.gretzky.test', '$2a$08$BVOlYrZedkIHf95Y9bRyQOu5mbJ6OIvoGGVUjg9T6YjGHxCpc7Fe.', '0.0.0.0', 'WknzHwK7K7', '', '', '0000-00-00 00:00:00', '', '', '1', '0', '0', '', '0000-00-00 00:00:00', '2012-04-12 21:15:05', '2011-01-01 00:00:00');
INSERT INTO `user_accounts` VALUES ('122', '1', 'drake@tpp.com', 'drake.test', '$2a$08$BVOlYrZedkIHf95Y9bRyQOu5mbJ6OIvoGGVUjg9T6YjGHxCpc7Fe.', '0.0.0.0', 'WknzHwK7K7', '', '', '0000-00-00 00:00:00', '', '', '1', '0', '0', '', '0000-00-00 00:00:00', '2012-04-12 21:15:05', '2011-01-01 00:00:00');
INSERT INTO `user_accounts` VALUES ('123', '1', 'mats.sundin@tpp.com', 'm.sundin.test', '$2a$08$BVOlYrZedkIHf95Y9bRyQOu5mbJ6OIvoGGVUjg9T6YjGHxCpc7Fe.', '0.0.0.0', 'WknzHwK7K7', '', '', '0000-00-00 00:00:00', '', '', '1', '0', '0', '', '0000-00-00 00:00:00', '2012-04-12 21:15:05', '2011-01-01 00:00:00');


INSERT INTO `tpp_user_profiles` VALUES ('0', '120', '1', '', 'James', 'Reimer', 'This is our year!', '416 123 3456', '1967-05-07', '', '', '0');
INSERT INTO `tpp_user_profiles` VALUES ('0', '121', '1', '', 'Wayne', 'Gretzky', 'Coming out of retirement next year!', '416 123 3456', '1967-05-07', '', '', '0');
INSERT INTO `tpp_user_profiles` VALUES ('0', '122', '1', '', 'Drizzy', 'Drake', 'You.Only.Live.Once', '416 123 3456', '1967-05-07', '', '', '0');
INSERT INTO `tpp_user_profiles` VALUES ('0', '123', '1', '', 'Mats', 'Sundin', 'Coming out of retirement next year!', '416 123 3456', '1967-05-07', '', '', '0');


INSERT INTO `tpp_user_stats` VALUES ('0', '120', '0', '0', '0', '0', '0', '364', '123', '23', '45', '1.88', '0.856', '1234', '7');
INSERT INTO `tpp_user_stats` VALUES ('0', '121', '34', '12', '56', '234', '34', '234', '123', '23', '45', '0', '0', '0', '1');
INSERT INTO `tpp_user_stats` VALUES ('0', '122', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');
INSERT INTO `tpp_user_stats` VALUES ('0', '123', '34', '12', '56', '234', '34', '234', '123', '23', '45', '0', '0', '0', '1');


INSERT INTO `tpp_user_following` VALUES ('0', '120', '121', '1', '0', '0', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_following` VALUES ('0', '120', '122', '1', '0', '0', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_following` VALUES ('0', '120', '123', '1', '0', '0', CURRENT_TIMESTAMP);

INSERT INTO `tpp_user_following` VALUES ('0', '121', '120', '1', '0', '0', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_following` VALUES ('0', '121', '122', '1', '0', '0', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_following` VALUES ('0', '121', '123', '1', '0', '0', CURRENT_TIMESTAMP);

INSERT INTO `tpp_user_following` VALUES ('0', '122', '121', '1', '0', '0', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_following` VALUES ('0', '122', '123', '1', '0', '0', CURRENT_TIMESTAMP);


INSERT INTO `tpp_user_comments` VALUES ('0', '120', '121', '1', '0', '0', '', 'Great power forward with masterful stick handling', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '120', '122', '1', '0', '0', '', 'Amazing talent! Went to his very first concert', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '120', '123', '1', '0', '0', '', 'Legendary Leafs player and will always be remembered', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '121', '120', '1', '0', '0', '', 'Great power forward with masterful stick handling', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '121', '122', '1', '0', '0', '', 'YMCMB >>>> MMG', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '121', '123', '1', '0', '0', '', 'Best Leafs center', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '123', '120', '1', '0', '0', '', 'Great power forward with masterful stick handling', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '123', '121', '1', '0', '0', '', 'YMCMB >>>> MMG', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_comments` VALUES ('0', '123', '122', '1', '0', '0', '', 'Best Leafs center', CURRENT_TIMESTAMP);


INSERT INTO `tpp_user_media` VALUES ('0', '120', 'HUGE Highlight Reel Save vs Bruins - May 10th 2013', '2', '0', '', 'uz6LlEVGO0Y');
INSERT INTO `tpp_user_media` VALUES ('0', '121', 'Legends of Hockey: Wayne Gretzky', '2', '0', '', 'WwBaF7D5DmE');
INSERT INTO `tpp_user_media` VALUES ('0', '121', 'Top 10 Wayne Gretzky Moments', '2', '0', '', 'tJBylN-RER0');
INSERT INTO `tpp_user_media` VALUES ('0', '121', 'Gretzky Highlight Video', '2', '0', '', 'XFX0dVXNDXw');
INSERT INTO `tpp_user_media` VALUES ('0', '122', '5 AM In Toronto (Official Video)', '2', '0', '', 'T4z4OrPmZgA');
INSERT INTO `tpp_user_media` VALUES ('0', '122', 'HYFR', '2', '0', '', '0KCWqnldEag');
INSERT INTO `tpp_user_media` VALUES ('0', '123', 'Mats Sundin - The Greatest Maple Leaf Ever', '2', '0', '', 'o94MbA9NmAA');
INSERT INTO `tpp_user_media` VALUES ('0', '123', 'Top 10 Mats Sundin Moments', '2', '0', '', 'pH0X0lM53o8');


INSERT INTO `tpp_user_activity` VALUES ('0', '120', '1', '120', 'upro_first_name, upro_status_msg', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '120', '2', '120', 'HUGE Highlight Reel Save vs Bruins - May 10th 2013', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '120', '4', '121', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '120', '4', '122', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '120', '4', '123', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '121', '1', '120', 'upro_first_name, upro_status_msg', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '121', '2', '121', 'Top 10 Wayne Gretzky Moments', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '121', '4', '120', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '121', '4', '122', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '121', '4', '123', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '122', '1', '122', 'upro_first_name, upro_status_msg', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '122', '2', '122', '5 AM In Toronto (Official Video)', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '122', '4', '121', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '122', '4', '123', '', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '123', '1', '123', 'upro_first_name, upro_status_msg', CURRENT_TIMESTAMP);
INSERT INTO `tpp_user_activity` VALUES ('0', '123', '2', '122', 'Top 10 Mats Sundin Moments', CURRENT_TIMESTAMP);

COMMIT;
