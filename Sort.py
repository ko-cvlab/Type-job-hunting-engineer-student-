from itertools import starmap
from turtle import end_fill


def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array
    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # 先頭から探索するためのindexと末尾から探索するためのindexをそれぞれ初期化する．
    index_left, index_right = 0, len(array) - 1
    #先頭からの探索と、末端からの探索がぶつかるまで探索する．
    while(index_left < index_right):
        # 先頭から基準値より大きい位置まで移動する．
        while(array[index_left] < pivot):
            index_left += 1
        # 末尾から基準値より小さい位置まで移動する．
        while(array[index_right] > pivot):
            index_right -= 1
        # 先頭から探索してきたindexと末尾から探索してきたindexがぶつかっていないとき，それらの値同士を交換する．
        if (index_left <= index_right):
            array[index_left], array[index_right] = array[index_right], array[index_left]
        # それ以外のとき(交換する部分がないとき)，探索を終了する．
        else:
            break
    # 左右２つに配列を分割してsort関数を再帰的に繰り返す．
    # pivot未満のグループの長さが1かつ0でないとき，pivot未満のグループを作成する．
    if len(array[:index_left]) not in [0, 1]:
        array[:index_left] = sort(array[:index_left])      
    # pivot以上のグループの長さが1かつ0でないとき，pivot以上のグループを作成する．
    if len(array[index_left+1:]) not in [0, 1]:
        array[index_left+1:] = sort(array[index_left+1:])  
    # 昇順にソートされた配列を返す．
    return array
    # ここまで記述

if __name__ == '__main__':
    main()