create database Aluguel_Barcos;

CREATE TABLE Cliente (
    cliente_id int not null primary key auto_increment,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

select * from Cliente;


CREATE TABLE Barco (
    barco_id int not null primary key auto_increment,
    modelo VARCHAR(100),
    tipo VARCHAR(50),
    capacidade INT,
    descricao TEXT,
    preco_aluguel DECIMAL(10, 2)
);

select * from Barco;

CREATE TABLE Aluguel (
    aluguel_id int not null primary key auto_increment,
    cliente_id INT,
    barco_id INT,
    data_inicio DATE,
    data_termino DATE,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
    FOREIGN KEY (barco_id) REFERENCES Barco(barco_id)
);

alter table Aluguel add constraint fk_Cliente_Aluguel
foreign key(cliente_id) references cliente(cliente_id);

alter table Aluguel add constraint fk_Barco_Aluguel
foreign key(barco_id) references Barco(Barco_id);


select Aluguel.cliente_id, Aluguel.barco_id, Aluguel.data_inicio, Aluguel.data_termino, Aluguel.valor_total, Barco.modelo, Cliente.nome from Aluguel
join Barco on
Barco.barco_id = Aluguel.barco_id
join Cliente on
Cliente.cliente_id = Aluguel.cliente_id
order by nome;

select * from Aluguel;









