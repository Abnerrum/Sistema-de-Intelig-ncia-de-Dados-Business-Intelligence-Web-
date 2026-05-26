USE dashboard;

-- Limpa a tabela para não duplicar se você já tiver algo
TRUNCATE TABLE vendas;

-- Insere 20 registros profissionais
INSERT INTO vendas (produto, valor, data_venda) VALUES 
('Notebook Gamer Dell', 5500.00, '2023-10-01'),
('Mouse Sem Fio Logitech', 120.00, '2023-10-05'),
('Monitor 4K LG 27p', 2300.00, '2023-10-10'),
('Cadeira Gamer RGB', 1500.00, '2023-10-15'),
('Teclado Mecânico Razer', 450.00, '2023-10-20'),
('Headset 7.1 HyperX', 380.00, '2023-10-25'),
('Webcam Full HD Logitech', 250.00, '2023-11-01'),
('SSD NVMe 1TB Kingston', 420.00, '2023-11-03'),
('Memória RAM 16GB Corsair', 350.00, '2023-11-05'),
('Placa de Vídeo RTX 3060', 3200.00, '2023-11-10'),
('Processador Intel i7', 1800.00, '2023-11-12'),
('Placa Mãe Asus B550', 950.00, '2023-11-15'),
('Fonte 750W 80 Plus Gold', 600.00, '2023-11-18'),
('Gabinete ATX Lateral Vidro', 400.00, '2023-11-20'),
('Impressora Laser HP', 1200.00, '2023-11-25'),
('Roteador Wi-Fi 6 TP-Link', 550.00, '2023-12-01'),
('HD Externo 2TB Seagate', 480.00, '2023-12-05'),
('Mesa de Escritório L', 800.00, '2023-12-10'),
('Suporte Articulado Monitor', 180.00, '2023-12-15'),
('Nobreak 1500VA SMS', 950.00, '2023-12-20');