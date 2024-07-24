-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema zanthus
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `zanthus` ;

-- -----------------------------------------------------
-- Schema zanthus
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `zanthus` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `zanthus` ;

-- -----------------------------------------------------
-- Table `zanthus`.`atualizacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `zanthus`.`atualizacao` ;

CREATE TABLE IF NOT EXISTS `zanthus`.`atualizacao` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `status` VARCHAR(45) NOT NULL,
  `data` DATETIME NOT NULL,
  `texto` VARCHAR(180) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `zanthus`.`monitoramento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `zanthus`.`monitoramento` ;

CREATE TABLE IF NOT EXISTS `zanthus`.`monitoramento` (
  `id_monitoramento` INT NOT NULL,
  `data` DATETIME NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `numero_de_dias` INT NOT NULL,
  `id_atualizacao` INT DEFAULT NULL,
  PRIMARY KEY (`id_monitoramento`),
  UNIQUE INDEX `idmonitoramento_UNIQUE` (`id_monitoramento` ASC) VISIBLE,
  INDEX `id_atualizacao_idx` (`id_atualizacao` ASC) VISIBLE,
  CONSTRAINT `id_atualizacao`
    FOREIGN KEY (`id_atualizacao`)
    REFERENCES `zanthus`.`atualizacao` (`id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- TABLE `zanthus`.`filiais`
-- -----------------------------------------------------

CREATE TABLE `zanthus`.`filiais` (
  `idfiliais` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `numero_filial` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(80) NULL,
  `descricao_manager` VARCHAR(260) NULL,
  `num_dias` INT NULL,
  `id_monitoramento` INT NULL,
  `id_atualizacao` INT NULL,
  `data_criacao` DATETIME NULL,
  `filiaiscol` VARCHAR(45) NULL,
  PRIMARY KEY (`idfiliais`),
  UNIQUE INDEX `idfiliais_UNIQUE` (`idfiliais` ASC),
  INDEX `id_monitoramento_idx` (`id_monitoramento` ASC),
  INDEX `id_atualizacao_idx` (`id_atualizacao` ASC),
  CONSTRAINT `fk_monitoramento`
    FOREIGN KEY (`id_monitoramento`)
    REFERENCES `monitoramento` (`id_monitoramento`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_atualizacao`
    FOREIGN KEY (`id_atualizacao`)
    REFERENCES `atualizacao` (`id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);
