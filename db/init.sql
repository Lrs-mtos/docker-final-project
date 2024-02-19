CREATE TABLE IF NOT EXISTS exemplo (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    descricao TEXT,
    data_criacao DATE NOT NULL DEFAULT CURRENT_DATE
);

INSERT INTO exemplo (nome, descricao) VALUES 
('Amaranth', 'A purple grain cultivated by an ancient civilization'),
('Kale', 'The waxy leaves are great in soups and stir frys'),
('Cave Carrot', 'A starchy snack found in caves. It helps miners work longer'),
('Hops', 'A bitter, tangy flower used to flavor beer');
