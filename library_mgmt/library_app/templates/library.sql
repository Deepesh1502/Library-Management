use library_db;

#To Show the list of Tables
show Tables;

#Show Table of all books added 
select * from library_app_book;

#Show all issued books with id which is member_id
select * from library_app_issuedbook;

#Show the list of all library members
select * from library_app_member;