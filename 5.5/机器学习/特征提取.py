import sklearn
import jieba
from sklearn.feature_extraction.text import CountVectorizer


def cutword():
    con1 = jieba.cut("我是中国人，你好，大好河山，你喜欢什么，我喜欢川菜")
    con2 = jieba.cut("唐诗三百首，你喜欢那首，我喜欢的可多了。")
    con3 = jieba.cut("你喜欢什么音乐，我喜欢流行歌曲")

    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    c1 = " ".join(content1)
    c2 = " ".join(content2)
    c2 = " ".join(content3)

    return c1, c2, c3


def hanzi():

    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    cv = CountVectorizer()
    data = cv.fit_transform([c1, c2, c3])
    print(cv.get_feature_names())
    print(data.toarray())
    return None


if __name__ == "__main__":
    hanzi()
