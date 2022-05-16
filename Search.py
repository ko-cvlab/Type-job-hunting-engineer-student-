from operator import index
from sys import flags

def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
    # ここから記述
    # 配列の始まりと終わりのindexをそれぞれ初期化する．
    index_start,index_finish = 0,len(sorted_array)-1
    # 配列の始まりのindexが終わりのindexより大きくなったら繰り返しを中止する．
    while index_start <= index_finish:
        # 配列の中央の値のindexを整数値で求める．
        index_middle = (index_start+index_finish)//2
        # "探索対象の数値"が"配列の中央の値"と等しいとき，配列の中央の値のindexを返す．
        if target_number == sorted_array[index_middle]:
            return index_middle
        # "探索対象の数値"が"配列の中央の値"より大きいとき，始まりのindexを中央の値のindex+1にする．
        elif target_number > sorted_array[index_middle]:
            index_start = index_middle + 1
        # それ以外のとき("探索対象の数値"が"配列の中央の値"より小さいとき)，終わりのindexを配列の中央の値のindex-1にする．
        else:
            index_finish = index_middle - 1
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()