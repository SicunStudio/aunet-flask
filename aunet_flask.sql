-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2016-11-16 09:09:20
-- 服务器版本： 5.7.16-0ubuntu0.16.04.1
-- PHP Version: 7.0.8-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aunet_flask`
--
CREATE DATABASE IF NOT EXISTS `aunet_flask` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `aunet_flask`;
-- --------------------------------------------------------

--
-- 表的结构 `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('6babb0d46bde');

-- --------------------------------------------------------

--
-- 表的结构 `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `remark` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `category`
--

INSERT INTO `category` (`id`, `name`, `remark`) VALUES
(1, 'news', NULL),
(2, 'notice', NULL),
(3, 'advance_notice', NULL),
(4, 'charm_association', NULL),
(5, 'pin_pai', NULL),
(6, 'charm_hust', NULL);

-- --------------------------------------------------------

--
-- 表的结构 `login_log`
--

CREATE TABLE `login_log` (
  `id` int(11) NOT NULL,
  `userName` varchar(64) DEFAULT NULL,
  `loginTime` varchar(25) DEFAULT NULL,
  `loginIp` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_colorprint`
--

CREATE TABLE `material_colorprint` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `is_sponsor` char(1) DEFAULT NULL,
  `remark` text,
  `time` varchar(5) DEFAULT NULL,
  `content` text,
  `resp_person` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_east4`
--

CREATE TABLE `material_east4` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `activity` varchar(15) DEFAULT NULL,
  `number` smallint(6) DEFAULT NULL,
  `sponsor` text,
  `opinion` varchar(10) DEFAULT NULL,
  `content` text,
  `resp_person` varchar(10) NOT NULL,
  `time` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_material`
--

CREATE TABLE `material_material` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `resp_person` varchar(10) NOT NULL,
  `activity` varchar(15) DEFAULT NULL,
  `opinion` varchar(20) DEFAULT NULL,
  `projector_date` date DEFAULT NULL,
  `projector_num` smallint(6) DEFAULT NULL,
  `chair_date` date DEFAULT NULL,
  `electricity_num` smallint(6) DEFAULT NULL,
  `desk_num` smallint(6) DEFAULT NULL,
  `chair_num` smallint(6) DEFAULT NULL,
  `trans_desk_num` smallint(6) DEFAULT NULL,
  `trans_chair_num` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_outdoor`
--

CREATE TABLE `material_outdoor` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `activity` varchar(15) DEFAULT NULL,
  `number` smallint(6) DEFAULT NULL,
  `sponsor` text,
  `opinion` varchar(10) DEFAULT NULL,
  `content` text,
  `resp_person` varchar(10) NOT NULL,
  `time` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_sacenter`
--

CREATE TABLE `material_sacenter` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `activity` varchar(15) DEFAULT NULL,
  `number` smallint(6) DEFAULT NULL,
  `sponsor` text,
  `opinion` varchar(10) DEFAULT NULL,
  `content` text,
  `resp_person` varchar(10) NOT NULL,
  `time` varchar(5) DEFAULT NULL,
  `is_query` char(1) DEFAULT NULL,
  `site_type` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_special`
--

CREATE TABLE `material_special` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `activity` varchar(15) DEFAULT NULL,
  `number` smallint(6) DEFAULT NULL,
  `sponsor` text,
  `opinion` varchar(10) DEFAULT NULL,
  `content` text,
  `resp_person` varchar(10) NOT NULL,
  `time` varchar(5) DEFAULT NULL,
  `is_query` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_sports`
--

CREATE TABLE `material_sports` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `school_id` varchar(10) DEFAULT NULL,
  `remark` text,
  `time` varchar(5) DEFAULT NULL,
  `resp_person` varchar(10) NOT NULL,
  `department` varchar(15) DEFAULT NULL,
  `content` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `material_teachingbuilding`
--

CREATE TABLE `material_teachingbuilding` (
  `id` int(11) NOT NULL,
  `apply_time` timestamp NULL DEFAULT NULL,
  `approve_time` timestamp NULL DEFAULT NULL,
  `result` char(1) NOT NULL,
  `applicant` varchar(10) NOT NULL,
  `advice` varchar(20) DEFAULT NULL,
  `pre_verify` varchar(20) DEFAULT NULL,
  `is_print` char(1) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `association` varchar(10) NOT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `content` text,
  `activity` varchar(15) DEFAULT NULL,
  `signature` varchar(10) DEFAULT NULL,
  `capacity` smallint(6) DEFAULT NULL,
  `number` smallint(6) DEFAULT NULL,
  `week` varchar(5) DEFAULT NULL,
  `person_type` char(5) DEFAULT NULL,
  `function` char(5) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `section` char(5) DEFAULT NULL,
  `activity_type` char(1) DEFAULT NULL,
  `host` varchar(10) DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `title` varchar(10) DEFAULT NULL,
  `resp_person` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `month` int(11) DEFAULT NULL,
  `day` int(11) DEFAULT NULL,
  `post_time` datetime DEFAULT NULL,
  `detail` text,
  `title` varchar(60) DEFAULT NULL,
  `outline` text,
  `img_url` varchar(40) DEFAULT NULL,
  `editable` tinyint(1) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `news`
--

INSERT INTO `news` (`id`, `year`, `month`, `day`, `post_time`, `detail`, `title`, `outline`, `img_url`, `editable`, `author`) VALUES
(53, 2016, 10, 27, '2016-10-27 17:35:54', '<body>hello world <img src="data:image/jpg;base64,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"/></body>', 'hello world', 'hello world ', 'static/Uploads/News1477594002.png', 1, '匿名'),
(54, 2016, 10, 27, '2016-10-27 17:51:32', '<body>hello world <img src="data:image/jpg;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAAAwCAMAAAChd4FcAAADAFBMVEUAAADi6OSMjIxSUlIrXja5trg8rFEDRhErokJ8w4pJrVxmZmYERRIinTn++P07nk/X0Naww7Stra0pdTj37/dlunUXWiS53L+ZmZmOy5pahGJKdVIQEBAsXzdni24VmC7MzMw1kEYzMzPZ4Nul1K6Wr5tWs2jp8eseaC0ufz5mZmaEoorI1cszpUkXTSJErFix2bi1tbVKSkp7e3skWC9wvn5zlHq6yL3S3dSXzqJBcEspKSnY6dxCQkLI486mvKulpaVAbUkTSx8ICAgjcDIhISHh7eM6Ojonnz1QsGP///+Dxo9Re1paWlqNqZOZzJmasJ6s1rMZGRk4pkx5wYYcYyodmzViuHPFxcVEtFl5mH/V3def0qlhh2rZ7d7F2MiEhIQ4Z0Lv8+/F4csvo0QbUidAp1OEoIoqfDozZjOx27kOSho6mkw2j0iftaMyi0S2xroSUiBrvHuFx5J0v4Lm7+eNqJOc0KVBq1TU59gpoEBskXRzc3Pg2N6tubDe5d99nYRNr1+ZmZkbWyg9pFHN18779/patWuZzJkzZT6Sq5e0xbfAz8OtvbUhazC12ryJpY6+3sXD0MbE4MmJyJUgVCtSsmXQ5tWjuKd5wobd8OEfYy0ZUCS9vb3v7+8LRxgtgD0xZzw1j0cnWjJiimp2mX2An4aUtZye1qkYmjDm5ube3t7W1tbk9+fM5NA4lEombjRWfl9Ke1K2270xhUGbs6BrjnI7akSY1aSrvq+5yr1Kc0q8zL/19fVrvXMxYjt5mX+1vbXCwsLDw8PExMTFxcXGxsbHx8fIyMjJycnKysrLy8vMzMzNzc3Ozs7Pz8/Q0NDR0dHS0tLT09PU1NTV1dXW1tbX19fY2NjZ2dna2trb29vc3Nzd3d3e3t7f39/g4ODh4eHi4uLj4+Pk5OTl5eXm5ubn5+fo6Ojp6enq6urr6+vs7Ozt7e3u7u7v7+/w8PDx8fHy8vLz8/P09PT19fX29vb39/f4+Pj5+fn6+vr7+/v8/Pz9/f3+/v7///8q44w1AAALfUlEQVR4nM2Z/1PTaB7Hw5dyhV4DlgELVC9CoexIhdLFBUqhtFLKA3WEIMQTPc1GzrmyKNgu33qHjPB0VnY4qqu45ybsrevOXdor6wh4OGb0T7snSVuSAgo/7OlnmCZ9SpJX3p9vT55gwidu2AHjEML/K8eBtg8gBMjQFkebj0+5BxCArNer2y9aW1v75s6/sXx0xgxAIBy7kntm4l7tuXPnaksnJk6cXBY+LqIKEMDxV4HSmxuL0/WiTS9u3Cx1d3ZA8LHoBDUgeFARqN2YVttXTwMVdR+RcBcQwtUzpRtIt0w7VfpDtdrNKH2SaS5+JBNeitZ07qMdaRzHkwc8uItybvwLOQGPENlpQFz4eb14dC+eaMXrc8qqAy5fuAx4nuAgvRSHHB+PiSQPLsxDoagIfYc8z8ViMFYkwHmCR7+B5guhb8tfv8brqqrqxqtwy5Mn3FEBceFF4NalffGQba5f2SXEl/redTazBtbAsZSGiBkpVxyCY32r5TTLGoiYBlAEGiJsNjamIQw8hN/2ne1bvn761e3TO8/7zraGtlfLTx42alKA8ErgpwP5pi/dCmynvQLmxsHXd6k40LAuinUVISAKx293/vn2vAFwhjgrAi4BA4dzNhvhogA4uQNCy+Xgwurqztll0He5bmeu4rA+TgKC0+sH6ydreD51z2B7C9z/BQEivfhYTARCgFXL1a/+pgGcrUhScAkiwJiB4uPzEJzsAHXj26D6/OrOH5dB+bflW6t9+JEAwWv3zffyoTg88yBJiD/ofNdXxbpYDW1gWSouK7jcev9Fs0ZjIzgX5VqiCEAZNGzcQNiQi9+0Pn/RcQXcXz3dcfYYePFFxfmfWw/JJwNC+tXF9+Mhu5c+J2jeqgIaIk5DuqhIkJICYdddqAJ0UQxCPs5zPEqCeDydJEtbIa4Zzs9XZV3mhSWhefzyEn0UQPB1YGz//FXYRqA65WQcQMjGxG+K5E6XGQhTJShdZtBvct0RN0Dq8kdREFre/prJV7+3IK5cpw+IbPyAgDpoXGaWtx9qUyIg2Noj4NipUxsZRfFSofuJfDKIZ9haGy4ov6dOvmbZRcXV/wApSj5ZjEryqk2tYEVGBG6Wun/4wV362eioYrDwx9/9LB0H18paFFYWDZFkA2iYbEraZK+sNN6vv5NibShTHQEh5/FIhKAbI9AWEjqVZSsBQfOjTWUKLz49c+XY0tLtuRv3CtMinlpxPypfki8c/INezzA+vV4/a2X0QwVCGcO0FDCzs7MMSWq1PtIryQSm9PlAVqydYfS7piXbALBjlVLQOjCN2PucmNpiQAE4PlGoStfcN7LMdddvLMoOFyc1X1clhYcJpEJBXu9Uy0jQGplqieJ4PzlZUHA8kShjIu3tD6/iCXN/f39DkBluQFvzcTzK1DSk7KW5gLxalJ1t6jKKjq1ECkobp/3aNbto4Ry73QWVCs6VKl1Z/GgpSQ/mc1fq6xdvXQw8234j7MaFqEmPFakAGpBGQIw/71peiaU3GCELgsFgG12AdPT5rPUk+vQxzEy7dnCtZSpp7RHyP92STGFENID57fZs2I0ZQFaWpEuOiVDHIN5Xq0iHMXe6ZQjgiXuzeOJMxVZWZlmwLJAJBNbvG0RRZmkIgTZyssVHktPTJOlroevzJvMH8yPk4/zBwcF665cJ7eDkEIoAq1arHRocJv9h04V1mKkr7dG4EzPEME824jNgUlQqk6SzWAH447OsdBZC+p/rb9/VwT1VC9ISIBABcfz4UI3XiwBng9GXL6PB2Sm6ftqLLjUix2CEaW/XNlkSibWI1TyTSHhryBkJxE+Ew2ET5g+HJQXnBzDMGQMOLEd5OUyAWW9vKgBXlG0cf9Bh2VtTIS0q2A5p3OwbRF+EfH1kbXSyxSqfwSoCioWnRZ8v3qsMCEOhUAlznA7RdA85g+P8gCkOdmOwG3MBPgfDBnIwTzwTMFcJeFHVxveZWULLZE9NzfQ0+qhZyCuoqXm8hn9f044Amcj3yCLMfoCDvT6rNQ8FAEk+jIgKOrFuSmwsDowFUrVxIcxsE3K3UaWICHhCCXhONRHapyfhbaTVisQSP1HMWa1MFDUy0cXaSfPIiHlScnFIcnGvKM6wCBhsaAoGF/ImS0rutNWQV4FfjDy/GhC1QB0adWUACvQrZQxufl61+w/0L9Xze0W8mpg5Pjp6fGatDTG1JWYgvNP0pXXQPGsVy6PVZ0ZJUmY2m5uY4X606WFQkkyKqJNMW/4CjfeQV0UQhwkLA6BUEIY9WKaEYhZXrCgACyfe7Wbx/d+7Py/v4DMYIQQJK7oQLpUZlAZXyQIzky+Yy0YW8sruNAiWacYnlxm9VGYSCW2TF+VPxDqSPxtsq8n7Ezagw3SUSQ2oqcSwRrZLraFYB7dLlXX65pnbSR5Q96i48Md77tyTxzg1I/hutgTNS5JlBn+pbRrxlYHvFrzD9XemR3C8YTA/P793mHzci7aDLfAhE4wMIVQrqjT6xxGyjYrZULLyUidJAtqMYmWEINaFeTioAtxSd5KVG+PS6gfY+fziKJrViH3k7dk3tKJSe+u1LSJZEjDf19Lri7ZrC7yR+jKSicr9TYpBeTeqDUZT3bjspZQkLgQomgOj5CxmjaZGKaF5p05dqMHSjVuqicuv7or7y8vVfe6VxeT4RvHExPW7dSkXCyVMvRemAGGogOxfqI/2+P4Oakhvr284eRvJLEZ7UW0JnTbvAiozEiBBUUQXZiQoAu/G7HEbEaeQEch4ZasThNYV9czqp9oJZBdvKcdOnZsIJHsMPckwZvHSuFkfROVkSl+CXB4Z+u7LYD3pDU37HuJJwO/TgKTSrBKgzrU7NzBmTBa60k6W5oPn3SofI1scG1vMGLq0EbgvAeLtPnJERmj4N9IIH1lo7yET//0XPjjE1FjAX0q88qxn6g9JBQVL8HGNwvJpKDYSqjJl3YTB0aU0v9LFAj7/rPgDj0yiFZ9ICR9NpC7cn2SJJkDRX/FQNGoRbHwqn0Jmb0oH9dQaNUmBNxLSg4Bkexb61BNWAdwNFH7wmWQssLr7TLK7gigdL/UsOeizKll0NfkHxdxY2oXyDnoscTUe9rFEfqoLnVj5oIBPv0nHBaCMRjSjBHEjkkEAtMGowUGlLm60CZBjeYHlNUZK/sGYnHmy86yRFSdmGqOLA7Fuk4E73KN78rm4I7D5ASd/FjiWvmVdZdg/kA2MDnvYpAOEIydcWck1DjTmmJzCPGYTPI6cRk8YUAN+e45JnDALnKkLDemAxdlo9zsoymEK80cBRJPWwMb7CC99tf48vbJgxFBvQR9+j4FnDZJveTvvrASAxQgeAWJ2AMImyBohRyBQERBtwDUP0HXFeL7RBOyOw65vJQGhUDEx9p61mQ33i/QjMNA5kPuyUAfI7u6qzKY9qHeKMYjKKyEDegxoYjIAeZ3TqTPZxaU6zoNardEEKx3+xka/DoQdR108AqHWiYM1/MpdQacTEZUwlIDZGG/PFoWMO50A9SfW6U8Dio3/mgl0OyDgPXbA8QjQKE6mgG4A3YvxGlLyiAqKhBWBzX2WL6X4W+/jFHcMw13+HIcNuAYadU4dXlXp1FXqYLdfpeC1AWDs8vtzuvwgu4uTAI0mgWt0oEMNwOXpjh1u+Wh3hRUIc4Hawn1EHHsaeK5+awJiBpZGfuVYQ1x0L4U2MB5DobbEcUWcUIQe2Pm4/G98EYwRghDnpSEIigwsuhQkbIdcwlSsUUOwcyJQXJih4lhx4JvlTH/AZGHdrYPJdQ4g/0F5F0pLxdLqRmpIrJ1yOTwcX8Yqv+WXZ4HaW7t9r3CzNpC7yh32ZL+Fqd+TQJBVXXHDXVpbfBNZbenEo4oL/Cf0nkQQEWHz1lxf59vc3M6+ufHL8BN70ySa1EB5nj/SMt5vZge87YSfzNvO/wHcaaRLhIAoxgAAAABJRU5ErkJggg=="/></body>', 'hello', 'hello world ', 'ddd', 1, '匿名'),
(55, 2016, 10, 27, '2016-10-27 17:55:24', '<body>hello world <img src="data:image/jpg;base64,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"/></body>', 'hello', 'hello world ', 'ddd', 1, '匿名'),
(56, 2016, 10, 27, '2016-10-27 17:57:22', '<body>hello world <img src="data:image/jpg;base64,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"/></body>', 'hello', 'hello world ', 'ddd', 1, '匿名'),
(57, 2016, 10, 27, '2016-10-27 18:22:18', '<body>\n hello world\n <img src="data:image/jpg;base64,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"/>\n</body>', 'hello', 'hello world ', 'ddd', 1, '匿名'),
(58, 2016, 10, 27, '2016-10-27 18:25:03', '<body>\n hello world\n <img src="data:image/jpg;base64,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"/>\n</body>', 'hello', 'hello world ', 'ddd', 1, '匿名'),
(59, 2016, 10, 27, '2016-10-27 18:26:27', '<body>\n hello world\n <img src="data:image/jpg;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAAAwCAMAAAChd4FcAAADAFBMVEUAAADi6OSMjIxSUlIrXja5trg8rFEDRhErokJ8w4pJrVxmZmYERRIinTn++P07nk/X0Naww7Stra0pdTj37/dlunUXWiS53L+ZmZmOy5pahGJKdVIQEBAsXzdni24VmC7MzMw1kEYzMzPZ4Nul1K6Wr5tWs2jp8eseaC0ufz5mZmaEoorI1cszpUkXTSJErFix2bi1tbVKSkp7e3skWC9wvn5zlHq6yL3S3dSXzqJBcEspKSnY6dxCQkLI486mvKulpaVAbUkTSx8ICAgjcDIhISHh7eM6Ojonnz1QsGP///+Dxo9Re1paWlqNqZOZzJmasJ6s1rMZGRk4pkx5wYYcYyodmzViuHPFxcVEtFl5mH/V3def0qlhh2rZ7d7F2MiEhIQ4Z0Lv8+/F4csvo0QbUidAp1OEoIoqfDozZjOx27kOSho6mkw2j0iftaMyi0S2xroSUiBrvHuFx5J0v4Lm7+eNqJOc0KVBq1TU59gpoEBskXRzc3Pg2N6tubDe5d99nYRNr1+ZmZkbWyg9pFHN18779/patWuZzJkzZT6Sq5e0xbfAz8OtvbUhazC12ryJpY6+3sXD0MbE4MmJyJUgVCtSsmXQ5tWjuKd5wobd8OEfYy0ZUCS9vb3v7+8LRxgtgD0xZzw1j0cnWjJiimp2mX2An4aUtZye1qkYmjDm5ube3t7W1tbk9+fM5NA4lEombjRWfl9Ke1K2270xhUGbs6BrjnI7akSY1aSrvq+5yr1Kc0q8zL/19fVrvXMxYjt5mX+1vbXCwsLDw8PExMTFxcXGxsbHx8fIyMjJycnKysrLy8vMzMzNzc3Ozs7Pz8/Q0NDR0dHS0tLT09PU1NTV1dXW1tbX19fY2NjZ2dna2trb29vc3Nzd3d3e3t7f39/g4ODh4eHi4uLj4+Pk5OTl5eXm5ubn5+fo6Ojp6enq6urr6+vs7Ozt7e3u7u7v7+/w8PDx8fHy8vLz8/P09PT19fX29vb39/f4+Pj5+fn6+vr7+/v8/Pz9/f3+/v7///8q44w1AAALfUlEQVR4nM2Z/1PTaB7Hw5dyhV4DlgELVC9CoexIhdLFBUqhtFLKA3WEIMQTPc1GzrmyKNgu33qHjPB0VnY4qqu45ybsrevOXdor6wh4OGb0T7snSVuSAgo/7OlnmCZ9SpJX3p9vT55gwidu2AHjEML/K8eBtg8gBMjQFkebj0+5BxCArNer2y9aW1v75s6/sXx0xgxAIBy7kntm4l7tuXPnaksnJk6cXBY+LqIKEMDxV4HSmxuL0/WiTS9u3Cx1d3ZA8LHoBDUgeFARqN2YVttXTwMVdR+RcBcQwtUzpRtIt0w7VfpDtdrNKH2SaS5+JBNeitZ07qMdaRzHkwc8uItybvwLOQGPENlpQFz4eb14dC+eaMXrc8qqAy5fuAx4nuAgvRSHHB+PiSQPLsxDoagIfYc8z8ViMFYkwHmCR7+B5guhb8tfv8brqqrqxqtwy5Mn3FEBceFF4NalffGQba5f2SXEl/redTazBtbAsZSGiBkpVxyCY32r5TTLGoiYBlAEGiJsNjamIQw8hN/2ne1bvn761e3TO8/7zraGtlfLTx42alKA8ErgpwP5pi/dCmynvQLmxsHXd6k40LAuinUVISAKx293/vn2vAFwhjgrAi4BA4dzNhvhogA4uQNCy+Xgwurqztll0He5bmeu4rA+TgKC0+sH6ydreD51z2B7C9z/BQEivfhYTARCgFXL1a/+pgGcrUhScAkiwJiB4uPzEJzsAHXj26D6/OrOH5dB+bflW6t9+JEAwWv3zffyoTg88yBJiD/ofNdXxbpYDW1gWSouK7jcev9Fs0ZjIzgX5VqiCEAZNGzcQNiQi9+0Pn/RcQXcXz3dcfYYePFFxfmfWw/JJwNC+tXF9+Mhu5c+J2jeqgIaIk5DuqhIkJICYdddqAJ0UQxCPs5zPEqCeDydJEtbIa4Zzs9XZV3mhSWhefzyEn0UQPB1YGz//FXYRqA65WQcQMjGxG+K5E6XGQhTJShdZtBvct0RN0Dq8kdREFre/prJV7+3IK5cpw+IbPyAgDpoXGaWtx9qUyIg2Noj4NipUxsZRfFSofuJfDKIZ9haGy4ov6dOvmbZRcXV/wApSj5ZjEryqk2tYEVGBG6Wun/4wV362eioYrDwx9/9LB0H18paFFYWDZFkA2iYbEraZK+sNN6vv5NibShTHQEh5/FIhKAbI9AWEjqVZSsBQfOjTWUKLz49c+XY0tLtuRv3CtMinlpxPypfki8c/INezzA+vV4/a2X0QwVCGcO0FDCzs7MMSWq1PtIryQSm9PlAVqydYfS7piXbALBjlVLQOjCN2PucmNpiQAE4PlGoStfcN7LMdddvLMoOFyc1X1clhYcJpEJBXu9Uy0jQGplqieJ4PzlZUHA8kShjIu3tD6/iCXN/f39DkBluQFvzcTzK1DSk7KW5gLxalJ1t6jKKjq1ECkobp/3aNbto4Ry73QWVCs6VKl1Z/GgpSQ/mc1fq6xdvXQw8234j7MaFqEmPFakAGpBGQIw/71peiaU3GCELgsFgG12AdPT5rPUk+vQxzEy7dnCtZSpp7RHyP92STGFENID57fZs2I0ZQFaWpEuOiVDHIN5Xq0iHMXe6ZQjgiXuzeOJMxVZWZlmwLJAJBNbvG0RRZmkIgTZyssVHktPTJOlroevzJvMH8yPk4/zBwcF665cJ7eDkEIoAq1arHRocJv9h04V1mKkr7dG4EzPEME824jNgUlQqk6SzWAH447OsdBZC+p/rb9/VwT1VC9ISIBABcfz4UI3XiwBng9GXL6PB2Sm6ftqLLjUix2CEaW/XNlkSibWI1TyTSHhryBkJxE+Ew2ET5g+HJQXnBzDMGQMOLEd5OUyAWW9vKgBXlG0cf9Bh2VtTIS0q2A5p3OwbRF+EfH1kbXSyxSqfwSoCioWnRZ8v3qsMCEOhUAlznA7RdA85g+P8gCkOdmOwG3MBPgfDBnIwTzwTMFcJeFHVxveZWULLZE9NzfQ0+qhZyCuoqXm8hn9f044Amcj3yCLMfoCDvT6rNQ8FAEk+jIgKOrFuSmwsDowFUrVxIcxsE3K3UaWICHhCCXhONRHapyfhbaTVisQSP1HMWa1MFDUy0cXaSfPIiHlScnFIcnGvKM6wCBhsaAoGF/ImS0rutNWQV4FfjDy/GhC1QB0adWUACvQrZQxufl61+w/0L9Xze0W8mpg5Pjp6fGatDTG1JWYgvNP0pXXQPGsVy6PVZ0ZJUmY2m5uY4X606WFQkkyKqJNMW/4CjfeQV0UQhwkLA6BUEIY9WKaEYhZXrCgACyfe7Wbx/d+7Py/v4DMYIQQJK7oQLpUZlAZXyQIzky+Yy0YW8sruNAiWacYnlxm9VGYSCW2TF+VPxDqSPxtsq8n7Ezagw3SUSQ2oqcSwRrZLraFYB7dLlXX65pnbSR5Q96i48Md77tyTxzg1I/hutgTNS5JlBn+pbRrxlYHvFrzD9XemR3C8YTA/P793mHzci7aDLfAhE4wMIVQrqjT6xxGyjYrZULLyUidJAtqMYmWEINaFeTioAtxSd5KVG+PS6gfY+fziKJrViH3k7dk3tKJSe+u1LSJZEjDf19Lri7ZrC7yR+jKSicr9TYpBeTeqDUZT3bjspZQkLgQomgOj5CxmjaZGKaF5p05dqMHSjVuqicuv7or7y8vVfe6VxeT4RvHExPW7dSkXCyVMvRemAGGogOxfqI/2+P4Oakhvr284eRvJLEZ7UW0JnTbvAiozEiBBUUQXZiQoAu/G7HEbEaeQEch4ZasThNYV9czqp9oJZBdvKcdOnZsIJHsMPckwZvHSuFkfROVkSl+CXB4Z+u7LYD3pDU37HuJJwO/TgKTSrBKgzrU7NzBmTBa60k6W5oPn3SofI1scG1vMGLq0EbgvAeLtPnJERmj4N9IIH1lo7yET//0XPjjE1FjAX0q88qxn6g9JBQVL8HGNwvJpKDYSqjJl3YTB0aU0v9LFAj7/rPgDj0yiFZ9ICR9NpC7cn2SJJkDRX/FQNGoRbHwqn0Jmb0oH9dQaNUmBNxLSg4Bkexb61BNWAdwNFH7wmWQssLr7TLK7gigdL/UsOeizKll0NfkHxdxY2oXyDnoscTUe9rFEfqoLnVj5oIBPv0nHBaCMRjSjBHEjkkEAtMGowUGlLm60CZBjeYHlNUZK/sGYnHmy86yRFSdmGqOLA7Fuk4E73KN78rm4I7D5ASd/FjiWvmVdZdg/kA2MDnvYpAOEIydcWck1DjTmmJzCPGYTPI6cRk8YUAN+e45JnDALnKkLDemAxdlo9zsoymEK80cBRJPWwMb7CC99tf48vbJgxFBvQR9+j4FnDZJveTvvrASAxQgeAWJ2AMImyBohRyBQERBtwDUP0HXFeL7RBOyOw65vJQGhUDEx9p61mQ33i/QjMNA5kPuyUAfI7u6qzKY9qHeKMYjKKyEDegxoYjIAeZ3TqTPZxaU6zoNardEEKx3+xka/DoQdR108AqHWiYM1/MpdQacTEZUwlIDZGG/PFoWMO50A9SfW6U8Dio3/mgl0OyDgPXbA8QjQKE6mgG4A3YvxGlLyiAqKhBWBzX2WL6X4W+/jFHcMw13+HIcNuAYadU4dXlXp1FXqYLdfpeC1AWDs8vtzuvwgu4uTAI0mgWt0oEMNwOXpjh1u+Wh3hRUIc4Hawn1EHHsaeK5+awJiBpZGfuVYQ1x0L4U2MB5DobbEcUWcUIQe2Pm4/G98EYwRghDnpSEIigwsuhQkbIdcwlSsUUOwcyJQXJih4lhx4JvlTH/AZGHdrYPJdQ4g/0F5F0pLxdLqRmpIrJ1yOTwcX8Yqv+WXZ4HaW7t9r3CzNpC7yh32ZL+Fqd+TQJBVXXHDXVpbfBNZbenEo4oL/Cf0nkQQEWHz1lxf59vc3M6+ufHL8BN70ySa1EB5nj/SMt5vZge87YSfzNvO/wHcaaRLhIAoxgAAAABJRU5ErkJggg=="/>\n</body>', 'hello', 'hello world ', 'static/Uploads/News1477593066.png', 1, '匿名'),
(60, 2016, 11, 16, '2016-11-16 00:55:38', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(61, 2016, 11, 16, '2016-11-16 00:55:38', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(62, 2016, 11, 16, '2016-11-16 00:55:38', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(63, 2016, 11, 16, '2016-11-16 00:55:38', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(64, 2016, 11, 16, '2016-11-16 00:55:38', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(65, 2016, 11, 16, '2016-11-16 00:59:49', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(66, 2016, 11, 16, '2016-11-16 00:59:49', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(67, 2016, 11, 16, '2016-11-16 00:59:49', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(68, 2016, 11, 16, '2016-11-16 00:59:49', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名'),
(69, 2016, 11, 16, '2016-11-16 00:59:49', '<body>good</body>', 'hello', 'hello', 'static/Uploads/News/1477594002.png', 1, '匿名');

-- --------------------------------------------------------

--
-- 表的结构 `news_category`
--

CREATE TABLE `news_category` (
  `news_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `news_category`
--

INSERT INTO `news_category` (`news_id`, `category_id`, `created_at`) VALUES
(54, 1, '2016-10-28 01:51:32'),
(55, 1, '2016-10-28 01:55:24'),
(56, 1, '2016-10-28 01:57:22'),
(57, 1, '2016-10-28 02:22:18'),
(58, 1, '2016-10-28 02:25:03'),
(59, 1, '2016-10-28 02:26:27'),
(53, 1, '2016-10-28 02:33:05'),
(60, 2, '2016-11-16 08:55:38'),
(60, 3, '2016-11-16 08:55:38'),
(60, 4, '2016-11-16 08:55:38'),
(60, 5, '2016-11-16 08:55:38'),
(60, 6, '2016-11-16 08:55:38'),
(65, 2, '2016-11-16 08:59:49'),
(66, 3, '2016-11-16 08:59:49'),
(67, 4, '2016-11-16 08:59:49'),
(68, 5, '2016-11-16 08:59:49'),
(69, 6, '2016-11-16 08:59:49');

-- --------------------------------------------------------

--
-- 表的结构 `news_tag`
--

CREATE TABLE `news_tag` (
  `news_id` int(11) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `news_tag`
--

INSERT INTO `news_tag` (`news_id`, `tag_id`, `created_at`) VALUES
(54, 1, '2016-10-28 01:51:32'),
(55, 1, '2016-10-28 01:55:24'),
(56, 1, '2016-10-28 01:57:22'),
(57, 1, '2016-10-28 02:22:18'),
(58, 1, '2016-10-28 02:25:03'),
(59, 1, '2016-10-28 02:26:27'),
(53, 1, '2016-10-28 02:33:05');

-- --------------------------------------------------------

--
-- 表的结构 `node`
--

CREATE TABLE `node` (
  `id` int(11) NOT NULL,
  `nodeName` varchar(20) DEFAULT NULL,
  `remark` varchar(20) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `node`
--

INSERT INTO `node` (`id`, `nodeName`, `remark`, `status`, `level`) VALUES
(1, '添加用户', NULL, 1, 1),
(2, '修改用户', NULL, 1, 1),
(3, '删除用户', NULL, 1, 1),
(4, '添加角色', NULL, 1, 1),
(5, '修改角色', NULL, 1, 1),
(6, '删除角色', NULL, 1, 1),
(7, '添加新闻', NULL, 1, 1),
(8, '修改新闻', NULL, 1, 1),
(9, '删除新闻', NULL, 1, 1),
(10, '添加新闻属性', NULL, 1, 1),
(11, '修改新闻属性', NULL, 1, 1),
(12, '删除新闻属性', NULL, 1, 1),
(13, '添加新闻标签', NULL, 1, 1),
(14, '修改新闻标签', NULL, 1, 1),
(15, '删除新闻标签', NULL, 1, 1),
(16, '修改节点', NULL, 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `roleName` varchar(20) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `remark` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `role`
--

INSERT INTO `role` (`id`, `roleName`, `status`, `remark`) VALUES
(1, '超管', 1, NULL),
(2, '前台', 1, NULL),
(3, '后台', 1, NULL),
(4, '次管', 1, NULL),
(5, '次次管', 1, NULL),
(6, '次次次管', 1, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `role_node`
--

CREATE TABLE `role_node` (
  `node_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `role_node`
--

INSERT INTO `role_node` (`node_id`, `role_id`, `created_at`) VALUES
(1, 1, '2016-10-27 01:39:22'),
(3, 1, '2016-10-27 01:43:46'),
(2, 1, '2016-10-27 01:43:46'),
(4, 1, '2016-10-27 01:43:46'),
(5, 1, '2016-10-27 01:43:46'),
(6, 1, '2016-10-27 01:43:46'),
(7, 1, '2016-10-27 01:43:46'),
(8, 1, '2016-10-27 01:43:46'),
(9, 1, '2016-10-27 01:43:46'),
(10, 1, '2016-10-27 01:43:46'),
(11, 1, '2016-10-27 01:43:46'),
(12, 1, '2016-10-27 01:43:46'),
(13, 1, '2016-10-27 01:43:46'),
(14, 1, '2016-10-27 01:43:46'),
(15, 1, '2016-10-27 01:43:46'),
(16, 1, '2016-10-27 01:43:46'),
(2, 6, '2016-10-28 02:57:35');

-- --------------------------------------------------------

--
-- 表的结构 `silder_show`
--

CREATE TABLE `silder_show` (
  `id` int(11) NOT NULL,
  `title` varchar(60) DEFAULT NULL,
  `img_url` varchar(40) DEFAULT NULL,
  `outline` text,
  `post_time` datetime DEFAULT NULL,
  `link` varchar(30) DEFAULT NULL,
  `editable` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `silder_show`
--

INSERT INTO `silder_show` (`id`, `title`, `img_url`, `outline`, `post_time`, `link`, `editable`) VALUES
(1, 'hellosfs', NULL, 'hello', NULL, 'https://www.google.com', 1),
(2, 'hellosfs', '1.jpg', 'hello', '2016-10-27 18:47:54', 'https://www.google.com', 1),
(3, 'good', 'static/Uploads/News/1477594002.png', 'dood', '2016-11-16 00:59:49', 'http://www.google.com', 1),
(4, 'good', 'static/Uploads/News/1477594002.png', 'dood', '2016-11-16 01:01:49', 'http://www.google.com', 1),
(5, 'good', 'static/Uploads/News/1477594002.png', 'dood', '2016-11-16 01:01:51', 'http://www.google.com', 1),
(6, 'good', 'static/Uploads/News/1477594002.png', 'dood', '2016-11-16 01:01:53', 'http://www.google.com', 1),
(7, 'good', 'static/Uploads/News/1477594002.png', 'dood', '2016-11-16 01:01:56', 'http://www.google.com', 1);

-- --------------------------------------------------------

--
-- 表的结构 `tag`
--

CREATE TABLE `tag` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `tag`
--

INSERT INTO `tag` (`id`, `name`) VALUES
(1, 'news');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `userName` varchar(64) DEFAULT NULL,
  `passWord` varchar(128) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `remark` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `userName`, `passWord`, `email`, `status`, `remark`) VALUES
(2, '思存', 'pbkdf2:sha1:1000$gpZhYu29$1e7eb0c937aae5e52bd682adb2dc7014a1c2abcc', '1412511544@qq.com', 1, NULL),
(3, 'admin', 'pbkdf2:sha1:1000$Magl3nmf$19f89915cdf2f26fcfe922ffcb4cee3e3dcb0227', NULL, 1, NULL),
(5, 'ly', 'pbkdf2:sha1:1000$eaAMVds0$40848acac5afb045ee95372435995dfb6bb2acc0', NULL, 1, NULL),
(6, 'lyjdwh', 'pbkdf2:sha1:1000$0YGw920F$2d39a3bf1e16c0dc267b5194bb0b5157f26346cf', NULL, 1, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `user_role`
--

CREATE TABLE `user_role` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user_role`
--

INSERT INTO `user_role` (`user_id`, `role_id`, `created_at`) VALUES
(2, 1, '2016-10-27 02:02:07'),
(3, 1, '2016-11-09 08:55:05'),
(5, 1, '2016-11-09 08:57:44'),
(6, 1, '2016-11-09 08:58:14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `login_log`
--
ALTER TABLE `login_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_colorprint`
--
ALTER TABLE `material_colorprint`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_east4`
--
ALTER TABLE `material_east4`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_material`
--
ALTER TABLE `material_material`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_outdoor`
--
ALTER TABLE `material_outdoor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_sacenter`
--
ALTER TABLE `material_sacenter`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_special`
--
ALTER TABLE `material_special`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_sports`
--
ALTER TABLE `material_sports`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material_teachingbuilding`
--
ALTER TABLE `material_teachingbuilding`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `news_category`
--
ALTER TABLE `news_category`
  ADD KEY `category_id` (`category_id`),
  ADD KEY `news_id` (`news_id`);

--
-- Indexes for table `news_tag`
--
ALTER TABLE `news_tag`
  ADD KEY `news_id` (`news_id`),
  ADD KEY `tag_id` (`tag_id`);

--
-- Indexes for table `node`
--
ALTER TABLE `node`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nodeName` (`nodeName`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roleName` (`roleName`);

--
-- Indexes for table `role_node`
--
ALTER TABLE `role_node`
  ADD KEY `node_id` (`node_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `silder_show`
--
ALTER TABLE `silder_show`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tag`
--
ALTER TABLE `tag`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_user_userName` (`userName`);

--
-- Indexes for table `user_role`
--
ALTER TABLE `user_role`
  ADD KEY `role_id` (`role_id`),
  ADD KEY `user_id` (`user_id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- 使用表AUTO_INCREMENT `login_log`
--
ALTER TABLE `login_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_colorprint`
--
ALTER TABLE `material_colorprint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_east4`
--
ALTER TABLE `material_east4`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_material`
--
ALTER TABLE `material_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_outdoor`
--
ALTER TABLE `material_outdoor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_sacenter`
--
ALTER TABLE `material_sacenter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_special`
--
ALTER TABLE `material_special`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_sports`
--
ALTER TABLE `material_sports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `material_teachingbuilding`
--
ALTER TABLE `material_teachingbuilding`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;
--
-- 使用表AUTO_INCREMENT `node`
--
ALTER TABLE `node`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- 使用表AUTO_INCREMENT `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- 使用表AUTO_INCREMENT `silder_show`
--
ALTER TABLE `silder_show`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- 使用表AUTO_INCREMENT `tag`
--
ALTER TABLE `tag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- 限制导出的表
--

--
-- 限制表 `news_category`
--
ALTER TABLE `news_category`
  ADD CONSTRAINT `news_category_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  ADD CONSTRAINT `news_category_ibfk_2` FOREIGN KEY (`news_id`) REFERENCES `news` (`id`);

--
-- 限制表 `news_tag`
--
ALTER TABLE `news_tag`
  ADD CONSTRAINT `news_tag_ibfk_1` FOREIGN KEY (`news_id`) REFERENCES `news` (`id`),
  ADD CONSTRAINT `news_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`);

--
-- 限制表 `role_node`
--
ALTER TABLE `role_node`
  ADD CONSTRAINT `role_node_ibfk_1` FOREIGN KEY (`node_id`) REFERENCES `node` (`id`),
  ADD CONSTRAINT `role_node_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

--
-- 限制表 `user_role`
--
ALTER TABLE `user_role`
  ADD CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`),
  ADD CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
