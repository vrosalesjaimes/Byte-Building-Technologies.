DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;
-----------------------------------------------------------------------------------------------------------
CREATE TYPE categoria as ENUM ('Pescado', 'Pizza', 'etc.');

CREATE TABLE Administrador(
 id_Administrador VARCHAR(50)  PRIMARY KEY,
 nombre VARCHAR(50) NOT NULL,
 apellidoP VARCHAR(50) NOT NULL,
 apellidoM VARCHAR(50) NOT NULL,
 edad int NOT NULL,
 contrasenia VARCHAR(50) NOT NULL
);

CREATE TABLE Encargado_Tableta (
 id_Encargado VARCHAR(50)  PRIMARY KEY,
 nombre VARCHAR(50) NOT NULL,
 apellidoP VARCHAR(50) NOT NULL,
 apellidoM VARCHAR(50) NOT NULL,
 edad int NOT NULL,
 contrasenia VARCHAR(50) NOT NULL
);

CREATE TABLE Menu(
 id_Menu VARCHAR(50) PRIMARY KEY,
 id_Admin VARCHAR(50) REFERENCES Administrador
);

CREATE TABLE Platillo (
 id_Platillo VARCHAR(50)  PRIMARY KEY,
 id_Administrador VARCHAR (50)REFERENCES administrador,
 id_menu VARCHAR(50) REFERENCES Menu,
 categoria categoria ,
 nombre VARCHAR(50) NOT NULL,
 costo int,
 descripcion text NOT NULL,
 imagen BYTEA
);

CREATE TABLE Tableta(
 id_Tableta VARCHAR(50) PRIMARY KEY,
 id_Encargado VARCHAR(50) REFERENCES Encargado_Tableta
);
CREATE TABLE Orden(
 id_Orden VARCHAR(50) PRIMARY KEY,
 id_Tableta VARCHAR(50) REFERENCES Tableta,
 fecha Date,
 hora time
);
CREATE TABLE Ordenar(
 id_Platillo VARCHAR(50) REFERENCES Platillo,
 id_orden VARCHAR(50) REFERENCES Orden
);
CREATE TABLE Account(
 mesa VARCHAR(10),
 ubicacion VARCHAR(20),
 is_staff boolean,
 is_active boolean,
 date_joined date,
 
);
CREATE TABLE Mesa(
 id_Mesa VARCHAR(50) PRIMARY KEY,
 ubicacion text, 
 contrasen text
);
CREATE TABLE Estar(
 id_Mesa VARCHAR(50) REFERENCES Mesa,
 id_Tableta VARCHAR(50) REFERENCES Tableta,
 fecha Date,
 ubicacion text
);
