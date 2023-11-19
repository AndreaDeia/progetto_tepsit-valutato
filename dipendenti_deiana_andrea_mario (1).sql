-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Creato il: Nov 18, 2023 alle 12:50
-- Versione del server: 5.7.40-0ubuntu0.18.04.1
-- Versione PHP: 7.2.24-0ubuntu0.18.04.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5ATepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_deiana_andrea_mario`
--

CREATE TABLE `dipendenti_deiana_andrea_mario` (
  `id` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cognome` varchar(20) NOT NULL,
  `posizione_lavorativa` varchar(20) NOT NULL,
  `settore_di_lavoro` varchar(20) NOT NULL,
  `turno` varchar(10) NOT NULL,
  `data_di_assunzione` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='1- per il turno 1 = diurno, 2 = notturno.';

--
-- Dump dei dati per la tabella `dipendenti_deiana_andrea_mario`
--

INSERT INTO `dipendenti_deiana_andrea_mario` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `settore_di_lavoro`, `turno`, `data_di_assunzione`) VALUES
(1, 'andrea', 'deiana', 'produzione', 'primario', 'diurno', '2023-07-03'),
(2, 'andrea', 'mario', 'produzione', 'primario', 'notturno', '2023-07-04'),
(3, 'mario', 'deiana', 'produzione', 'secondario', 'diurno', '2023-07-05');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_deiana_andrea_mario`
--
ALTER TABLE `dipendenti_deiana_andrea_mario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_deiana_andrea_mario`
--
ALTER TABLE `dipendenti_deiana_andrea_mario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
