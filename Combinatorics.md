# Combinatorics
組み合わせのライブラリです。入力の最大値を $maxi$ とすると対し前計算が $ \Theta(maxi) $ かかります。デフォルトでは $maxi = 3 \times 10^6$ となっています。

## コンストラクタ

>hoge = Combinatorics(MOD)

MOD はあらかじめ決められた <strong>素数</strong> です。



## choose
>def choose(self, n, k) -> int:\
>hoge.choose(n, k)

${}n C_k  \mod MOD$ を返します。

### 制約
$-10^{18} \le n < maxi$\
$-10^{18} \le k < maxi$

## perm
>def perm(self, n, k) -> int:\
>hoge.perm(n, k)

${}n P_k  \mod MOD$ を返します。

### 制約
$-10^{18} \le n < maxi$\
$-10^{18} \le k < maxi$

## homop
>def homop(self, n, k) -> int:\
>hoge.homop(n, k)

${}n H_k  \mod MOD$ を返します。

### 制約

$-10^{18} \le n < maxi$\
$-10^{18} \le k < maxi$\
$-10^{18} \le n + k - 1 < maxi$

## factorial
> hoge.factorial(n)

$ n! \mod MOD $ を返します。 $ 0! = 1 $ です。

### 制約

$ 0 \le n \le maxi$

## 備考
負の値が入力された際は、単に0が返ってきます。（負の二項係数には対応していません）

計算量は、構築 $\Theta (maxi)$ 、 クエリ $\Theta (1) $ です。

## verified with:
https://yukicoder.me/submissions/755756

https://atcoder.jp/contests/agc054/submissions/31164591 (TL が厳しいので、maxiの調整と入力の高速化が必要)
