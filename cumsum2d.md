# cumsum2d （一次元累積和）

$X \times Y$ の二次元配列に対して、区間 $[x_1, x_2] \times [y_1, y_2]$ の要素の総和を前計算 $\Theta(XY)$ 、クエリ $\Theta (1) $ で行えるデータ構造です。

他のライブラリと異なり、区間は <strong>閉区間</strong> で定められることに注意してください。

## コンストラクタ

>hoge = cumsum2d(A)

A は二次元配列です。要素 $A_{i, j}$ に <code> A[i][j] </code> としてアクセスできれば <code>list</code> じゃなくても大丈夫です。　Aの各要素に対し加減算が定義されているなら <code>int</code> で無くても構いません。

（例えば個人で定義したクラスを載せるなどしても大丈夫です）

##  query

> hoge.query(x1, y1, x2, y2) -> int

$\displaystyle \sum_{i = x_1}^{x_2} \sum_{j = y_1}^{y_2} A_{i, j}$ を出力します。

### 制約

$0 \le x_1 \le x_2 < X$

$0 \le y_1 \le y_2 < Y$