CREATE DATABASE user_db CHARACTER SET utf8;
GRANT ALL PRIVILEGES ON user_db.* TO 'dbuser'@'localhost' IDENTIFIED BY 'dbpass';

USE `user_db`;
CREATE TABLE users (
  idx int auto_increment primary key,
  uid varchar(128) not null,
  upw varchar(128) not null
);

INSERT INTO users (uid, upw) values ('admin', 'DH{**FLAG**}');
INSERT INTO users (uid, upw) values ('guest', 'guest');
INSERT INTO users (uid, upw) values ('test', 'test');
FLUSH PRIVILEGES;
