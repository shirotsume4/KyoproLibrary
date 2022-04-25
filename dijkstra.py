INF = 2 ** 63 - 1
def dijkstra(s, graph):
    import heapq
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    bef = [0] * n
    bef[s] = s
    hq = [(0, s)]
    visit = [False] * n
    heapq.heapify(hq)
    while hq:
        c, now = heapq.heappop(hq)
        visit[now] = True
        if c > dist[now]:
            continue
        for to, cost in graph[now]:
            if (not visit[to]) and dist[now] + cost < dist[to]:
                dist[to] = cost + dist[now]
                bef[to] = now
                heapq.heappush(hq, (dist[to], to))
    return dist, bef

def rest(bef, t):
    now = t
    ret = []
    while bef[now] != now:
        ret.append((bef[now], now))
        now = bef[now]
    ret.reverse()
    return ret

