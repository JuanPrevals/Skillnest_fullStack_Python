USE `esquema_tacos`;

INSERT INTO `tacos` (`tortilla`, `guiso`, `salsa`) VALUES
    ('Maíz', 'Carne asada', 'Verde'),
    ('Harina', 'Pollo', 'Roja'),
    ('Maíz azul', 'Champiñones', 'Aguacate');

INSERT INTO `complementos` (`nombre_complemento`) VALUES
    ('Cebolla'),
    ('Cilantro'),
    ('Limón');

INSERT INTO `complementos_en_tacos` (`complemento_id`, `taco_id`) VALUES
    (1, 1),
    (2, 1),
    (3, 1),
    (1, 2),
    (3, 2),
    (2, 3);

