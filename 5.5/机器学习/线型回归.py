import tensorflow.compat.v1 as tf
import os

tf.disable_v2_behavior()

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
# g = tf.Graph
# print(g)
# with g().as_default():
#     c = tf.constant(11.0)
#     print(c.graph)
#
# a = tf.constant(5.0)
# b = tf.constant(6.0)
# sum1 = tf.add(a, b)
#
# graph = tf.get_default_graph()
# print(graph)
# with tf.Session() as sess:
#     print(sess.run(sum1))
#     print(a.graph)
#     print(sum1.graph)
#     print(sess.graph)


def myregression():
    with tf.variable_scope("data"):
        #准备特征值X,Y目标值
        x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name="x_data")
        #矩阵相乘，必须是二维的
        y_true = tf.matmul(x, [[0.7]]) + 0.8

    with tf.variable_scope("model"):
        #建立线性回归权重，特征
        weight = tf.Variable(tf.random_normal([1, 1], mean=0.0, stddev=1.0, name="w"))
        bias = tf.Variable(0.0, name="b")
        y_predict = tf.matmul(x, weight) + bias

    with tf.variable_scope("loss"):
        #建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope("optimizer"):
        #梯度下降优化损失
        train_op = tf.train.GradientDescentOptimizer(0.05535).minimize(loss)

    #定义一个初始变量OP
    init_op = tf.global_variables_initializer()

    #通过会话运行程序
    with tf.Session() as sess:
        #初始化变理
        sess.run(init_op)
        print("随机权重：%f,偏置：%f" % (weight.eval(), bias.eval()))
        #建立事件文件
        tf.summary.FileWriter("./tu/first/", graph=sess.graph)
        for i in range(500):
            sess.run(train_op)
            print(
                "第%d优化权重：%f,偏置：%f,损失:%f" % (i, weight.eval(), bias.eval(), loss.eval())
            )
    return None


if __name__ == "__main__":
    myregression()
