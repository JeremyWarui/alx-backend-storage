-- Script that create a trigger that decreases quantity of an items after adding new order
-- Quantity in table items cn be negative
CREATE TRIGGER order_decrease BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
