from sklearn import svm
from sklearn.model_selection import cross_validate
import numpy as np
from utils import plot_train_vald

def with_k_fold(train_data_x, train_data_y):
    prec = [0.2, 0.4, 0.6, 0.8, 1]
    acc_train = []
    acc_vald = []
    sampels_num = [int(x * len(train_data_x)) for x in prec]
    for k in sampels_num:
        # SVM
        # degree, gamma = ha'kafol (gamma * x_i * x_j), r = (b independedt), c = regulariztion
        # train_x_cross, train_y_cross = split_k(train_data_x[:int(len(train_data_x) * k)], train_data_y[:int(len(
        # train_data_y)*k)], 5)
        print(int(len(train_data_x) * k))
        # for i in range(5):
        '''## k fold
        x = []
        y = []
        [x.append(train_x_cross[j].copy()) for j in range(5) if j != i]
        [y.append(train_y_cross[j].copy()) for j in range(5) if j != i]
        x_train = np.concatenate(np.array(x))
        y_train = np.concatenate(np.array(y))

        x_vald = np.array(train_x_cross[i])
        y_vald = np.array(train_y_cross[i])'''

        clf = svm.SVC(C=1, kernel='poly', degree=3, gamma=1, coef0=0, max_iter=20000)  # c = 0 -> no penalety

        # a = clf.fit(x_train, y_train)
        result = cross_validate(clf, train_data_x[:k], train_data_y[:k], cv=5, scoring='accuracy',
                                return_train_score=True)
        '''y_hat = clf.predict(x_vald)
        print(np.sum(y_hat == y_vald) / len(y_vald))'''
        # result = cross_validate(clf, train_data_x, train_data_y, cv=5, scoring='accuracy', return_train_score=True)
        acc_vald.append(round(np.sum(result['test_score']) / len(result['test_score']), 3))
        acc_train.append(round(np.sum(result['train_score']) / len(result['train_score']), 3))
        print("vald: ", np.sum(result['test_score']) / len(result['test_score']))
        print("train: ", np.sum(result['train_score']) / len(result['train_score']))

    plot_train_vald(acc_train, acc_vald, sampels_num)

def witout_k_fold(train_data_x, train_data_y):
    training_set_size = int((4/5)*len(train_data_x))
    vald_x = train_data_x[training_set_size:, ]
    vald_y = train_data_y[training_set_size:]

    train_data_x = train_data_x[:training_set_size]
    train_data_y = train_data_y[:training_set_size]


    prec = [0.2, 0.4, 0.6, 0.8, 1]
    acc_train = []
    acc_vald = []
    sampels_num = [int(x * len(train_data_x)) for x in prec]
    for k in sampels_num:
        print(int(len(train_data_x) * k))
        clf = svm.SVC(C=1, kernel='poly', degree=3, gamma=1, coef0=0, max_iter=20000)

        a = clf.fit(train_data_x[:k], train_data_y[:k])
        y_hat = clf.predict(vald_x)
        print(np.sum(y_hat == vald_y) / len(vald_y))
        # result = cross_validate(clf, train_data_x, train_data_y, cv=5, scoring='accuracy', return_train_score=True)
        '''acc_vald.append(round(np.sum(result['test_score']) / len(result['test_score']), 3))
        acc_train.append(round(np.sum(result['train_score']) / len(result['train_score']), 3))
        print("vald: ", np.sum(result['test_score']) / len(result['test_score']))
        print("train: ", np.sum(result['train_score']) / len(result['train_score']))'''

    plot_train_vald(acc_train, acc_vald, sampels_num)