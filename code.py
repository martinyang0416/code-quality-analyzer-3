import heapq

def mincostToHireWorkers(quality, wage, K):
    workers = sorted((w / q, q) for q, w in zip(quality, wage))
    heap = []
    sum_q = 0
    res = float('inf')
    for ratio, q in workers:
        heapq.heappush(heap, -q)
        sum_q += q
        if len(heap) > K:
            sum_q += heapq.heappop(heap)  # Pop the largest quality (stored as negative)
        if len(heap) == K:
            res = min(res, ratio * sum_q)
    return res