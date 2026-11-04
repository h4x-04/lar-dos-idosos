-- SCRIPT SQL DE CRIAÇÃO DO BANCO DE DADOS
-- Projeto: Portal Lar dos Idosos WB
-- Disciplina: Atividades Extensionistas - Tecnologia Aplicada à Inclusão Digital

CREATE TABLE IF NOT EXISTS doacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_doador TEXT NOT NULL,
    telefone TEXT NOT NULL,
    tipo_doacao TEXT NOT NULL,          -- Ex: Produtos de Higiene, Fraldas Geriátricas, Alimentos, PIX
    descricao_itens TEXT NOT NULL,      -- Detalhes (ex: 5 pacotes de sabonete, 2 fardos de fralda G)
    horario_preferencial TEXT NOT NULL, -- Ex: Manhã (até 12h), Tarde (até 17h)
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'Pendente'      -- 'Pendente' ou 'Recebido'
);

-- Inserção de dados iniciais para demonstração acadêmica
INSERT INTO doacoes (nome_doador, telefone, tipo_doacao, descricao_itens, horario_preferencial, status)
VALUES 
('Comunidade Vila Santa Maria', '(43) 99888-1122', 'Produtos de Higiene', '10 sabonetes e 3 cremes dentais', 'Manhã', 'Recebido'),
('Voluntários de Wenceslau Braz', '(43) 99111-2233', 'Fraldas Geriátricas', '4 pacotes de fralda tamanho G', 'Manhã', 'Pendente');
