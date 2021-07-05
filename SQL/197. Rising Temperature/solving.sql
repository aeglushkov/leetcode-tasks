SELECT W1.Id FROM Weather AS W1, Weather AS W2
WHERE DATEDIFF(W1.recordDate, W2.recordDate) = 1 AND W1.Temperature > W2.Temperature;