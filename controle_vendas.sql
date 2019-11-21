SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE DATABASE IF NOT EXISTS `ControleDeVendas` DEFAULT CHARACTER SET utf8 ;
USE `ControleDeVendas`;

-- -----------------------------------------------------
-- Table `ControleDeVendas`.`Marca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ControleDeVendas`.`Marca` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ControleDeVendas`.`Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ControleDeVendas`.`Produto` (
  `codigo` INT NOT NULL,
  `Descricao` VARCHAR(60) NOT NULL,
  `Linha` VARCHAR(25) NOT NULL,
  `Marca_idMarca` INT NOT NULL,
  PRIMARY KEY (`codigo`),
  CONSTRAINT `fk_Produto_Marca1`
    FOREIGN KEY (`Marca_idMarca`)
    REFERENCES `ControleDeVendas`.`Marca` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Produto_Marca1_idx` ON `ControleDeVendas`.`Produto` (`Marca_idMarca` ASC);

CREATE UNIQUE INDEX `codigo_UNIQUE` ON `ControleDeVendas`.`Produto` (`codigo` ASC);


-- -----------------------------------------------------
-- Table `ControleDeVendas`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ControleDeVendas`.`Cliente` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(60) NULL,
  `Telefone` VARCHAR(45) NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Nome_UNIQUE` ON `ControleDeVendas`.`Cliente` (`Nome` ASC);


-- -----------------------------------------------------
-- Table `ControleDeVendas`.`Estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ControleDeVendas`.`Estoque` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `Quantidade` INT NOT NULL DEFAULT 0,
  `Validade` DATE NULL,
  `Produto_codigo` INT NOT NULL,
  `Preco` DECIMAL(2) NULL,
  PRIMARY KEY (`codigo`),
  CONSTRAINT `fk_Estoque_Produto`
    FOREIGN KEY (`Produto_codigo`)
    REFERENCES `ControleDeVendas`.`Produto` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Estoque_Produto_idx` ON `ControleDeVendas`.`Estoque` (`Produto_codigo` ASC);

CREATE UNIQUE INDEX `codigo_UNIQUE` ON `ControleDeVendas`.`Estoque` (`codigo` ASC);

-- -----------------------------------------------------
-- Table `ControleDeVendas`.`Venda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ControleDeVendas`.`Venda` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `DataVenda` DATE NULL,
  `DataPagamento` DATE NULL,
  `Cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`codigo`),
  CONSTRAINT `fk_Venda_Cliente1`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `ControleDeVendas`.`Cliente` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Venda_Cliente1_idx` ON `ControleDeVendas`.`Venda` (`Cliente_idCliente` ASC);
-- -----------------------------------------------------
-- Table `ControleDeVendas`.`DescricaoVenda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ControleDeVendas`.`DescricaoVenda` (
  `Estoque_idEstoque` INT NOT NULL,
  `Venda_idVenda` INT NOT NULL,
  `quantidadeProduto` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Estoque_idEstoque`, `Venda_idVenda`),
  CONSTRAINT `fk_Estoque_has_Venda_Estoque1`
    FOREIGN KEY (`Estoque_idEstoque`)
    REFERENCES `ControleDeVendas`.`Estoque` (`idEstoque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Estoque_has_Venda_Venda1`
    FOREIGN KEY (`Venda_idVenda`)
    REFERENCES `ControleDeVendas`.`Venda` (`idVenda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Estoque_has_Venda_Venda1_idx` ON `ControleDeVendas`.`DescricaoVenda` (`Venda_idVenda` ASC);

CREATE INDEX `fk_Estoque_has_Venda_Estoque1_idx` ON `ControleDeVendas`.`DescricaoVenda` (`Estoque_idEstoque` ASC);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;