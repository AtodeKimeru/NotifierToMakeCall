CREATE DATABASE vacunaYdesparasitante;
USE vacunaYdesparasitante;

CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `propietario` varchar(50) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `raza` varchar(50) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `vacuna` varchar(100) DEFAULT NULL,
  `fechaVac` varchar(100),
  `desparasitante` varchar(100) DEFAULT NULL,
  `fechaDespar` varchar(100),
  PRIMARY KEY (`id`)
);

