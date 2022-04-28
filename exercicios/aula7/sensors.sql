-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28-Abr-2022 às 12:41
-- Versão do servidor: 10.4.22-MariaDB
-- versão do PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sensors`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `alert`
--

CREATE TABLE `alert` (
  `idAlert` int(11) NOT NULL,
  `idSensor` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `description` varchar(45) NOT NULL,
  `cleared` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `location`
--

CREATE TABLE `location` (
  `idLocation` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `location`
--

INSERT INTO `location` (`idLocation`, `name`, `description`) VALUES
(1, 'Prometheus Server II', 'Prometheus Server @ lab. 163 / ISE /UAlg');

-- --------------------------------------------------------

--
-- Estrutura da tabela `reading`
--

CREATE TABLE `reading` (
  `idReading` int(11) NOT NULL,
  `idSensor` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `reading`
--

INSERT INTO `reading` (`idReading`, `idSensor`, `timestamp`, `value`) VALUES
(1, 1, '2022-03-29 14:56:41', 5.7),
(2, 1, '2022-03-29 14:56:42', 8.9),
(3, 1, '2022-03-29 14:56:43', 3.8),
(4, 1, '2022-03-29 14:56:44', 3),
(5, 1, '2022-03-29 14:56:45', 2.4),
(6, 1, '2022-03-29 14:56:46', 2.3),
(7, 1, '2022-03-29 14:56:47', 3),
(8, 1, '2022-03-29 14:56:48', 4.7),
(9, 1, '2022-03-29 14:56:49', 9.7),
(10, 1, '2022-03-29 14:56:50', 10.2),
(11, 1, '2022-03-29 14:56:51', 10.7),
(12, 1, '2022-03-29 14:56:52', 8.3),
(13, 1, '2022-03-29 14:56:53', 4.9),
(14, 1, '2022-03-29 14:56:54', 6.4),
(15, 1, '2022-03-29 14:56:55', 2.9),
(16, 1, '2022-03-29 14:56:56', 2.9),
(17, 1, '2022-03-29 14:56:57', 7.7),
(18, 1, '2022-03-29 14:56:58', 13.8),
(19, 1, '2022-03-29 14:56:59', 10.6),
(20, 1, '2022-03-29 14:57:00', 18.4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `sensor`
--

CREATE TABLE `sensor` (
  `idSensor` int(11) NOT NULL,
  `idLocation` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `unit` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `sensor`
--

INSERT INTO `sensor` (`idSensor`, `idLocation`, `name`, `unit`) VALUES
(1, 1, 'cpu_sensor_01', 'percent');

-- --------------------------------------------------------

--
-- Estrutura da tabela `unit`
--

CREATE TABLE `unit` (
  `unit` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `unit`
--

INSERT INTO `unit` (`unit`, `description`) VALUES
('percent', 'percentage of usage');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `alert`
--
ALTER TABLE `alert`
  ADD PRIMARY KEY (`idAlert`),
  ADD KEY `fk_Alert_Sensor1_idx` (`idSensor`);

--
-- Índices para tabela `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`idLocation`),
  ADD UNIQUE KEY `name_UNIQUE` (`name`);

--
-- Índices para tabela `reading`
--
ALTER TABLE `reading`
  ADD PRIMARY KEY (`idReading`),
  ADD KEY `fk_Reading_Sensor1_idx` (`idSensor`);

--
-- Índices para tabela `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`idSensor`),
  ADD UNIQUE KEY `uniq_loc_vs_sensor` (`idLocation`,`name`),
  ADD KEY `fk_Sensor_Location_idx` (`idLocation`),
  ADD KEY `fk_Sensor_Units1_idx` (`unit`);

--
-- Índices para tabela `unit`
--
ALTER TABLE `unit`
  ADD PRIMARY KEY (`unit`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `alert`
--
ALTER TABLE `alert`
  MODIFY `idAlert` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `location`
--
ALTER TABLE `location`
  MODIFY `idLocation` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `reading`
--
ALTER TABLE `reading`
  MODIFY `idReading` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de tabela `sensor`
--
ALTER TABLE `sensor`
  MODIFY `idSensor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `alert`
--
ALTER TABLE `alert`
  ADD CONSTRAINT `fk_Alert_Sensor1` FOREIGN KEY (`idSensor`) REFERENCES `sensor` (`idSensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `reading`
--
ALTER TABLE `reading`
  ADD CONSTRAINT `fk_Reading_Sensor1` FOREIGN KEY (`idSensor`) REFERENCES `sensor` (`idSensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `sensor`
--
ALTER TABLE `sensor`
  ADD CONSTRAINT `fk_Sensor_Location` FOREIGN KEY (`idLocation`) REFERENCES `location` (`idLocation`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Sensor_Units1` FOREIGN KEY (`unit`) REFERENCES `unit` (`unit`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
