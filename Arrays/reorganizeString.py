class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)

        result = []

        while len(heap) >= 2:
            count1, ch1 = heapq.heappop(heap)
            count2, ch2 = heapq.heappop(heap)

            result.extend([ch1, ch2])

            count1 += 1
            count2 += 1

            if count1 < 0:
                heapq.heappush(heap, (count1, ch1))
            if count2 < 0:
                heapq.heappush(heap, (count2, ch2))

        if heap:
            count, ch = heapq.heappop(heap)

            if -count > 1:
                return ""

            result.append(ch)

        return "".join(result)  