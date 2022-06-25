SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `equipa` (
  `id_equipa` int(11) NOT NULL,
  `sigla` varchar(10) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `torneio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `jogador` (
  `id_jogador` int(11) NOT NULL,
  `nome` int(11) NOT NULL,
  `data_nascimento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `jogo` (
  `id_jogo` int(11) NOT NULL,
  `equipa_a` int(11) NOT NULL,
  `equipa_b` int(11) NOT NULL,
  `equipa_a_score` int(11) NOT NULL,
  `equipa_b_score` int(11) NOT NULL,
  `data_realizacao` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `membros_equipa` (
  `equipa` int(11) NOT NULL,
  `jogador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `torneios` (
  `id_torneio` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `data_inicio` date NOT NULL,
  `data_fim` date NOT NULL,
  `local` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `equipa`
  ADD PRIMARY KEY (`id_equipa`),
  ADD KEY `torneio` (`torneio`);

ALTER TABLE `jogador`
  ADD PRIMARY KEY (`id_jogador`);

ALTER TABLE `jogo`
  ADD PRIMARY KEY (`id_jogo`),
  ADD KEY `equipa_a` (`equipa_a`),
  ADD KEY `equipa_b` (`equipa_b`);

ALTER TABLE `membros_equipa`
  ADD PRIMARY KEY (`equipa`,`jogador`),
  ADD KEY `jogador` (`jogador`);

ALTER TABLE `torneios`
  ADD PRIMARY KEY (`id_torneio`);


ALTER TABLE `equipa`
  ADD CONSTRAINT `equipa_ibfk_1` FOREIGN KEY (`torneio`) REFERENCES `torneios` (`id_torneio`);

ALTER TABLE `jogo`
  ADD CONSTRAINT `jogo_ibfk_1` FOREIGN KEY (`equipa_a`) REFERENCES `equipa` (`id_equipa`),
  ADD CONSTRAINT `jogo_ibfk_2` FOREIGN KEY (`equipa_b`) REFERENCES `equipa` (`id_equipa`);

ALTER TABLE `membros_equipa`
  ADD CONSTRAINT `membros_equipa_ibfk_1` FOREIGN KEY (`equipa`) REFERENCES `equipa` (`id_equipa`),
  ADD CONSTRAINT `membros_equipa_ibfk_2` FOREIGN KEY (`jogador`) REFERENCES `jogador` (`id_jogador`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
