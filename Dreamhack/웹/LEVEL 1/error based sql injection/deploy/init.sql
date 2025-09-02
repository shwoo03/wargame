CREATE DATABASE IF NOT EXISTS `users`;
GRANT ALL PRIVILEGES ON users.* TO 'dbuser'@'localhost' IDENTIFIED BY 'dbpass';

USE `users`;
CREATE TABLE user(
  idx int auto_increment primary key,
  uid varchar(128) not null,
  upw varchar(128) not null
);

INSERT INTO user(uid, upw) values('admin', 'DH{**FLAG**}');
INSERT INTO user(uid, upw) values('guest', 'guest');
INSERT INTO user(uid, upw) values('test', 'test');
FLUSH PRIVILEGES;