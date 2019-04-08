-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`users` (
  `uid` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE INDEX `uid_UNIQUE` (`uid` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`chords`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`chords` (
  `cid` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(10) NOT NULL,
  `image` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`cid`),
  UNIQUE INDEX `cid_UNIQUE` (`cid` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`progressions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`progressions` (
  `progid` INT NOT NULL AUTO_INCREMENT,
  `c1` INT NOT NULL,
  `c2` INT NOT NULL,
  `c3` INT NOT NULL,
  `c4` INT NOT NULL,
  `date` DATETIME NULL,
  `uid` INT NOT NULL,
  PRIMARY KEY (`progid`),
  UNIQUE INDEX `progid_UNIQUE` (`progid` ASC) VISIBLE,
  INDEX `fk_c1_idx` (`c1` ASC) VISIBLE,
  INDEX `fk_c2_idx` (`c2` ASC) VISIBLE,
  INDEX `fk_c3_idx` (`c3` ASC) VISIBLE,
  INDEX `fk_c4_idx` (`c4` ASC) VISIBLE,
  INDEX `fk_uid_idx` (`uid` ASC) VISIBLE,
  CONSTRAINT `fk_c1`
    FOREIGN KEY (`c1`)
    REFERENCES `mydb`.`chords` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_c2`
    FOREIGN KEY (`c2`)
    REFERENCES `mydb`.`chords` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_c3`
    FOREIGN KEY (`c3`)
    REFERENCES `mydb`.`chords` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_c4`
    FOREIGN KEY (`c4`)
    REFERENCES `mydb`.`chords` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_uid`
    FOREIGN KEY (`uid`)
    REFERENCES `mydb`.`users` (`uid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Posts` (
  `pid` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(1000) NULL,
  `date` DATETIME NULL,
  `uid` INT NULL,
  `progid` INT NOT NULL,
  PRIMARY KEY (`pid`),
  UNIQUE INDEX `pid_UNIQUE` (`pid` ASC) VISIBLE,
  INDEX `fk_uid_idx` (`uid` ASC) VISIBLE,
  INDEX `fk_progid_idx` (`progid` ASC) VISIBLE,
  CONSTRAINT `fk_uid2`
    FOREIGN KEY (`uid`)
    REFERENCES `mydb`.`users` (`uid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_progid`
    FOREIGN KEY (`progid`)
    REFERENCES `mydb`.`progressions` (`progid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`keys`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`keys` (
  `kid` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`kid`),
  UNIQUE INDEX `kid_UNIQUE` (`kid` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`keychords`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`keychords` (
  `kid` INT NOT NULL,
  `cid` INT NOT NULL,
  INDEX `fk_cid_idx` (`cid` ASC) VISIBLE,
  CONSTRAINT `fk_kid`
    FOREIGN KEY (`kid`)
    REFERENCES `mydb`.`keys` (`kid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cid`
    FOREIGN KEY (`cid`)
    REFERENCES `mydb`.`chords` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
