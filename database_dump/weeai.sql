-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2023 at 01:08 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `weeai`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add x image', 7, 'add_ximage'),
(26, 'Can change x image', 7, 'change_ximage'),
(27, 'Can delete x image', 7, 'delete_ximage'),
(28, 'Can view x image', 7, 'view_ximage'),
(29, 'Can add x segmentation result', 8, 'add_xsegmentationresult'),
(30, 'Can change x segmentation result', 8, 'change_xsegmentationresult'),
(31, 'Can delete x segmentation result', 8, 'delete_xsegmentationresult'),
(32, 'Can view x segmentation result', 8, 'view_xsegmentationresult');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$g0ZJ4lADh8LN2AISLxhAgq$79ZhIRnAcR1TvEVSEEnbOtVENh0I85OSg/lSUfYYGtY=', '2023-05-16 18:00:53.798980', 1, 'admin', '', '', 'iki.mukti@gmail.com', 1, 1, '2023-04-04 20:00:31.074651');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-04-04 20:01:43.206393', '1', '1 - asdasd', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-04-04 20:01:46.162365', '2', '2 - asfasdf', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-04-04 20:14:45.470940', '3', '3 - asd23523', 1, '[{\"added\": {}}]', 7, 1),
(4, '2023-04-04 20:14:48.384491', '4', '4 - wreygy53', 1, '[{\"added\": {}}]', 7, 1),
(5, '2023-04-04 20:14:52.163984', '5', '5 - rfa43gt', 1, '[{\"added\": {}}]', 7, 1),
(6, '2023-04-04 20:14:55.227743', '6', '6 - wegvsertt', 1, '[{\"added\": {}}]', 7, 1),
(7, '2023-04-04 20:14:58.523759', '7', '7 - rsahgeth', 1, '[{\"added\": {}}]', 7, 1),
(8, '2023-04-08 02:36:00.843916', '120', '120 - asd', 1, '[{\"added\": {}}]', 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'myapp', 'ximage'),
(8, 'myapp', 'xsegmentationresult'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-04 19:55:10.804257'),
(2, 'auth', '0001_initial', '2023-04-04 19:55:11.107268'),
(3, 'admin', '0001_initial', '2023-04-04 19:55:11.165792'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-04 19:55:11.171793'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-04 19:55:11.176767'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-04 19:55:11.210315'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-04 19:55:11.238026'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-04-04 19:55:11.249030'),
(9, 'auth', '0004_alter_user_username_opts', '2023-04-04 19:55:11.257031'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-04-04 19:55:11.280036'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-04-04 19:55:11.282036'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-04 19:55:11.288037'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-04-04 19:55:11.299040'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-04 19:55:11.311046'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-04-04 19:55:11.321333'),
(16, 'auth', '0011_update_proxy_permissions', '2023-04-04 19:55:11.327335'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-04 19:55:11.340158'),
(18, 'myapp', '0001_initial', '2023-04-04 19:55:11.355161'),
(19, 'myapp', '0002_alter_ximage_uploader', '2023-04-04 19:55:11.376165'),
(20, 'sessions', '0001_initial', '2023-04-04 19:55:11.402057'),
(21, 'myapp', '0003_ximage_date', '2023-04-04 20:11:32.005575'),
(22, 'myapp', '0004_ximage_slug', '2023-04-07 11:14:12.002752'),
(23, 'myapp', '0005_remove_ximage_title', '2023-04-08 01:35:44.547278'),
(24, 'myapp', '0006_ximage_published_ximage_updated', '2023-04-08 01:39:21.173906'),
(25, 'myapp', '0007_remove_ximage_published_remove_ximage_updated', '2023-04-08 02:36:52.606022'),
(26, 'myapp', '0008_xsegmentationresult', '2023-04-08 04:32:49.429122');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('00vyk593xgqdlzw2d9rhsh6oyt9h9qn1', '.eJxVjMsOwiAQRf-FtSHMlPJw6d5vIMAMUjU0Ke3K-O_apAvd3nPOfYkQt7WGrfMSJhJnAeL0u6WYH9x2QPfYbrPMc1uXKcldkQft8joTPy-H-3dQY6_f2irURWUPowODnk3CwoMZ0fhsowMCcFqpUgoRmIKZXLKcbFaEQ9JGvD_EHDei:1pkxSn:6vHezgu0VEsozmLOQi_ubzAYEixuR6nTdVuIq6lUCMc', '2023-04-22 01:33:57.929188'),
('09f2y9uubbks2oh3elf08gr775ihfszd', '.eJxVjMsOwiAQRf-FtSHMlPJw6d5vIMAMUjU0Ke3K-O_apAvd3nPOfYkQt7WGrfMSJhJnAeL0u6WYH9x2QPfYbrPMc1uXKcldkQft8joTPy-H-3dQY6_f2irURWUPowODnk3CwoMZ0fhsowMCcFqpUgoRmIKZXLKcbFaEQ9JGvD_EHDei:1pyvcK:eneEl66yxba45l20CB8kiLDDfvbYfYGud-zwrHC9bSc', '2023-05-30 14:25:32.849245'),
('23h5tm14zgz8vp0unmhcefldgxl2hz2s', '.eJxVjMsOwiAQRf-FtSHMlPJw6d5vIMAMUjU0Ke3K-O_apAvd3nPOfYkQt7WGrfMSJhJnAeL0u6WYH9x2QPfYbrPMc1uXKcldkQft8joTPy-H-3dQY6_f2irURWUPowODnk3CwoMZ0fhsowMCcFqpUgoRmIKZXLKcbFaEQ9JGvD_EHDei:1pjmqL:zhqRD3Rro4GAhnAOA7Elb2HFJgGmBk5_V29LmcPmVoo', '2023-04-18 20:01:25.329632'),
('3vipxazh29fmwv9nflr6bx19lxxxrzzy', '.eJxVjMsOwiAQRf-FtSHMlPJw6d5vIMAMUjU0Ke3K-O_apAvd3nPOfYkQt7WGrfMSJhJnAeL0u6WYH9x2QPfYbrPMc1uXKcldkQft8joTPy-H-3dQY6_f2irURWUPowODnk3CwoMZ0fhsowMCcFqpUgoRmIKZXLKcbFaEQ9JGvD_EHDei:1pyyyj:atS23ZVhkIvMrjfVo6nT8DmhFnT4Cjx6mRu9YSLgijs', '2023-05-30 18:00:53.803981'),
('hu5ayd8z2ayiy70jwhxbzyfk7sjpahai', '.eJxVjMsOwiAQRf-FtSHMlPJw6d5vIMAMUjU0Ke3K-O_apAvd3nPOfYkQt7WGrfMSJhJnAeL0u6WYH9x2QPfYbrPMc1uXKcldkQft8joTPy-H-3dQY6_f2irURWUPowODnk3CwoMZ0fhsowMCcFqpUgoRmIKZXLKcbFaEQ9JGvD_EHDei:1pl02C:9b7Spzt1j5wn-osVk5tXKWRKT3D2VD7yjb_Aa13ze3M', '2023-04-22 04:18:40.190516'),
('iak9cb6zdegw2hnmvfae7yv1wb23ronm', '.eJxVjMsOwiAQRf-FtSHMlPJw6d5vIMAMUjU0Ke3K-O_apAvd3nPOfYkQt7WGrfMSJhJnAeL0u6WYH9x2QPfYbrPMc1uXKcldkQft8joTPy-H-3dQY6_f2irURWUPowODnk3CwoMZ0fhsowMCcFqpUgoRmIKZXLKcbFaEQ9JGvD_EHDei:1pyA8d:aqZZXcNnUc3K6PsSX6a7IADlEijBpDkYDcTyuZFOaus', '2023-05-28 11:43:43.690203');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_ximage`
--

CREATE TABLE `myapp_ximage` (
  `id` int(11) NOT NULL,
  `pathImage` varchar(100) NOT NULL,
  `uploader` varchar(100) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `slug` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_ximage`
--

INSERT INTO `myapp_ximage` (`id`, `pathImage`, `uploader`, `date`, `slug`) VALUES
(1290, '0926119bbb910f5991aec4e2630e0df120230408113850.jpg', 'Mukti', '2023-04-08 04:38:50.624674', '0926119bbb910f5991aec4e2630e0df120230408113850jpg'),
(1291, '31587786219cd19816efb1f5bec8b05120230408115335.jpg', 'Muk', '2023-04-08 04:53:35.529798', '31587786219cd19816efb1f5bec8b05120230408115335jpg'),
(1292, 'b179738faf3d64d6854d0f9e98f1528020230408115748.jpg', 'Mukti', '2023-04-08 04:57:48.345326', 'b179738faf3d64d6854d0f9e98f1528020230408115748jpg'),
(1293, '348aa62cecaa6cfaf7ec1d972119c08920230408115814.jpg', 'Mukti', '2023-04-08 04:58:14.252348', '348aa62cecaa6cfaf7ec1d972119c08920230408115814jpg'),
(1294, '874975ea69634e0896fa95f99ed436c120230408120651.jpg', 'Mukti', '2023-04-08 05:06:51.264511', '874975ea69634e0896fa95f99ed436c120230408120651jpg'),
(1295, 'd70a14757df400b6baa1b76d6b31538620230516231613.jpg', 'Mukti', '2023-05-16 16:16:13.803540', 'd70a14757df400b6baa1b76d6b31538620230516231613jpg'),
(1296, 'd70a14757df400b6baa1b76d6b31538620230516233701.jpg', 'Mukti', '2023-05-16 16:37:01.736931', 'd70a14757df400b6baa1b76d6b31538620230516233701jpg'),
(1297, '876b29e669d915123070c0df67e44e5520230516233706.jpg', 'Mukti', '2023-05-16 16:37:06.059425', '876b29e669d915123070c0df67e44e5520230516233706jpg'),
(1298, 'c74c7ee7e2a22a09cc6cffb2866403eb20230516233712.jpg', 'Mukti', '2023-05-16 16:37:12.041289', 'c74c7ee7e2a22a09cc6cffb2866403eb20230516233712jpg'),
(1299, 'da6a138eda1a6fca49c385426c7aa37220230516233720.jpg', 'Mukti', '2023-05-16 16:37:20.634245', 'da6a138eda1a6fca49c385426c7aa37220230516233720jpg'),
(1300, '5a517c70873dc9f07233dca5fd4cfcd720230516233726.jpg', 'Mukti', '2023-05-16 16:37:26.804661', '5a517c70873dc9f07233dca5fd4cfcd720230516233726jpg'),
(1301, '3bb90be95859524b2cfa3058c283a15020230516233734.jpg', 'Mukti', '2023-05-16 16:37:34.678461', '3bb90be95859524b2cfa3058c283a15020230516233734jpg'),
(1302, '57c5b74b91e5a52014f259b864746afa20230516233742.jpg', 'Mukti', '2023-05-16 16:37:42.479240', '57c5b74b91e5a52014f259b864746afa20230516233742jpg'),
(1303, '12a25f8f9e49aa333bc0e18bee49538d20230516233749.jpg', 'Mukti', '2023-05-16 16:37:49.472488', '12a25f8f9e49aa333bc0e18bee49538d20230516233749jpg'),
(1304, 'c9d0cee502b4711e21c48c1d0b64245c20230516233756.jpg', 'Mukti', '2023-05-16 16:37:56.300056', 'c9d0cee502b4711e21c48c1d0b64245c20230516233756jpg'),
(1305, '458fe5aa36d6c01fef03156dd25599e720230516233804.jpg', 'Mukti', '2023-05-16 16:38:04.212939', '458fe5aa36d6c01fef03156dd25599e720230516233804jpg'),
(1306, '7fedd8cd26e9449df99eeb3a1ebe3d8620230516233810.jpg', 'Mukti', '2023-05-16 16:38:10.905474', '7fedd8cd26e9449df99eeb3a1ebe3d8620230516233810jpg'),
(1307, 'bcafd02b3334895f1cc802d8f46b29b720230516233818.jpg', 'Mukti', '2023-05-16 16:38:18.759945', 'bcafd02b3334895f1cc802d8f46b29b720230516233818jpg'),
(1308, '421fae7ec40a5869747ef3b5fc3d468720230516233824.jpg', 'Mukti', '2023-05-16 16:38:24.896348', '421fae7ec40a5869747ef3b5fc3d468720230516233824jpg'),
(1309, 'e087da480a0834bcd20eee86e5eed9fb20230517003826.jpg', 'Paijo', '2023-05-16 17:38:26.907717', 'e087da480a0834bcd20eee86e5eed9fb20230517003826jpg'),
(1310, 'b749d834b086e718c447bf391f0dbcf220230517003834.jpg', 'Paijo', '2023-05-16 17:38:34.433089', 'b749d834b086e718c447bf391f0dbcf220230517003834jpg'),
(1311, 'b66c9bce2f6153b10d5fb6c2bcc911df20230517003840.jpg', 'Paijo', '2023-05-16 17:38:40.073701', 'b66c9bce2f6153b10d5fb6c2bcc911df20230517003840jpg'),
(1312, '47ecab6d6217dbd6d1164034d2d0347920230517003845.jpg', 'Paijo', '2023-05-16 17:38:45.439287', '47ecab6d6217dbd6d1164034d2d0347920230517003845jpg'),
(1313, '8aec0434664caa4a2eeadc4815109b9920230517003853.jpg', 'Paijo', '2023-05-16 17:38:53.336289', '8aec0434664caa4a2eeadc4815109b9920230517003853jpg'),
(1314, '9f2868063fce5ac4bc41caf39a26215120230517003858.jpg', 'Paijo', '2023-05-16 17:38:58.931050', '9f2868063fce5ac4bc41caf39a26215120230517003858jpg'),
(1315, '0ab9b6baa463e6353c0703efc15dbeca20230517003906.jpg', 'Paijo', '2023-05-16 17:39:06.780771', '0ab9b6baa463e6353c0703efc15dbeca20230517003906jpg'),
(1316, 'a60990d71ba0a85d085ff65e22524ddd20230517003912.jpg', 'Paijo', '2023-05-16 17:39:12.875670', 'a60990d71ba0a85d085ff65e22524ddd20230517003912jpg'),
(1317, '420d3a0b01cc26635b0efb32d5cc46f420230517003918.jpg', 'Paijo', '2023-05-16 17:39:18.804363', '420d3a0b01cc26635b0efb32d5cc46f420230517003918jpg'),
(1318, '3dd7fc55cc044191c183f0df83f3b29c20230517003926.jpg', 'Paijo', '2023-05-16 17:39:26.517687', '3dd7fc55cc044191c183f0df83f3b29c20230517003926jpg'),
(1319, '2ca75d009ce06b256c78945ac29bcc4320230517003933.jpg', 'Paijo', '2023-05-16 17:39:33.615210', '2ca75d009ce06b256c78945ac29bcc4320230517003933jpg'),
(1320, '7b2bc613af7299ba5d0e705d127e458320230517003939.jpg', 'Paijo', '2023-05-16 17:39:39.216004', '7b2bc613af7299ba5d0e705d127e458320230517003939jpg'),
(1321, '7a9d94da230db2a8801b44bb2a58d02e20230517003945.jpg', 'Paijo', '2023-05-16 17:39:45.451056', '7a9d94da230db2a8801b44bb2a58d02e20230517003945jpg'),
(1322, '0926119bbb910f5991aec4e2630e0df120230517021635.jpg', 'Malae', '2023-05-16 19:16:35.195727', '0926119bbb910f5991aec4e2630e0df120230517021635jpg'),
(1323, '01c0e1e46220d2d5c06b6410312cb66f20230517021640.jpg', 'Malae', '2023-05-16 19:16:40.702256', '01c0e1e46220d2d5c06b6410312cb66f20230517021640jpg'),
(1324, '852c03d1e4f861990468f1490f67163c20230517021646.jpg', 'Malae', '2023-05-16 19:16:46.214741', '852c03d1e4f861990468f1490f67163c20230517021646jpg'),
(1325, '426a8929ca450778c28585b13af4f26520230517021651.jpg', 'Malae', '2023-05-16 19:16:51.038847', '426a8929ca450778c28585b13af4f26520230517021651jpg'),
(1326, '6116550f3d73e760d3082096bc17027720230517021655.jpg', 'Malae', '2023-05-16 19:16:55.736425', '6116550f3d73e760d3082096bc17027720230517021655jpg'),
(1327, '0d151e83a60f496b5f57ceb2be9adb4320230517021701.jpg', 'Malae', '2023-05-16 19:17:01.150160', '0d151e83a60f496b5f57ceb2be9adb4320230517021701jpg'),
(1328, 'dca40025075fa0723e1b10e32a81735520230517021705.jpg', 'Malae', '2023-05-16 19:17:05.611684', 'dca40025075fa0723e1b10e32a81735520230517021705jpg'),
(1329, '272c7b22affb9228b7e08b81dd8fc87820230517021710.jpg', 'Malae', '2023-05-16 19:17:10.688344', '272c7b22affb9228b7e08b81dd8fc87820230517021710jpg'),
(1330, '943d13d704884108a8835bc0922f022a20230517021718.jpg', 'Malae', '2023-05-16 19:17:18.075034', '943d13d704884108a8835bc0922f022a20230517021718jpg'),
(1331, '299aa2b454a379a346105274d3d660a620230517021725.jpg', 'Malae', '2023-05-16 19:17:25.203669', '299aa2b454a379a346105274d3d660a620230517021725jpg'),
(1332, 'd7430e9e63b4fe78ba772ad2e50c478f20230517021732.jpg', 'Malae', '2023-05-16 19:17:32.421330', 'd7430e9e63b4fe78ba772ad2e50c478f20230517021732jpg'),
(1333, '7580880e16c8ddd832c038c200a80b9b20230517021740.jpg', 'Malae', '2023-05-16 19:17:40.096084', '7580880e16c8ddd832c038c200a80b9b20230517021740jpg'),
(1334, '82672f623810aa778aad9190e95c8a9b20230517021746.jpg', 'Malae', '2023-05-16 19:17:46.910495', '82672f623810aa778aad9190e95c8a9b20230517021746jpg'),
(1335, '29129597498e8fa8f7147cebb71eaf4e20230517021754.jpg', 'Malae', '2023-05-16 19:17:54.349199', '29129597498e8fa8f7147cebb71eaf4e20230517021754jpg'),
(1336, '210c08aaf65cc9e3486bd957326aff7f20230517021758.jpg', 'Malae', '2023-05-16 19:17:58.744706', '210c08aaf65cc9e3486bd957326aff7f20230517021758jpg'),
(1337, 'b179738faf3d64d6854d0f9e98f1528020230517021804.jpg', 'Malae', '2023-05-16 19:18:04.965629', 'b179738faf3d64d6854d0f9e98f1528020230517021804jpg'),
(1338, 'd95066a59a4f5c61aa8b8ce37ad50f2620230517021811.jpg', 'Malae', '2023-05-16 19:18:11.031028', 'd95066a59a4f5c61aa8b8ce37ad50f2620230517021811jpg'),
(1339, 'fdbbbea321e3a69c0b7422a99d34613820230517021816.jpg', 'Malae', '2023-05-16 19:18:16.876866', 'fdbbbea321e3a69c0b7422a99d34613820230517021816jpg'),
(1340, 'f58f58f8388bc7e2297dd2ef5f24f02c20230517021824.jpg', 'Malae', '2023-05-16 19:18:24.175297', 'f58f58f8388bc7e2297dd2ef5f24f02c20230517021824jpg'),
(1341, '438778feff2300da51172f4333b9823e20230517021830.jpg', 'Malae', '2023-05-16 19:18:30.654273', '438778feff2300da51172f4333b9823e20230517021830jpg'),
(1342, 'd2561d1222e7312985a5312046d0f82a20230517021836.jpg', 'Malae', '2023-05-16 19:18:36.127027', 'd2561d1222e7312985a5312046d0f82a20230517021836jpg'),
(1343, '1231f9618bce659ce2966e08b55aa05820230517021841.jpg', 'Malae', '2023-05-16 19:18:41.225189', '1231f9618bce659ce2966e08b55aa05820230517021841jpg'),
(1344, '645343e0027cb6283fff3231995db91620230517021846.jpg', 'Malae', '2023-05-16 19:18:46.178412', '645343e0027cb6283fff3231995db91620230517021846jpg'),
(1345, '31587786219cd19816efb1f5bec8b05120230517021851.jpg', 'Malae', '2023-05-16 19:18:51.262075', '31587786219cd19816efb1f5bec8b05120230517021851jpg'),
(1346, '2d7225e0f4bedd35097d6db8de41927a20230517021857.jpg', 'Malae', '2023-05-16 19:18:57.157924', '2d7225e0f4bedd35097d6db8de41927a20230517021857jpg'),
(1347, 'd870d1debbc388b1a413becf64d8c4d220230517021903.jpg', 'Malae', '2023-05-16 19:19:03.004408', 'd870d1debbc388b1a413becf64d8c4d220230517021903jpg'),
(1348, 'd1ad77ccc91a80edcf0a2d5193986c2d20230517021909.jpg', 'Malae', '2023-05-16 19:19:09.245336', 'd1ad77ccc91a80edcf0a2d5193986c2d20230517021909jpg'),
(1349, 'd427cba48f4f78d7cfe12f65f8e5fcc420230517021915.jpg', 'Malae', '2023-05-16 19:19:15.152186', 'd427cba48f4f78d7cfe12f65f8e5fcc420230517021915jpg'),
(1350, 'be2728be491517d4858c8528a23b4fc020230517021922.jpg', 'Malae', '2023-05-16 19:19:22.756933', 'be2728be491517d4858c8528a23b4fc020230517021922jpg'),
(1351, '7037a40d5fbee16845ccdc25ca380a3920230517021929.jpg', 'Malae', '2023-05-16 19:19:29.429955', '7037a40d5fbee16845ccdc25ca380a3920230517021929jpg'),
(1352, '7ca847dfc816d2e595e82a50e8f9453620230517021936.jpg', 'Malae', '2023-05-16 19:19:36.555583', '7ca847dfc816d2e595e82a50e8f9453620230517021936jpg'),
(1353, '14a6e63d6e590f52b6b9900208baa7d120230517021941.jpg', 'Malae', '2023-05-16 19:19:41.889304', '14a6e63d6e590f52b6b9900208baa7d120230517021941jpg'),
(1354, 'e73a747605ce6b91080ed28ca7b7d1d120230517021947.jpg', 'Malae', '2023-05-16 19:19:47.172018', 'e73a747605ce6b91080ed28ca7b7d1d120230517021947jpg');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_xsegmentationresult`
--

CREATE TABLE `myapp_xsegmentationresult` (
  `id` int(11) NOT NULL,
  `pathSegmentationKMeans` varchar(100) NOT NULL,
  `pathSegmentationAdaptive` varchar(100) NOT NULL,
  `pathGroundTruth` varchar(100) NOT NULL,
  `report` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`report`)),
  `date` datetime(6) NOT NULL,
  `idImage_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_xsegmentationresult`
--

INSERT INTO `myapp_xsegmentationresult` (`id`, `pathSegmentationKMeans`, `pathSegmentationAdaptive`, `pathGroundTruth`, `report`, `date`, `idImage_id`) VALUES
(1, '0926119bbb910f5991aec4e2630e0df120230408113855_segmented.jpg', '0926119bbb910f5991aec4e2630e0df120230408113855_segmented.jpg', '0926119bbb910f5991aec4e2630e0df120230408113855_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-04-08 04:38:55.207309', 1290),
(2, '31587786219cd19816efb1f5bec8b05120230408115340_segmented.jpg', '31587786219cd19816efb1f5bec8b05120230408115340_segmented.jpg', '31587786219cd19816efb1f5bec8b05120230408115340_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-04-08 04:53:40.396923', 1291),
(3, 'b179738faf3d64d6854d0f9e98f1528020230408115752_segmented.jpg', 'b179738faf3d64d6854d0f9e98f1528020230408115752_segmented.jpg', 'b179738faf3d64d6854d0f9e98f1528020230408115752_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-04-08 04:57:52.882874', 1292),
(4, '348aa62cecaa6cfaf7ec1d972119c08920230408115818_segmented.jpg', '348aa62cecaa6cfaf7ec1d972119c08920230408115818_segmented.jpg', '348aa62cecaa6cfaf7ec1d972119c08920230408115818_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-04-08 04:58:19.088967', 1293),
(5, '874975ea69634e0896fa95f99ed436c120230408120657_segmented.jpg', '874975ea69634e0896fa95f99ed436c120230408120657_segmented.jpg', '874975ea69634e0896fa95f99ed436c120230408120657_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-04-08 05:06:57.730000', 1294),
(6, 'd70a14757df400b6baa1b76d6b31538620230516231618_segmented.jpg', 'd70a14757df400b6baa1b76d6b31538620230516231618_segmented.jpg', 'd70a14757df400b6baa1b76d6b31538620230516231618_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:16:18.469605', 1295),
(7, 'd70a14757df400b6baa1b76d6b31538620230516233705_segmented.jpg', 'd70a14757df400b6baa1b76d6b31538620230516233705_segmented.jpg', 'd70a14757df400b6baa1b76d6b31538620230516233705_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:06.057425', 1296),
(8, '876b29e669d915123070c0df67e44e5520230516233711_segmented.jpg', '876b29e669d915123070c0df67e44e5520230516233711_segmented.jpg', '876b29e669d915123070c0df67e44e5520230516233711_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:12.039289', 1297),
(9, 'c74c7ee7e2a22a09cc6cffb2866403eb20230516233720_segmented.jpg', 'c74c7ee7e2a22a09cc6cffb2866403eb20230516233720_segmented.jpg', 'c74c7ee7e2a22a09cc6cffb2866403eb20230516233720_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:20.632245', 1298),
(10, 'da6a138eda1a6fca49c385426c7aa37220230516233726_segmented.jpg', 'da6a138eda1a6fca49c385426c7aa37220230516233726_segmented.jpg', 'da6a138eda1a6fca49c385426c7aa37220230516233726_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:26.801660', 1299),
(11, '5a517c70873dc9f07233dca5fd4cfcd720230516233734_segmented.jpg', '5a517c70873dc9f07233dca5fd4cfcd720230516233734_segmented.jpg', '5a517c70873dc9f07233dca5fd4cfcd720230516233734_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:34.673460', 1300),
(12, '3bb90be95859524b2cfa3058c283a15020230516233742_segmented.jpg', '3bb90be95859524b2cfa3058c283a15020230516233742_segmented.jpg', '3bb90be95859524b2cfa3058c283a15020230516233742_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:42.478239', 1301),
(13, '57c5b74b91e5a52014f259b864746afa20230516233749_segmented.jpg', '57c5b74b91e5a52014f259b864746afa20230516233749_segmented.jpg', '57c5b74b91e5a52014f259b864746afa20230516233749_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:49.470488', 1302),
(14, '12a25f8f9e49aa333bc0e18bee49538d20230516233756_segmented.jpg', '12a25f8f9e49aa333bc0e18bee49538d20230516233756_segmented.jpg', '12a25f8f9e49aa333bc0e18bee49538d20230516233756_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:37:56.295055', 1303),
(15, 'c9d0cee502b4711e21c48c1d0b64245c20230516233804_segmented.jpg', 'c9d0cee502b4711e21c48c1d0b64245c20230516233804_segmented.jpg', 'c9d0cee502b4711e21c48c1d0b64245c20230516233804_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:38:04.210939', 1304),
(16, '458fe5aa36d6c01fef03156dd25599e720230516233810_segmented.jpg', '458fe5aa36d6c01fef03156dd25599e720230516233810_segmented.jpg', '458fe5aa36d6c01fef03156dd25599e720230516233810_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:38:10.903473', 1305),
(17, '7fedd8cd26e9449df99eeb3a1ebe3d8620230516233818_segmented.jpg', '7fedd8cd26e9449df99eeb3a1ebe3d8620230516233818_segmented.jpg', '7fedd8cd26e9449df99eeb3a1ebe3d8620230516233818_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:38:18.758945', 1306),
(18, 'bcafd02b3334895f1cc802d8f46b29b720230516233824_segmented.jpg', 'bcafd02b3334895f1cc802d8f46b29b720230516233824_segmented.jpg', 'bcafd02b3334895f1cc802d8f46b29b720230516233824_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:38:24.894347', 1307),
(19, '421fae7ec40a5869747ef3b5fc3d468720230516233831_segmented.jpg', '421fae7ec40a5869747ef3b5fc3d468720230516233831_segmented.jpg', '421fae7ec40a5869747ef3b5fc3d468720230516233831_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 16:38:31.750917', 1308),
(20, 'e087da480a0834bcd20eee86e5eed9fb20230517003834_segmented.jpg', 'e087da480a0834bcd20eee86e5eed9fb20230517003834_segmented.jpg', 'e087da480a0834bcd20eee86e5eed9fb20230517003834_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:38:34.431088', 1309),
(21, 'b749d834b086e718c447bf391f0dbcf220230517003839_segmented.jpg', 'b749d834b086e718c447bf391f0dbcf220230517003839_segmented.jpg', 'b749d834b086e718c447bf391f0dbcf220230517003839_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:38:40.069700', 1310),
(22, 'b66c9bce2f6153b10d5fb6c2bcc911df20230517003845_segmented.jpg', 'b66c9bce2f6153b10d5fb6c2bcc911df20230517003845_segmented.jpg', 'b66c9bce2f6153b10d5fb6c2bcc911df20230517003845_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:38:45.437287', 1311),
(23, '47ecab6d6217dbd6d1164034d2d0347920230517003853_segmented.jpg', '47ecab6d6217dbd6d1164034d2d0347920230517003853_segmented.jpg', '47ecab6d6217dbd6d1164034d2d0347920230517003853_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:38:53.335253', 1312),
(24, '8aec0434664caa4a2eeadc4815109b9920230517003858_segmented.jpg', '8aec0434664caa4a2eeadc4815109b9920230517003858_segmented.jpg', '8aec0434664caa4a2eeadc4815109b9920230517003858_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:38:58.929049', 1313),
(25, '9f2868063fce5ac4bc41caf39a26215120230517003906_segmented.jpg', '9f2868063fce5ac4bc41caf39a26215120230517003906_segmented.jpg', '9f2868063fce5ac4bc41caf39a26215120230517003906_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:06.779770', 1314),
(26, '0ab9b6baa463e6353c0703efc15dbeca20230517003912_segmented.jpg', '0ab9b6baa463e6353c0703efc15dbeca20230517003912_segmented.jpg', '0ab9b6baa463e6353c0703efc15dbeca20230517003912_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:12.874167', 1315),
(27, 'a60990d71ba0a85d085ff65e22524ddd20230517003918_segmented.jpg', 'a60990d71ba0a85d085ff65e22524ddd20230517003918_segmented.jpg', 'a60990d71ba0a85d085ff65e22524ddd20230517003918_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:18.803363', 1316),
(28, '420d3a0b01cc26635b0efb32d5cc46f420230517003926_segmented.jpg', '420d3a0b01cc26635b0efb32d5cc46f420230517003926_segmented.jpg', '420d3a0b01cc26635b0efb32d5cc46f420230517003926_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:26.515182', 1317),
(29, '3dd7fc55cc044191c183f0df83f3b29c20230517003933_segmented.jpg', '3dd7fc55cc044191c183f0df83f3b29c20230517003933_segmented.jpg', '3dd7fc55cc044191c183f0df83f3b29c20230517003933_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:33.613707', 1318),
(30, '2ca75d009ce06b256c78945ac29bcc4320230517003939_segmented.jpg', '2ca75d009ce06b256c78945ac29bcc4320230517003939_segmented.jpg', '2ca75d009ce06b256c78945ac29bcc4320230517003939_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:39.214979', 1319),
(31, '7b2bc613af7299ba5d0e705d127e458320230517003945_segmented.jpg', '7b2bc613af7299ba5d0e705d127e458320230517003945_segmented.jpg', '7b2bc613af7299ba5d0e705d127e458320230517003945_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:45.449054', 1320),
(32, '7a9d94da230db2a8801b44bb2a58d02e20230517003951_segmented.jpg', '7a9d94da230db2a8801b44bb2a58d02e20230517003951_segmented.jpg', '7a9d94da230db2a8801b44bb2a58d02e20230517003951_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 17:39:51.457283', 1321),
(33, '0926119bbb910f5991aec4e2630e0df120230517021640_segmented.jpg', '0926119bbb910f5991aec4e2630e0df120230517021640_segmented.jpg', '0926119bbb910f5991aec4e2630e0df120230517021640_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:16:40.701257', 1322),
(34, '01c0e1e46220d2d5c06b6410312cb66f20230517021646_segmented.jpg', '01c0e1e46220d2d5c06b6410312cb66f20230517021646_segmented.jpg', '01c0e1e46220d2d5c06b6410312cb66f20230517021646_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:16:46.213741', 1323),
(35, '852c03d1e4f861990468f1490f67163c20230517021650_segmented.jpg', '852c03d1e4f861990468f1490f67163c20230517021650_segmented.jpg', '852c03d1e4f861990468f1490f67163c20230517021650_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:16:51.036847', 1324),
(36, '426a8929ca450778c28585b13af4f26520230517021655_segmented.jpg', '426a8929ca450778c28585b13af4f26520230517021655_segmented.jpg', '426a8929ca450778c28585b13af4f26520230517021655_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:16:55.735425', 1325),
(37, '6116550f3d73e760d3082096bc17027720230517021700_segmented.jpg', '6116550f3d73e760d3082096bc17027720230517021700_segmented.jpg', '6116550f3d73e760d3082096bc17027720230517021700_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:01.149160', 1326),
(38, '0d151e83a60f496b5f57ceb2be9adb4320230517021705_segmented.jpg', '0d151e83a60f496b5f57ceb2be9adb4320230517021705_segmented.jpg', '0d151e83a60f496b5f57ceb2be9adb4320230517021705_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:05.609683', 1327),
(39, 'dca40025075fa0723e1b10e32a81735520230517021710_segmented.jpg', 'dca40025075fa0723e1b10e32a81735520230517021710_segmented.jpg', 'dca40025075fa0723e1b10e32a81735520230517021710_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:10.686343', 1328),
(40, '272c7b22affb9228b7e08b81dd8fc87820230517021717_segmented.jpg', '272c7b22affb9228b7e08b81dd8fc87820230517021717_segmented.jpg', '272c7b22affb9228b7e08b81dd8fc87820230517021717_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:18.074035', 1329),
(41, '943d13d704884108a8835bc0922f022a20230517021724_segmented.jpg', '943d13d704884108a8835bc0922f022a20230517021724_segmented.jpg', '943d13d704884108a8835bc0922f022a20230517021724_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:25.202668', 1330),
(42, '299aa2b454a379a346105274d3d660a620230517021732_segmented.jpg', '299aa2b454a379a346105274d3d660a620230517021732_segmented.jpg', '299aa2b454a379a346105274d3d660a620230517021732_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:32.418329', 1331),
(43, 'd7430e9e63b4fe78ba772ad2e50c478f20230517021739_segmented.jpg', 'd7430e9e63b4fe78ba772ad2e50c478f20230517021739_segmented.jpg', 'd7430e9e63b4fe78ba772ad2e50c478f20230517021739_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:40.094084', 1332),
(44, '7580880e16c8ddd832c038c200a80b9b20230517021746_segmented.jpg', '7580880e16c8ddd832c038c200a80b9b20230517021746_segmented.jpg', '7580880e16c8ddd832c038c200a80b9b20230517021746_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:46.909495', 1333),
(45, '82672f623810aa778aad9190e95c8a9b20230517021754_segmented.jpg', '82672f623810aa778aad9190e95c8a9b20230517021754_segmented.jpg', '82672f623810aa778aad9190e95c8a9b20230517021754_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:54.347198', 1334),
(46, '29129597498e8fa8f7147cebb71eaf4e20230517021758_segmented.jpg', '29129597498e8fa8f7147cebb71eaf4e20230517021758_segmented.jpg', '29129597498e8fa8f7147cebb71eaf4e20230517021758_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:17:58.742705', 1335),
(47, '210c08aaf65cc9e3486bd957326aff7f20230517021804_segmented.jpg', '210c08aaf65cc9e3486bd957326aff7f20230517021804_segmented.jpg', '210c08aaf65cc9e3486bd957326aff7f20230517021804_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:04.963630', 1336),
(48, 'b179738faf3d64d6854d0f9e98f1528020230517021810_segmented.jpg', 'b179738faf3d64d6854d0f9e98f1528020230517021810_segmented.jpg', 'b179738faf3d64d6854d0f9e98f1528020230517021810_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:11.029027', 1337),
(49, 'd95066a59a4f5c61aa8b8ce37ad50f2620230517021816_segmented.jpg', 'd95066a59a4f5c61aa8b8ce37ad50f2620230517021816_segmented.jpg', 'd95066a59a4f5c61aa8b8ce37ad50f2620230517021816_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:16.872864', 1338),
(50, 'fdbbbea321e3a69c0b7422a99d34613820230517021823_segmented.jpg', 'fdbbbea321e3a69c0b7422a99d34613820230517021823_segmented.jpg', 'fdbbbea321e3a69c0b7422a99d34613820230517021823_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:24.173297', 1339),
(51, 'f58f58f8388bc7e2297dd2ef5f24f02c20230517021830_segmented.jpg', 'f58f58f8388bc7e2297dd2ef5f24f02c20230517021830_segmented.jpg', 'f58f58f8388bc7e2297dd2ef5f24f02c20230517021830_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:30.641270', 1340),
(52, '438778feff2300da51172f4333b9823e20230517021835_segmented.jpg', '438778feff2300da51172f4333b9823e20230517021835_segmented.jpg', '438778feff2300da51172f4333b9823e20230517021835_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:36.126026', 1341),
(53, 'd2561d1222e7312985a5312046d0f82a20230517021840_segmented.jpg', 'd2561d1222e7312985a5312046d0f82a20230517021840_segmented.jpg', 'd2561d1222e7312985a5312046d0f82a20230517021840_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:41.224188', 1342),
(54, '1231f9618bce659ce2966e08b55aa05820230517021845_segmented.jpg', '1231f9618bce659ce2966e08b55aa05820230517021845_segmented.jpg', '1231f9618bce659ce2966e08b55aa05820230517021845_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:46.176412', 1343),
(55, '645343e0027cb6283fff3231995db91620230517021851_segmented.jpg', '645343e0027cb6283fff3231995db91620230517021851_segmented.jpg', '645343e0027cb6283fff3231995db91620230517021851_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:51.260075', 1344),
(56, '31587786219cd19816efb1f5bec8b05120230517021856_segmented.jpg', '31587786219cd19816efb1f5bec8b05120230517021856_segmented.jpg', '31587786219cd19816efb1f5bec8b05120230517021856_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:18:57.155924', 1345),
(57, '2d7225e0f4bedd35097d6db8de41927a20230517021902_segmented.jpg', '2d7225e0f4bedd35097d6db8de41927a20230517021902_segmented.jpg', '2d7225e0f4bedd35097d6db8de41927a20230517021902_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:03.002407', 1346),
(58, 'd870d1debbc388b1a413becf64d8c4d220230517021908_segmented.jpg', 'd870d1debbc388b1a413becf64d8c4d220230517021908_segmented.jpg', 'd870d1debbc388b1a413becf64d8c4d220230517021908_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:09.243336', 1347),
(59, 'd1ad77ccc91a80edcf0a2d5193986c2d20230517021914_segmented.jpg', 'd1ad77ccc91a80edcf0a2d5193986c2d20230517021914_segmented.jpg', 'd1ad77ccc91a80edcf0a2d5193986c2d20230517021914_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:15.150185', 1348),
(60, 'd427cba48f4f78d7cfe12f65f8e5fcc420230517021922_segmented.jpg', 'd427cba48f4f78d7cfe12f65f8e5fcc420230517021922_segmented.jpg', 'd427cba48f4f78d7cfe12f65f8e5fcc420230517021922_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:22.754931', 1349),
(61, 'be2728be491517d4858c8528a23b4fc020230517021929_segmented.jpg', 'be2728be491517d4858c8528a23b4fc020230517021929_segmented.jpg', 'be2728be491517d4858c8528a23b4fc020230517021929_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:29.425953', 1350),
(62, '7037a40d5fbee16845ccdc25ca380a3920230517021936_segmented.jpg', '7037a40d5fbee16845ccdc25ca380a3920230517021936_segmented.jpg', '7037a40d5fbee16845ccdc25ca380a3920230517021936_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:36.550582', 1351),
(63, '7ca847dfc816d2e595e82a50e8f9453620230517021941_segmented.jpg', '7ca847dfc816d2e595e82a50e8f9453620230517021941_segmented.jpg', '7ca847dfc816d2e595e82a50e8f9453620230517021941_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:41.887304', 1352),
(64, '14a6e63d6e590f52b6b9900208baa7d120230517021946_segmented.jpg', '14a6e63d6e590f52b6b9900208baa7d120230517021946_segmented.jpg', '14a6e63d6e590f52b6b9900208baa7d120230517021946_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:47.166017', 1353),
(65, 'e73a747605ce6b91080ed28ca7b7d1d120230517021953_segmented.jpg', 'e73a747605ce6b91080ed28ca7b7d1d120230517021953_segmented.jpg', 'e73a747605ce6b91080ed28ca7b7d1d120230517021953_segmented.jpg', '{\"kmeans\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}, \"adaptive\": {\"accuracy\": 0.5, \"precision\": 0.5, \"recall\": 0.5, \"f1\": 0.5}}', '2023-05-16 19:19:53.535972', 1354);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_ximage`
--
ALTER TABLE `myapp_ximage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_ximage_slug_638a1bd8` (`slug`);

--
-- Indexes for table `myapp_xsegmentationresult`
--
ALTER TABLE `myapp_xsegmentationresult`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_xsegmentationresult_idImage_id_20822da0_fk_myapp_ximage_id` (`idImage_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `myapp_ximage`
--
ALTER TABLE `myapp_ximage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1355;

--
-- AUTO_INCREMENT for table `myapp_xsegmentationresult`
--
ALTER TABLE `myapp_xsegmentationresult`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `myapp_xsegmentationresult`
--
ALTER TABLE `myapp_xsegmentationresult`
  ADD CONSTRAINT `myapp_xsegmentationresult_idImage_id_20822da0_fk_myapp_ximage_id` FOREIGN KEY (`idImage_id`) REFERENCES `myapp_ximage` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
