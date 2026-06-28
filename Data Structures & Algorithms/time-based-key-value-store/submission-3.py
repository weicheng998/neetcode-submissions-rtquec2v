from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        v_list = self.m[key]
        if not v_list:
            return ""
        # Binary search through v for the largest timestamp_prev
        # v[i][0] is the prev timestamp and is strictly ascending
        l, r = 0, len(v_list) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            t, v = v_list[mid]
            if t == timestamp:
                return v
            elif t > timestamp:
                r = mid - 1
            else:  # t < timestamp
                res = v
                l = mid + 1
        return res
