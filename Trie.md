# BinaryTrie

BinaryTrieです。集合 $A$ への非負整数値の追加、削除、集合内の各要素と、与えられた $x$ に対して、各要素と xor を取った値として考えられる最小値がそれぞれ $ \Theta (\max(A)) $ で出来ます。


## コンストラクタ

> T = Trie(wordsize = 64)

wordsizeはビット数の最大値です。辞書順比較をするために、入力された値はこのビット数になるよう桁埋めされます。

例えば $x \leq 10^9$ なら wordsize = 32 にすれば良いです。

## add
> T.add(x)

集合に値 $x$ を追加します。すでに集合に $x$ がある場合は何もしません。

## remove

> T.remove(x)

集合から値 $x$ を削除します。集合内に $x$ がないときは何もしません。

## conteins

> T.conteins(x) -> bool

集合に $x$ が含まれるなら True 、含まれないなら False を返します。

## xormin

> T.xormin(x) -> int

集合の各要素に対し、 $x$ との XOR を計算した時の最小値を返します。

## verified with:

https://judge.yosupo.jp/submission/87387




