-- create table users
-- if not exists
CREATE TABLE `users` (
`id` INT( 25 ) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
`email` VARCHAR( 255 ) NOT NULL ,
`name` VARCHAR( 255 ) NOT NULL ,
UNIQUE (
`email`
)
);
