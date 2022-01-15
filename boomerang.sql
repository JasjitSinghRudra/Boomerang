-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 25, 2020 at 08:36 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `boomerang`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `Username`, `Password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

DROP TABLE IF EXISTS `complaint`;
CREATE TABLE IF NOT EXISTS `complaint` (
  `name` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `message` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`name`, `email`, `message`) VALUES
('abc', 'abc@gmail.com', 'pls work'),
('abc', 'abc', 'abc\n'),
('Jasjit Rudra', 'rudra.jasjit@gmail.com', 'Is soup a drink or food. Following a debate and its arguments, I say whether we eat curd or drink it? it is kind of liquid too!\n'),
('Sunny Madarchod', 'sunnymc@gmail.com', 'i inserted a 10 inch dildo up my ass and its stuck there. Pls help\n'),
('', '', '\n'),
('abc', 'abc@gmail.com', 'Problem in payments\n'),
('abc', 'abc@gmail.com', 'bootstrap not working');

-- --------------------------------------------------------

--
-- Table structure for table `locationsearch`
--

DROP TABLE IF EXISTS `locationsearch`;
CREATE TABLE IF NOT EXISTS `locationsearch` (
  `Country` varchar(25) NOT NULL,
  `Tags` varchar(255) NOT NULL,
  PRIMARY KEY (`Country`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locationsearch`
--

INSERT INTO `locationsearch` (`Country`, `Tags`) VALUES
('Egypt', 'arabia, africa, desert, nile, pyramid, islam, city, redsea'),
('Mexico', 'pyramid, north america, desert, beach, city, democracy, latin, populated');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `First` varchar(30) NOT NULL,
  `Last` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Location` varchar(50) NOT NULL,
  `PIN` varchar(10) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`First`, `Last`, `Email`, `Location`, `PIN`, `Phone`, `Username`, `Password`) VALUES
('a', 'b', 'c@gmail.com', 'Berlin, Germany', '420691', '4563217098', 'abc', '123'),
('Bert', 'Maklin', 'maklinfbi@gmail.com', 'Parts Unknown', '000000', '9765234100', 'maklinbert', '123'),
('Bart', 'Simpson', 'simpbart@gmail.com', 'Springfield, USA', '02000000', '9211420111', 'simpbart', '123'),
('Xavier', 'Sanchez', 'xv@hotmail.com', 'Brazil', '123434', '7894653210', 'xvir', '12345'),
('Xavier', 'Jose', 'josexavier@hotmail.com', 'SÃ£o Paulo, Brazil', '01000456', '5541278965', 'josexavier', 'qazxsw'),
('John', 'Morrison', 'nitrojohn@yahoomail.com', 'California, United States', '93657', '1125478712', 'morrison', 'wwerawvssmackdown'),
('wasd', 'dfwe', 'wdebu@gmail.com', 'Florida, United States', '127602', '1122338643', 'wasdfw', 'nhytgb'),
('qw', 'qw', 'qw@gmail.com', 'fewefw', '12334231', '1239423760', 'qwertyuiop', 'qwertyuiop'),
('dfs', 'sdf', 'fds@gmail.com', 'edw', '21433232', '2314324440', 'sdfgh', 'sdfgh'),
('', '', '', '', '', '', 'abc@gmail.com', 'abc'),
('qwsa', 'qwsa', 'qwsa@hotmail.com', 'North Dakota, United States', '212321321', '9827272712', 'qwsa', 'qwsa');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
CREATE TABLE IF NOT EXISTS `payments` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `amount` int(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `name`, `amount`) VALUES
(1, 'Jason Brody', 136000),
(2, 'Timothy', 135090),
(3, 'John Deere', 133990),
(4, 'Erin', 123990),
(5, 'Frodo', 110090),
(6, 'Jim Dugan', 65599);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
