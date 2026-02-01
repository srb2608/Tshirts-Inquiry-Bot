-- Create the database
CREATE DATABASE atliq_tshirts_new;
USE atliq_tshirts_new;

-- Create the t_shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL,
    size ENUM('XS', 'S', 'M', 'L', 'XL') NOT NULL,
    price INT CHECK (price BETWEEN 10 AND 50),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_color_size (brand, color, size)
);

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    t_shirt_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100)
    #FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id)
);
ALTER TABLE atliq_tshirts_new.discounts
ADD CONSTRAINT constraint_name
FOREIGN KEY (t_shirt_id)
REFERENCES t_shirts(t_shirt_id);

