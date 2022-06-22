-- phpMyAdmin SQL Dump
-- version 5.0.4deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 23-Jun-2022 às 00:59
-- Versão do servidor: 10.5.15-MariaDB-0+deb11u1
-- versão do PHP: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `torneios`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `equipa`
--

CREATE TABLE `equipa` (
  `id_equipa` int(11) NOT NULL,
  `sigla` varchar(10) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `torneio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `jogador`
--

CREATE TABLE `jogador` (
  `id_jogador` int(11) NOT NULL,
  `nome` int(11) NOT NULL,
  `data_nascimento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `jogo`
--

CREATE TABLE `jogo` (
  `id_jogo` int(11) NOT NULL,
  `equipa_a` int(11) NOT NULL,
  `equipa_b` int(11) NOT NULL,
  `equipa_a_score` int(11) NOT NULL,
  `equipa_b_score` int(11) NOT NULL,
  `data_realizacao` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `membros_equipa`
--

CREATE TABLE `membros_equipa` (
  `equipa` int(11) NOT NULL,
  `jogador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `torneios`
--

CREATE TABLE `torneios` (
  `id_torneio` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `data_inicio` date NOT NULL,
  `data_fim` date NOT NULL,
  `local` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `equipa`
--
ALTER TABLE `equipa`
  ADD PRIMARY KEY (`id_equipa`),
  ADD KEY `torneio` (`torneio`);

--
-- Índices para tabela `jogador`
--
ALTER TABLE `jogador`
  ADD PRIMARY KEY (`id_jogador`);

--
-- Índices para tabela `jogo`
--
ALTER TABLE `jogo`
  ADD PRIMARY KEY (`id_jogo`),
  ADD KEY `equipa_a` (`equipa_a`),
  ADD KEY `equipa_b` (`equipa_b`);

--
-- Índices para tabela `membros_equipa`
--
ALTER TABLE `membros_equipa`
  ADD PRIMARY KEY (`equipa`,`jogador`),
  ADD KEY `jogador` (`jogador`);

--
-- Índices para tabela `torneios`
--
ALTER TABLE `torneios`
  ADD PRIMARY KEY (`id_torneio`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `equipa`
--
ALTER TABLE `equipa`
  ADD CONSTRAINT `equipa_ibfk_1` FOREIGN KEY (`torneio`) REFERENCES `torneios` (`id_torneio`);

--
-- Limitadores para a tabela `jogo`
--
ALTER TABLE `jogo`
  ADD CONSTRAINT `jogo_ibfk_1` FOREIGN KEY (`equipa_a`) REFERENCES `equipa` (`id_equipa`),
  ADD CONSTRAINT `jogo_ibfk_2` FOREIGN KEY (`equipa_b`) REFERENCES `equipa` (`id_equipa`);

--
-- Limitadores para a tabela `membros_equipa`
--
ALTER TABLE `membros_equipa`
  ADD CONSTRAINT `membros_equipa_ibfk_1` FOREIGN KEY (`equipa`) REFERENCES `equipa` (`id_equipa`),
  ADD CONSTRAINT `membros_equipa_ibfk_2` FOREIGN KEY (`jogador`) REFERENCES `jogador` (`id_jogador`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
