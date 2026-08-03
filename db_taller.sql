CREATE DATABASE taller_mecanico;
USE taller_mecanico;
create table Servicios(
    se_clave int auto_increment primary key,
    se_cliente varchar (100),
    se_vehiculo varchar (100),
    se_TipoServicio varchar (150),
    se_precio decimal (10,2)
    );
insert into Servicios(se_cliente, se_vehiculo, se_TipoServicio,se_precio)
    values
    ("Victor Galvan"," Koenigsegg Agera RS","Afinacion",12000),
    ("Anahi Rojas","Toyota Supra","Cambio de Balatas",3500);