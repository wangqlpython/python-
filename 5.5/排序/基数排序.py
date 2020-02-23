def RadixSort(list):
    i = 0  # 初始为个位排序
    n = 1  # 最小的位数置为1（包含0）
    max_num = max(list)  # 得到带排序数组中最大数
    while max_num > 10 ** n:  # 得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}  # 用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])  # 将每个桶置空
        for x in list:  # 对每一位进行排序
            radix = int((x / (10 ** i)) % 10)  # 得到每位的基数
            bucket[radix].append(x)  # 将对应的数组元素加入到相 #应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:  # 若桶不为空
                for y in bucket[k]:  # 将该桶中每个元素
                    list[j] = y  # 放回到数组中
                    j += 1
        i += 1

    return list

if __name__ == "__main__":
    str1 = [6, 1, 25, 7, 9, 35, 4, 5, 10, 8]
    print(RadixSort(str1))
