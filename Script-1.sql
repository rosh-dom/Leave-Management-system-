use training;
-- create table leave_systems(id int primary key, 
-- description varchar(255), 
-- start_date varchar(30),
-- end_date varchar(30)
-- , status varchar(30)
-- );
-- ALTER table leave_system modify start_date varchar(30);
-- ALTER table leave_system modify end_date varchar(30);

alter table leave_systems  status set default 'Pending'


insert into leave_systems(id, description, start_date, end_date,status)
values (2,"Wedding", "4th april", "6th april","sucess");



select * from leave_systems;









