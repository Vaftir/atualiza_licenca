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
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `id_UNIQUE` ON `zanthus`.`atualizacao` (`id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `zanthus`.`monitoramento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `zanthus`.`monitoramento` ;

CREATE TABLE IF NOT EXISTS `zanthus`.`monitoramento` (
  `id_monitoramento` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `descricao` VARCHAR(800) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `numero_de_dias` INT NOT NULL,
  `id_atualizacao` INT NULL DEFAULT NULL,
  `data_atualizacao` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_monitoramento`),
  CONSTRAINT `id_atualizacao`
    FOREIGN KEY (`id_atualizacao`)
    REFERENCES `zanthus`.`atualizacao` (`id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `idmonitoramento_UNIQUE` ON `zanthus`.`monitoramento` (`id_monitoramento` ASC) VISIBLE;

CREATE INDEX `id_atualizacao_idx` ON `zanthus`.`monitoramento` (`id_atualizacao` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `zanthus`.`filiais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `zanthus`.`filiais` ;

CREATE TABLE IF NOT EXISTS `zanthus`.`filiais` (
  `idfiliais` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `numero_filial` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(80) NULL DEFAULT NULL,
  `descricao_manager` VARCHAR(260) NULL DEFAULT NULL,
  `num_dias` INT NULL DEFAULT NULL,
  `id_monitoramento` INT NULL DEFAULT NULL,
  `id_atualizacao` INT NULL DEFAULT NULL,
  `data_criacao` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`idfiliais`),
  CONSTRAINT `fk_atualizacao`
    FOREIGN KEY (`id_atualizacao`)
    REFERENCES `zanthus`.`atualizacao` (`id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_monitoramento`
    FOREIGN KEY (`id_monitoramento`)
    REFERENCES `zanthus`.`monitoramento` (`id_monitoramento`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `idfiliais_UNIQUE` ON `zanthus`.`filiais` (`idfiliais` ASC) VISIBLE;

CREATE INDEX `id_monitoramento_idx` ON `zanthus`.`filiais` (`id_monitoramento` ASC) VISIBLE;

CREATE INDEX `id_atualizacao_idx` ON `zanthus`.`filiais` (`id_atualizacao` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
