def Dijkstra(s, graph):
    INF = 2 ** 63 - 1
    half = 10 ** 6
    import heapq
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    bef = [0] * n
    bef[s] = s
    hq = [0 * half + s]
    heapq.heapify(hq)
    while hq:
        x = heapq.heappop(hq)
        c = x // half
        now = x % half
        
        if c > dist[now]:
            continue
        for to, cost in graph[now]:
            if dist[now] + cost < dist[to]:
                dist[to] = cost + dist[now]
                bef[to] = now
                heapq.heappush(hq, dist[to] * half + to)
    return dist, bef

def DijkstraRest(bef, t):
    now = t
    ret = []
    while bef[now] != now:
        ret.append((bef[now], now))
        now = bef[now]
    ret.reverse()
    return ret

