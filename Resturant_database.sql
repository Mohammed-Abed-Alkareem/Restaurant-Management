-- Creation of tables for Resturant Project

create database Resturant;
use Resturant;

create table Orders(order_id int, order_data date,customer_id INT, table_code INT, payment_type varchar(20),
					 PRIMARY KEY (order_id), foreign key (customer_id) REFERENCES Customers (customer_id), 
                     foreign key (table_code) references Tables(table_code),
                     foreign key (payment_type) references Payment_Method (payment));

create table Customers(customer_id INT, customer_name VARCHAR(20), customer_phone VARCHAR(20), 
					    PRIMARY KEY (customer_id));

create table Rate(rate_id INT, order_id INT, PRIMARY KEY (rate_id),FOREIGN KEY (order_id) REFERENCES Orders (order_id));

create table Tables(class varchar(20), num_of_seats int, location varchar(20), table_code INT,
					 primary key (table_code)); 

create table Payment_Method(payment varchar(20) primary key);

create table Menu_Items(name varchar(20), description varchar(100), item_id int, category varchar(30), price INT,
						 primary key (item_id));
                         
create table Order_Details(id int, quantity int, price float, item_id int,
							primary key (id), foreign key (item_id) references Menu_Items (item_id));
