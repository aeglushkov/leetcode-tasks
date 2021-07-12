SELECT DISTINCT L1.Num AS 'ConsecutiveNums' FROM Logs AS L1, Logs AS L2, Logs AS L3
WHERE L1.Num = L2.Num and L2.Num = L3.Num and L2.Id = L1.Id + 1 and L3.Id = L2.Id + 1;