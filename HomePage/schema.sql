drop table if exists courses;
create table courses (
   id integer primary key autoincrement,
   course_name text not null
);

drop table if exists languages;
create table languages(
	id integer primary key autoincrement,
	language text not null	
);

drop table if exists work_experience;
create table work_experience(
	id integer primary key autoincrement,
	place text not null,
	location text not null,
	time_period text not null,
	role text not null,
	description
);

drop table if exists projects;
create table projects(
	id integer primary key autoincrement,
	project_description text not null
);

drop table if exists pass;
create table pass(
	id integer primary key autoincrement,
	password text not null
);