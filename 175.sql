SELECT Person.firstName as firstName, Person.lastName as lastName, Address.city AS city, Address.state AS state from Person LEFT JOIN Address ON Address.personId=Person.personId
g