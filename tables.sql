create table province (
	province_name varchar(10)
);
create table district (
	district_name varchar(20),
	province_name varchar(10)
);
create table municipality(
	municipality_name varchar(20),
	district_name varchar(20)
);