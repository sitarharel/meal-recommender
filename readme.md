# Cornell Dining Hall Recommender

This is a python command line app that, once trained, will recommend the best dining hall for you for a meal. For now, this only owrks with dinner, as foods at different meals tend to be very different, thus making the training procedure longer. Additional meal may be added in the future.

### Training

Training the rcommender is a 3 step process. This process results in a database of food tastes for the user, that the recommender will use to recommend on-campus dining halls.

To begin, run 

```
python train_list.py load
```

This will initialize the training database with foods from the dining halls (this may take a couple minutes)

Next, run 

```
python train_list.py train
```

This will launch an interface that will print out different foods. Your job is to rate them from 0-5 by typing out the numbers 0, 1, 2, 3, 4, or 5 and pressing enter for each food. If you want to pause, simply type **q** and enter at any time. This can take a while and you can stop at any time, but the more foods you rate, the more accurate the recommendations will be.

Whenever you finish training, whether you decide to stop or the interface says that you are done, run the following:

```
python train_list.py index
```

This indexes the taste data so that the recommender works quickly. 

### Recommending

Once trained, recommending is simple. Just run:
```
python bestplace.py
```

This will print out a score and some foods you may like for each dining hall and at the end, recommend a dining hall for you.