class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []

        self.data[key].append(
            (timestamp, value)
        )
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or self.data[key] == []:
            return ""
        arr = self.data[key]
        l = 0
        r = len(arr) - 1
        cand = ""
   
        while l <= r:
            mid = l + (r-l) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            
            elif arr[mid][0] > timestamp:      # if the mid value is too big, go into left half
                r = mid - 1
            
            else: # here mid is < timestamp so go into right half but save this value as a cand
                cand = arr[mid][1]
                l = mid + 1
        return cand
        

        
