SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE DATABASE IF NOT EXISTS `cv` DEFAULT CHARACTER SET utf8 ;
USE `cv` ;

-- -----------------------------------------------------
-- Table `cv`.`Marca`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cv`.`Marca` ;

CREATE TABLE IF NOT EXISTS `cv`.`Marca` (
  `idMarca` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idMarca`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cv`.`Produto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cv`.`Produto` ;

CREATE TABLE IF NOT EXISTS `cv`.`Produto` (
  `codigo` INT NOT NULL,
  `Descricao` VARCHAR(60) NOT NULL,
  `Linha` VARCHAR(25) NOT NULL,
  `Marca_idMarca` INT NOT NULL,
  PRIMARY KEY (`codigo`),
  CONSTRAINT `fk_Produto_Marca1`
    FOREIGN KEY (`Marca_idMarca`)
    REFERENCES `cv`.`Marca` (`idMarca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Produto_Marca1_idx` ON `cv`.`Produto` (`Marca_idMarca` ASC) VISIBLE;

CREATE UNIQUE INDEX `Descricao_UNIQUE` ON `cv`.`Produto` (`Descricao` ASC) VISIBLE;

CREATE UNIQUE INDEX `codigo_UNIQUE` ON `cv`.`Produto` (`codigo` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `cv`.`Cliente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cv`.`Cliente` ;

CREATE TABLE IF NOT EXISTS `cv`.`Cliente` (
  `idCliente` INT NOT NULL,
  `Nome` VARCHAR(60) NULL,
  `Telefone` VARCHAR(45) NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Nome_UNIQUE` ON `cv`.`Cliente` (`Nome` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `cv`.`Estoque`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cv`.`Estoque` ;

CREATE TABLE IF NOT EXISTS `cv`.`Estoque` (
  `idEstoque` INT NOT NULL,
  `Quantidade` INT NOT NULL DEFAULT 0,
  `Validade` DATE NULL,
  `Produto_codigo` INT NOT NULL,
  `Preco` DECIMAL(2) NULL,
  PRIMARY KEY (`idEstoque`),
  CONSTRAINT `fk_Estoque_Produto`
    FOREIGN KEY (`Produto_codigo`)
    REFERENCES `cv`.`Produto` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Estoque_Produto_idx` ON `cv`.`Estoque` (`Produto_codigo` ASC) VISIBLE;

CREATE UNIQUE INDEX `idEstoque_UNIQUE` ON `cv`.`Estoque` (`idEstoque` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `cv`.`Venda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cv`.`Venda` ;

CREATE TABLE IF NOT EXISTS `cv`.`Venda` (
  `idVenda` INT NOT NULL AUTO_INCREMENT,
  `DataVenda` DATE NULL,
  `DataPagamento` DATE NULL,
  `Cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idVenda`),
  CONSTRAINT `fk_Venda_Cliente1`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `cv`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Venda_Cliente1_idx` ON `cv`.`Venda` (`Cliente_idCliente` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `cv`.`DescricaoVenda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cv`.`DescricaoVenda` ;

CREATE TABLE IF NOT EXISTS `cv`.`DescricaoVenda` (
  `Estoque_idEstoque` INT NOT NULL,
  `Venda_idVenda` INT NOT NULL,
  `quantidadeProduto` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Estoque_idEstoque`, `Venda_idVenda`),
  CONSTRAINT `fk_Estoque_has_Venda_Estoque1`
    FOREIGN KEY (`Estoque_idEstoque`)
    REFERENCES `cv`.`Estoque` (`idEstoque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Estoque_has_Venda_Venda1`
    FOREIGN KEY (`Venda_idVenda`)
    REFERENCES `cv`.`Venda` (`idVenda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Estoque_has_Venda_Venda1_idx` ON `cv`.`DescricaoVenda` (`Venda_idVenda` ASC) VISIBLE;

CREATE INDEX `fk_Estoque_has_Venda_Estoque1_idx` ON `cv`.`DescricaoVenda` (`Estoque_idEstoque` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
