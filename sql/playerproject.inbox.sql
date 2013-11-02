-- NEW STRUCTURE

-- messages
--     message_id
--     message_type
--     sender_id
--     timestamp

-- message_recipient
--     message_id
--     user_id

-- message_status
--     message_status_id
--     message_id
--     user_id
--     is_read
--     read_datetime
--     is_deleted
--     deleted_datetime

DROP TABLE IF EXISTS `tpp_msg_messages`;
CREATE TABLE `tpp_msg_messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text NOT NULL,
  `priority` int(2) NOT NULL DEFAULT '0',
  `sender_id` int(11) NOT NULL,
  `cdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `tpp_msg_recipient`;
CREATE TABLE `tpp_msg_recipient` (
  `message_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`message_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `tpp_msg_status`;
CREATE TABLE `tpp_msg_status` (
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `status` int(2) NOT NULL,
  `rdate` timestamp NOT NULL DEFAULT '0',
  PRIMARY KEY (`message_id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
