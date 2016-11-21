
SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `Category`;
CREATE TABLE `Category` (
  `ID` varchar(50) NOT NULL,
  `isActive` tinyint(1) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `imageURL` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Playlist*/
DROP TABLE IF EXISTS `Playlist`;
CREATE TABLE `Playlist` (
  `ID` varchar(50) NOT NULL,
  `isActive` tinyint(1) DEFAULT NULL,
  `categoryID` varchar(50) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `imageURL` varchar(255) DEFAULT NULL,
  `ownerId` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_Category_Playlist` (`categoryID`),
  CONSTRAINT `FK_Category_Playlist` FOREIGN KEY (`categoryID`) REFERENCES `Category` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- /*Track*/

/*Playlist*/
DROP TABLE IF EXISTS `Track`;
CREATE TABLE `Track` (
  `ID` varchar(50) NOT NULL,
  `isActive` tinyint(1) DEFAULT NULL,
  `playlistID` varchar(50) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `playbackURL` varchar(255) DEFAULT NULL,
  `popularity` smallint DEFAULT NULL,
  `albumName` varchar(255) DEFAULT NULL,
  `albumImageURL` varchar(255) DEFAULT NULL,
  `artistID` varchar(50) DEFAULT NULL,
  `artistName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_Playlist_Track` (`playlistID`),
  CONSTRAINT `FK_Playlist_Track` FOREIGN KEY (`playlistID`) REFERENCES `Playlist` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Audio Features

DROP TABLE IF EXISTS `AudioFeatures`;
CREATE TABLE `AudioFeatures` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `isActive` tinyint(1) DEFAULT NULL,
  `trackID` varchar(50) NOT NULL,
  `acousticness` decimal(15,6) DEFAULT NULL,
  `danceability` decimal(15,6) DEFAULT NULL,
  `duration_ms` bigint DEFAULT NULL,
  `energy` decimal(15,6) DEFAULT NULL,
  `instrumentalness` decimal(15,6) DEFAULT NULL,
  `a_key` smallint DEFAULT NULL,
  `liveness` decimal(15,6) DEFAULT NULL,
  `loudness` decimal(15,6) DEFAULT NULL,
  `a_mode` smallint DEFAULT NULL,
  `speechiness` decimal(15,6) DEFAULT NULL,
  `tempo` decimal(15,6) DEFAULT NULL,
  `time_signature` smallint DEFAULT NULL,
  `valence` decimal(15,6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_TRACK_AUDIOFEATURE` (`trackID`),
  CONSTRAINT `FK_TRACK_AUDIOFEATURE` FOREIGN KEY (`trackID`) REFERENCES `Track` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS=1;
