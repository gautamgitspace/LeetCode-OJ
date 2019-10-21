class TimeMap:

    def __init__(self):
        self._dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dic[key].append((value, timestamp,))

    def get(self, key: str, timestamp: int) -> str:
        if key in self._dic:
            li = self._dic[key]
            l, r = 0, len(self._dic[key]) - 1

            if li[l][1] > timestamp:
                return ""
            elif li[r][1] <= timestamp:
                return li[r][0]
            else:
                while l <= r:
                    mid = l + (r - l) // 2

                    if li[mid][1] == timestamp:
                        return li[mid][0]

                    if li[mid][1] < timestamp:
                        l = mid + 1
                    else:
                        r = mid - 1

                return li[r][0]
        return ""
