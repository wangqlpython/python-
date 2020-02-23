import sklearn
import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def cutword():
    con1 = jieba.cut("我是中国人，你好，大好河山，你喜欢什么，我喜欢川菜")
    con2 = jieba.cut("唐诗三百首，你喜欢那首，我喜欢的可多了。")
    con3 = jieba.cut("你喜欢什么音乐，我喜欢流行歌曲")

    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    c1 = " ".join(content1)
    c2 = " ".join(content2)
    c3 = " ".join(content3)

    return c1, c2, c3


def hanzi():

    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    cv = CountVectorizer()
    data = cv.fit_transform([c1, c2, c3])
    print(cv.get_feature_names())
    print(data.toarray())
    return None


def dictvec():
    dict = DictVectorizer(sparse=False)
    # sparse False 显示为数据格式
    data = [
        {"city": "北京", "temp": 100},
        {"city": "成都", "temp": 10},
        {"city": "上海", "temp": 20},
    ]
    data2 = dict.fit_transform(data)
    print(dict.get_feature_names())  # 显示特征码
    print(data2)
    print(dict.inverse_transform(data2))  # 转回
    return None


def tfidfvec():
    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    tf = TfidfVectorizer()
    data = tf.fit_transform([c1, c2, c3])
    print(tf.get_feature_names())
    print(data.toarray())
    return None


def mm():
    mm = MinMaxScaler()
    list_data = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]
    data = mm.fit_transform(list_data)
    print(data)
    return None


def stand():
    std = StandardScaler()
    list_data = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]
    data = std.fit_transform(list_data)
    print(data)
    return None


if __name__ == "__main__":
    # hanzi()
    # dictvec()
    # tfidfvec()
    # mm()
    stand()
