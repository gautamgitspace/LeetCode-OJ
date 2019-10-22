class TimeMap:

    def __init__(self):
        self._dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dic[key].append((value, timestamp,))

    def get(self, key: str, timestamp: int) -> str:
        if key in self._dic:
            # fetch list at given key
            li = self._dic[key]
            # init L and R of the list
            l, r = 0, len(self._dic[key]) - 1

            # return empty string if asked for what
            # the KV store does not have stored
            if li[l][1] > timestamp:
                return ""
            # return the last one if timestamp
            # is in range or is equal to
            elif li[r][1] <= timestamp:
                return li[r][0]

            # do a BS on the TS
            else:
                while l <= r:
                    mid = l + (r - l) // 2

                    # found
                    if li[mid][1] == timestamp:
                        return li[mid][0]
                    # adjust l
                    if li[mid][1] < timestamp:
                        l = mid + 1
                    # adjust r
                    else:
                        r = mid - 1

                return li[r][0]
        return ""
