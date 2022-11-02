CREATE TABLE IF NOT EXISTS cliente
(
    id       int auto_increment primary key,
    cpf      char(12)     not null,
    nome     VARCHAR(255) not null,
    email    VARCHAR(255) not null,
    telefone VARCHAR(11)  not null,
    senha    VARCHAR(30)  not null,
    saldo    float default 0.0
);

CREATE TABLE IF NOT EXISTS produto
(
    id         int auto_increment primary key,
    nome       VARCHAR(255) not null,
    categoria  VARCHAR(255) not null,
    descricao  VARCHAR(255) not null,
    quantidade int          not null,
    valor      float        not null
);

CREATE TABLE IF NOT EXISTS venda
(
    id          int auto_increment primary key,
    id_cliente  int   not null,
    valor_total float not null,
    data timestamp not null
);

CREATE TABLE IF NOT EXISTS produtos_vendidos
(
    id         int auto_increment primary key,
    id_produto int   not null,
    id_venda   int   not null,
    quantidade int   not null,
    valor      float not null
);
