ans = 0
right = 0
#n -> 数列の長さ
for left in range(n):
    while right < n:
        ここにrightが区間に入った時の処理を書く
        if ここに満たすべき条件を書く:
            right += 1
        else:
            ここにrightが区間から出たときの処理を書く
            break

    ここにansの更新式を書く

    if right == left:
        right += 1
    else:
        ここにleftが区間から出たときの処理を書く
