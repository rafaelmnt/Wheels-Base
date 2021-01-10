-- Criando e selecionando o banco de dados 

CREATE DATABASE wheels_base;

USE wheels_base;

-- Tabela dos clientes que pagam mensalmente para estacionar no local
 
CREATE TABLE mensal (
	id_mensal INT AUTO_INCREMENT,
	pri_nome VARCHAR(20) NOT NULL,
	seg_nome VARCHAR(20) NOT NULL,
	telefone INT,
	dia DATE NOT NULL,
	PRIMARY KEY(id_mensal)
 );

-- Tabela dos carros que estão cadastrados estacionamento como mensalistas

CREATE TABLE carro (
	placa VARCHAR(7),
	modelo VARCHAR(20),
    	id_mensal INT,
	PRIMARY KEY(placa),
    	FOREIGN KEY(id_mensal) REFERENCES mensal(id_mensal) ON DELETE CASCADE
);

-- Tabela dos clientes que compram uma diária para estacionar no local

CREATE TABLE diaria (
	id_dia INT AUTO_INCREMENT,
	placa VARCHAR(7) NOT NULL,
	modelo VARCHAR(20) NOT NULL,
	chegada TIME NOT NULL,
	saida TIME,
	PRIMARY KEY(id_dia)
);
