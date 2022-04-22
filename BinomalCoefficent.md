# BinomalCoefficent
二項係数のライブラリです。入力の最大値を $$maxi$$ とすると対し前計算が $ \Theta(maxi) $ かかります。デフォルトでは $maxi = 3 \times 10^6$ となっています。

## コンストラクタ

>hoge = BinomalCoefficent(MOD)

MOD はあらかじめ決められた <strong>素数</strong> です。



## choose
>def choose(self, n, k) -> int:\
>hoge.choose(n, k)

${}n C_k  \mod MOD$ を返します。

### 制約
$-10^{18} \le n < MOD$\
$-10^{18} \le k < MOD$

## perm
>def perm(self, n, k) -> int:\
>hoge.perm(n, k)

${}n P_k  \mod MOD$ を返します。

### 制約
$-10^{18} \le n < MOD$\
$-10^{18} \le k < MOD$

## homop
>def homop(self, n, k) -> int:\
>hoge.homop(n, k)

${}n H_k  \mod MOD$ を返します。

### 制約

$-10^{18} \le n < MOD$\
$-10^{18} \le k < MOD$\
$-10^{18} \le n + k - 1 < MOD$

## 備考
負の値が入力された際は、単に0が返ってきます。（負の二項係数には対応していません）

計算量は、構築 $\Theta (maxi)$ 、 クエリ $\Theta (1) $ です。

## verified with:
https://yukicoder.me/submissions/755211

https://atcoder.jp/contests/agc054/submissions/31145776 (TL が厳しいので、maxiの調整と入力の高速化が必要)
