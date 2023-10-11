-- Calculate the rank of country origins based on non-unique fans
SELECT origin, SUM(fans) as nb_fans FROM `metal_bands` GROUP BY origin ORDER BY nb_fans DESC;
