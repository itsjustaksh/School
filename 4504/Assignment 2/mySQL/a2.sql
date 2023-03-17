CREATE DATABASE aksh_ravi_syscbook
CREATE TABLE users_info (
	student_id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    student_email VARCHAR(150),
    f_name VARCHAR(150),
    l_name VARCHAR(150),
	bday DATE
);
ALTER TABLE users_info AUTO_INCREMENT=100100;
CREATE TABLE users_program (
	student_id INT(10) NOT NULL PRIMARY KEY,
    program VARCHAR(50),
    FOREIGN KEY(student_id) REFERENCES users_info(student_id)
);
CREATE TABLE users_avatar (
	student_id INT(10) NOT NULL PRIMARY KEY,
    avatar INT(1),
    FOREIGN KEY(student_id) REFERENCES users_info(student_id)
);
CREATE TABLE users_address (
	student_id INT(10) NOT NULL PRIMARY KEY,
    street_num INT(5),
    street_name VARCHAR(150),
    city VARCHAR(30),
	province VARCHAR(2),
    postal_code VARCHAR(7),
    FOREIGN KEY(student_id) REFERENCES users_info(student_id)
);
CREATE TABLE users_posts (
	post_id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    student_id INT(10),
    new_post TEXT(1000),
    post_date TIMESTAMP,
    FOREIGN KEY(student_id) REFERENCES users_info(student_id)
);