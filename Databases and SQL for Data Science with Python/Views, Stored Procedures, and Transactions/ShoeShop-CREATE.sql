DROP TABLE IF EXISTS ShoeShop;

CREATE TABLE ShoeShop (
    Product VARCHAR(25) NOT NULL,
    Stock INTEGER NOT NULL,
    Price DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (Product),
    CHECK(Price>0)
    );

INSERT INTO ShoeShop VALUES
('Boots',11,200),
('High heels',8,600),
('Brogues',10,150),
('Trainers',14,300);



SELECT * FROM ShoeShop;