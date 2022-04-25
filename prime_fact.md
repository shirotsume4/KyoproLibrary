# prime_fact

素数判定及び素因数分解のアルゴリズムです。
素数判定はミラー-ラビン法、素因数分解はポラードのロー法を用いています。

# is_prime

> is_prime(N) -> bool

N が素数なら True、 素数でないなら False を返します。

ミラー-ラビン法は本来確率的にしか判定ができませんが、N <= 10^18 の範囲において、 23　以下の素数において判定を行えば確定的に判定ができるみたいです。

# prime_fact

> prime_fact(N) -> list

N を素因数分解した時のリストを返します。

## verified with:

https://judge.yosupo.jp/submission/87396