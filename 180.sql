SELECT l1.num as ConsecutiveNums
FROM Logs AS l1, Logs as l2, Logs as l3
WHERE l1.num=l2.num AND l1.num=l3.num AND l1.id=l2.id+1 AND l1.id= l3.id+2
GROUP BY l1.num