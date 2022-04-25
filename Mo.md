# Mo

Mo のアルゴリズムです。区間クエリが与えられるので全部やってください問題を、平方分割の考え方を用いることで高速に処理できるみたいです。

## Mo

> M = Mo(N, Q, A, LRs).ans

N は 数列の長さ、Q はクエリの個数、 A は与えられる数列、 LRs は 各クエリで与えられる (L, R) をタプルで並べた配列です。

Mo().ansはリストで、i番目の要素がi個目のクエリの答えになっています。

## in_query, out_query

問題に応じて、関数 in_query と out_query とその周辺を適宜変更してください。

尺取り法と同じ感覚で、区間内に x が入った時と、出たときの変化をそれぞれ書いてください。

## verified with:
Static Range Sum
https://judge.yosupo.jp/submission/87393

Range Pairing Query
https://atcoder.jp/contests/abc242/submissions/31267462

