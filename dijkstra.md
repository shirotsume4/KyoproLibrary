# dijkstra

ダイクストラ法です。復元もあります。

## dijkstra

> dist, bef = dijkstra(s, graph)

s は始点の頂点番号、graphは隣接リストで与えられるグラフを表す配列です。

> graph = [[] for _ in range(n)]

として、graph[i] が頂点iに隣接する頂点のリストとなるようにすれば大丈夫です。

返り値である dist は頂点sから各頂点までの最短距離が入った配列、bef は経路の復元に用いる配列です。
経路の復元をする必要がないときはbefを削除しても良いです。

## rest

> path = rest(t, bef)

経路の復元を行う関数です。

path には、sからtまでの経路で通った辺を (u, v) のタプルとして入れた配列が返されます。

## verified with:

https://judge.yosupo.jp/submission/87330