
create table Unit(
id int identity(1,1) primary key,
title varchar(10)
)

create table City(
id int identity(1,1) primary key,
title varchar(60)
)

create table Street(
city_id int foreign key (city_id) references City(id),
title varchar(60)
)

create table Categories(
id int identity(1,1) primary key,
title varchar(50),
slug varchar(max) 
)

create table Product(
id int identity(1,1) primary key ,
img varchar(max),
price money,
unit_id int foreign key (unit_id) references Unit(id),
cat_id int foreign key (cat_id) references Categories(id)
)

create table [User](
id  identity(1,1) int primary key,
last_name varchar(60),
first_name varchar(60),
tell varchar(11),
date_registration date default auto
)
create table [Order](
[user_id] int foreign key ([user_id]) references User(id),
product_id int foreign key (product_id) references Product(id),
count_ int ,
)
create table Sales (
id int identity(1,1) primary key,
product_id int foreign key (product_id) references Product(id),
[user_id] int foreign key ([user_id]) references User(id),
street_id int foreign key (street_id) references Street(id)
)
