SELECT name, population, area FROM World
WHERE area > 3 * POWER(10, 6) or population > 25 * POWER(10, 6);

## Using UNION
# SELECT
#     name, population, area
# FROM
#     world
# WHERE
#     area > 3000000
# UNION
# SELECT
#     name, population, area
# FROM
#     world
# WHERE
#     population > 25000000;
