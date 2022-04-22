# cumsum1d （一次元累積和）

長さ $N$ の配列に対して、区間の要素の総和を前計算 $\Theta(N)$ 、クエリ $\Theta (1) $ で行えるデータ構造です。

他のライブラリと異なり、区間は <strong>閉区間</strong> で定められることに注意してください。

## コンストラクタ

>hoge = cumsum1d(A)

A は配列 $A = (A_0, A_1, \dots, A_{N - 1})$ です。Aの各要素に対し加減算が定義されているなら <code>int</code> で無くても構いません。

（例えば個人で定義したクラスを載せるなどしても大丈夫です）

##  query

> hoge.query(l, r) -> int

$\displaystyle \sum_{i = l}^{r} A_i$ を出力します。

## get

> hoge.get(i) -> int

$A_i$ を出力します。
