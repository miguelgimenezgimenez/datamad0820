INSERT INTO CUSTOMER ( idCustomer, name, `phone number`, email, address,city,`state/province`,  country, `zip code`)
VALUES (1001, "PABLO PICASSO","+34636176382","EMAIL","PASEO DE LA CHOPERA,14","MADRID","MADRID","SPAIN","28045");
INSERT INTO CUSTOMER ( idCustomer, name, `phone number`, email, address,city,`state/province`,  country, `zip code`)
VALUES (2001, "Abraham Lincoln","+13059077086","email","120 SW 8th St","Miami","Florida","United States","33130");
INSERT INTO CUSTOMER ( idCustomer, name, `phone number`, email, address,city,`state/province`,  country, `zip code`)
VALUES (3001, "Napoleon Bonaparte","+33179754000","email","40,Rue du Colisee","Paris","Ile-de-France","France","75008");

INSERT INTO CAR ( VIN, Manufacturer, Model,Year, Color)
VALUES ("3K096I98581DHSNUP","Volkswagen","VINTiguan",2019,"Blue");
INSERT INTO CAR ( VIN, Manufacturer, Model,Year, Color)
VALUES ("ZM8G7BEUQZ97IH46V", "Peugeot","Rifter",2019,"Red");
INSERT INTO CAR ( VIN, Manufacturer, Model,Year, Color)
VALUES ("RKXVNNIHLVVZOUB4M", "Ford","Fusion",2018,"White");

INSERT INTO SALESPERSON (StaffId, name, Store)
VALUES (1, 'Petey Cruiser', 'Madrid');
INSERT INTO SALESPERSON (StaffId, name, Store)
VALUES (2, 'Anna Sthesia', 'Barcelona');
INSERT INTO SALESPERSON (StaffId, name, Store)
VALUES (3, 'Gail Forcewind	', 'Paris');
INSERT INTO SALESPERSON (StaffId, name, Store)
VALUES (4, 'Paige Turner', 'Mimia');

INSERT INTO INVOICE (
  `Invoice number`,
  Date,
  Car_VIN,
  Salesperson_StaffId,
  Customer_idCustomer
 )
VALUES (852399038, '2018-08-08', 'RKXVNNIHLVVZOUB4M', 1, 1001);

INSERT INTO INVOICE (
  `Invoice number`,
  Date,
 Car_VIN ,
  Salesperson_StaffId,
  Customer_idCustomer
 )
VALUES (731166526, '2018-12-12',  'ZM8G7BEUQZ97IH46V', 2, 2001);

INSERT INTO INVOICE (
  `Invoice number`,
  Date,
  Car_VIN,
  Salesperson_StaffId,
  Customer_idCustomer
 )
VALUES (271135104, '2019-01-01', '3K096I98581DHSNUP' , 3, 3001);