-- Criação da tabela
CREATE TABLE vendas (
    quantity INTEGER,
    price NUMERIC(10, 2),
    country VARCHAR(50),
    stockcode VARCHAR(20),
    description TEXT,
    invoiceno VARCHAR(20),
    sale_date DATE
);

INSERT INTO vendas (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) VALUES
('536365', '85123A', 'WHITE HANGING HEART T-LIGHT HOLDER', 6, '2010-12-01 08:26:00', 2.55, 17850, 'United Kingdom'),
('536365', '71053', 'WHITE METAL LANTERN', 6, '2010-12-01 08:26:00', 3.39, 17850, 'United Kingdom'),
('536366', '84406B', 'CREAM CUPID HEARTS COAT HANGER', 8, '2010-12-01 08:28:00', 2.75, 17851, 'United Kingdom'),
('536367', '84029G', 'KNITTED UNION FLAG HOT WATER BOTTLE', 6, '2010-12-01 08:34:00', 3.39, 17852, 'United Kingdom');