import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306, charset='utf8')

criar_tabelas = '''SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mylista
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mylista
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mylista` DEFAULT CHARACTER SET utf8 ;
USE `mylista` ;

-- -----------------------------------------------------
-- Table `mylista`.`SCORE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`SCORE` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `SCORE` REAL NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`SYNOPSIS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`SYNOPSIS` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `SYNOPSIS` LONGTEXT NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`SERIE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`SERIE` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(45) NOT NULL,
  `EPS` INT NOT NULL,
  `TEMPS` VARCHAR(45) NOT NULL,
  `SCORE_ID` INT NOT NULL,
  `SYNOPSIS_ID` INT NOT NULL,
  PRIMARY KEY (`ID`, `SCORE_ID`, `SYNOPSIS_ID`),
  INDEX `fk_SERIE_SCORE1_idx` (`SCORE_ID` ASC) VISIBLE,
  INDEX `fk_SERIE_SYNOPSIS1_idx` (`SYNOPSIS_ID` ASC) VISIBLE,
  CONSTRAINT `fk_SERIE_SCORE1`
    FOREIGN KEY (`SCORE_ID`)
    REFERENCES `mylista`.`SCORE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SERIE_SYNOPSIS1`
    FOREIGN KEY (`SYNOPSIS_ID`)
    REFERENCES `mylista`.`SYNOPSIS` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`MOVIE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`MOVIE` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(45) NOT NULL,
  `DURATION` TIME NOT NULL,
  `SCORE_ID` INT NOT NULL,
  `SYNOPSIS_ID` INT NOT NULL,
  PRIMARY KEY (`ID`, `SCORE_ID`, `SYNOPSIS_ID`),
  INDEX `fk_MOVIE_SCORE1_idx` (`SCORE_ID` ASC) VISIBLE,
  INDEX `fk_MOVIE_SYNOPSIS1_idx` (`SYNOPSIS_ID` ASC) VISIBLE,
  CONSTRAINT `fk_MOVIE_SCORE1`
    FOREIGN KEY (`SCORE_ID`)
    REFERENCES `mylista`.`SCORE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MOVIE_SYNOPSIS1`
    FOREIGN KEY (`SYNOPSIS_ID`)
    REFERENCES `mylista`.`SYNOPSIS` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`GENERO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`GENERO` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`GENERO_SERIE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`GENERO_SERIE` (
  `GENERO_ID` INT NOT NULL,
  `SERIE_ID` INT NOT NULL,
  PRIMARY KEY (`GENERO_ID`, `SERIE_ID`),
  INDEX `fk_GENERO_has_SERIE_SERIE1_idx` (`SERIE_ID` ASC) VISIBLE,
  INDEX `fk_GENERO_has_SERIE_GENERO_idx` (`GENERO_ID` ASC) VISIBLE,
  CONSTRAINT `fk_GENERO_has_SERIE_GENERO`
    FOREIGN KEY (`GENERO_ID`)
    REFERENCES `mylista`.`GENERO` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_GENERO_has_SERIE_SERIE1`
    FOREIGN KEY (`SERIE_ID`)
    REFERENCES `mylista`.`SERIE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`GENERO_MOVIE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`GENERO_MOVIE` (
  `GENERO_ID` INT NOT NULL,
  `MOVIE_ID` INT NOT NULL,
  PRIMARY KEY (`GENERO_ID`, `MOVIE_ID`),
  INDEX `fk_GENERO_has_MOVIE_MOVIE1_idx` (`MOVIE_ID` ASC) VISIBLE,
  INDEX `fk_GENERO_has_MOVIE_GENERO1_idx` (`GENERO_ID` ASC) VISIBLE,
  CONSTRAINT `fk_GENERO_has_MOVIE_GENERO1`
    FOREIGN KEY (`GENERO_ID`)
    REFERENCES `mylista`.`GENERO` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_GENERO_has_MOVIE_MOVIE1`
    FOREIGN KEY (`MOVIE_ID`)
    REFERENCES `mylista`.`MOVIE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`ANO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`ANO` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `ANO` INT NOT NULL,
  `SERIE_ID` INT NOT NULL,
  `MOVIE_ID` INT NOT NULL,
  PRIMARY KEY (`ID`, `SERIE_ID`, `MOVIE_ID`),
  INDEX `fk_ANO_MOVIE1_idx` (`MOVIE_ID` ASC) VISIBLE,
  CONSTRAINT `fk_ANO_SERIE1`
    FOREIGN KEY (`SERIE_ID`)
    REFERENCES `mylista`.`SERIE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ANO_MOVIE1`
    FOREIGN KEY (`MOVIE_ID`)
    REFERENCES `mylista`.`MOVIE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`STUDIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`STUDIO` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(45) NOT NULL,
  `SERIE_ID` INT NOT NULL,
  `MOVIE_ID` INT NOT NULL,
  PRIMARY KEY (`ID`, `SERIE_ID`, `MOVIE_ID`),
  INDEX `fk_STUDIO_SERIE1_idx` (`SERIE_ID` ASC) VISIBLE,
  INDEX `fk_STUDIO_MOVIE1_idx` (`MOVIE_ID` ASC) VISIBLE,
  CONSTRAINT `fk_STUDIO_SERIE1`
    FOREIGN KEY (`SERIE_ID`)
    REFERENCES `mylista`.`SERIE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_STUDIO_MOVIE1`
    FOREIGN KEY (`MOVIE_ID`)
    REFERENCES `mylista`.`MOVIE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mylista`.`USUARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylista`.`USUARIO` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(45) NOT NULL,
  `EMAIL` VARCHAR(45) NOT NULL,
  `SENHA` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;'''
conn.cursor().execute(criar_tabelas)

cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO mylista.USUARIO (NOME, EMAIL, SENHA) VALUES (%s, %s, %s)',
      [
            ('otavio', 'otavio@gmail.com', '123456'),
      ])

cursor.execute('select * from mylista.USUARIO')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])


conn.commit()
cursor.close()
