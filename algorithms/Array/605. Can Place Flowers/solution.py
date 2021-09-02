class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        i = 0
        while i < len(flowerbed):
            if (0 < i < len(flowerbed) - 1):
                if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i < len(flowerbed) - 1:
                if flowerbed[i] == flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i - 1] == flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            if n == 0:
                return True
            i += 1
        return False
