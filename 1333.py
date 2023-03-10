class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:

        return [
            r[0]
            for r in sorted(
                [
                    r
                    for r in restaurants
                    if veganFriendly == 0 or (veganFriendly == 1 and r[2] == 1)
                    if r[3] <= maxPrice
                    if r[4] <= maxDistance
                ],
                key=lambda r: (r[1], r[0]),
                reverse=True,
            )
        ]
