# Creates a local copy of the MNIST-ReID datasets.

import copy
import numpy as np
import random
import pickle
import gzip

def createData(X, Y, corrupted = False, train = True):

    random.seed(0)

    digits = {}
    for d in range(10): digits[d] = []
    for i in range(Y.shape[0]):
        digits[Y[i]].append(X[i])
    digits_fixed = copy.deepcopy(digits)

    # Split into IDs.
    # Train ID are limited to IDs not divisible by 7.
    # Test ID queries are divisible by 7 but gallery from everywhere.

    ids = {}
    modeList = ['red','green','rg']  # Or 'pan'

    idList = list(range(100))
    if train:
        idList = [i for i in idList if not(i % 7 == 0)]

    mDict = {}
    for m in modeList: mDict[m] = []
    for d in idList:
        ids[d] = copy.deepcopy(mDict)

    madeNew = True
    while madeNew:
        madeNew = False
        for d in idList:
            d1 = d // 10
            d2 = d - 10 * d1

            m = random.choice(modeList)
            if not(train):
                ngs = len(ids[d]['red']) + len(ids[d]['green'])
                if d % 7 == 0:
                    if ngs >= 30: m = 'rg'
                else:
                    m = random.choice(modeList[:-1])
                    if ngs >= 30: continue

            if not(m == 'green') and len(digits[d1]) == 0: continue
            if not(m == 'red'):
                if len(digits[d2]) == 0: continue
                if (d1 == d2) and len(digits[d2]) == 1: continue

            if not(m == 'green'):
                im1 = digits[d1].pop(0)
                if corrupted and not(m == 'rg'):
                    dr = (d1 + random.randint(1,9)) % 10
                    imr = random.choice(digits_fixed[dr])
                    im1 = np.maximum(im1,imr)
                im1 = np.expand_dims(im1, -1)

            if not(m == 'red'):
                im2 = digits[d2].pop(0)
                if corrupted and not(m == 'rg'):
                    dr = (d2 + random.randint(1,9)) % 10
                    imr = random.choice(digits_fixed[dr])
                    im2 = np.maximum(im2,imr)
                im2 = np.expand_dims(im2, -1)

            if m == 'red':
                ids[d]['red'].append(im1)
            elif m == 'green':
                ids[d]['green'].append(im2)
            elif m == 'pan':
                ids[d]['pan'].append(np.maximum(im1,im2))
            else:
                ids[d]['rg'].append(np.concatenate((im1,im2), axis=-1))
            madeNew = True
        print('.', end='')
    print('Done')
    return ids



data_filename = './mnist.npz'
data = np.load(data_filename)
Xtr = data['x_train']
Ytr = data['y_train']
Xte = data['x_test']
Yte = data['y_test']

# Create pristine dataset

dataTr = createData(Xtr, Ytr, corrupted = False, train = True)
dataTe = createData(Xte, Yte, corrupted = False, train = False)

fid = gzip.open('./mnist_reid.pkz', 'wb')
pickle.dump((dataTr, dataTe), fid)
fid.close()

# Create corrupted dataset

dataTr = createData(Xtr, Ytr, corrupted = True, train = True)
dataTe = createData(Xte, Yte, corrupted = True, train = False)


fid = gzip.open('./mnist_reid_C.pkz', 'wb')
pickle.dump((dataTr, dataTe), fid)
fid.close()
