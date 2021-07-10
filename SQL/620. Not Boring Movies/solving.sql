SELECT * FROM Cinema
WHERE description  <> "boring" and id MOD 2 = 1
ORDER BY rating DESC;