

CREATE TABLE member (
	member_id	VARCHAR(100) NOT NULL,
	member_account	VARCHAR(50) NOT NULL UNIQUE,
	member_password	VARCHAR(50) NOT NULL,
	member_roles	INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY (member_id)
);
CREATE TABLE membertype (
	role_code	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	role_description	TEXT NOT NULL
);

CREATE TABLE sales (
	sales_id VARCHAR(100) NOT NULL ,
	member_id VARCHAR(100) NOT NULL,
	number_of_ticket	INTEGER NOT NULL,
	time_of_sales datetime NOT NULL,
	event_id VARCHAR(100) NOT NULL,

	PRIMARY KEY (sales_id)
);

CREATE TABLE eventtype(
	type_code	INTEGER PRIMARY KEY AUTOINCREMENT,
	type_description	TEXT NOT NULL 
);
CREATE TABLE event(
	event_id VARCHAR(100) NOT NULL,
	event_name VARCHAR(100) NOT NULL,
	event_type INTEGER NOT NULL DEFAULT 1,
	event_description TEXT,
	event_date datetime NOT NULL,
	starting_time datetime NOT NULL,
	ending_time TEXT NOT NULL,
	sale_roles INTEGER,
	sales_limit INTEGER,
	sales_per_member INTEGER,

	PRIMARY KEY (event_id)
);