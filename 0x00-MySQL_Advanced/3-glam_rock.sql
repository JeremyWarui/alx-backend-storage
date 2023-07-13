-- Script that lists all bands with Glam rock
-- column names must be band_name, lifespan
SELECT `band_name`,
    COALESCE(`split`, 2020) - `formed` AS `lifespan`
FROM `metal_bands` WHERE `style` = `Glam rock`
ORDER BY `lifespan` DESC;
