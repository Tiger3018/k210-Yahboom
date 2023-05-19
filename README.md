# K210-Yahboom-binds-eyes

## Datasets

Thanks to these datasets for acdemical use.

> <https://paperswithcode.com/datasets?q=traffic&v=lst&o=match> or pedestrian, bike, bicycle.

* <https://apolloscape.auto/trajectory.html>

* <https://data.mendeley.com/datasets/766ygrbt8y/3>

* <http://www.cbsr.ia.ac.cn/users/sfzhang/WiderPerson/>

* <https://www.kaggle.com/datasets/pengcw1/market-1501>

* <https://www.crcv.ucf.edu/data/UCF50.php>

## Training

* [model.py](./model.py) and the cost-free cloud training from <https://maixhub.com>.

> !! <https://developer.canaan-creative.com/> may also provide similar services.

You can try tfjs model from <https://maixhub.com/phone/deploy/model?type=classification&token=dcc525d655164c06aab4b8615c4145ab>.

1. [50342](./model-50342.kmodel) (Too large to load for the standard microPython installation)

```sh
+ mirror, + rotation, - blur, <contain>, 224, 224, Avg = 123.5, Std = 58.395
mobilenet_1.0
Epoches = 180, Batch = 128, Rate = .001, + data_balance
ValLoss = .18418, ValAcc = 1.0
```

2. [50343](./model-50343.kmodel) (Too large to load for the standard microPython installation)

```sh
+ mirror, + rotation, - blur, <fill>, 224, 224, Avg = 123.5, Std = 58.395
mobilenet_1.0
Epoches = 160, Batch = 128, Rate = .001, + data_balance
ValLoss = .44987, ValAcc = .79167
```

3. [50627](./model-50627.kmodel) (SELECTED)

```sh
+ mirror, + rotation, - blur, <fill>, 224, 224, Avg = 123.5, Std = 58.395
mobilenet_0.75
Epoches = 100, Batch = 64, Rate = .001, + data_balance
ValLoss = .37415, ValAcc = .91667
```

4. [50628](./model-50628.kmodel)

```sh
+ mirror, + rotation, - blur, <contain>, 224, 224, Avg = 123.5, Std = 58.395
mobilenet_0.5
Epoches = 100, Batch = 128, Rate = .001, + data_balance
ValLoss = .66497, ValAcc = .70833
```

5. [50629](./model-50629.kmodel)

```sh
+ mirror, + rotation, - blur, <fill>, 224, 224, Avg = 123.5, Std = 58.395
mobilenet_0.25
Epoches = 100, Batch = 32, Rate = .001, - data_balance
ValLoss = .58333, ValAcc = .89375
```

> It seems that blurring may contributes to better recognition.
