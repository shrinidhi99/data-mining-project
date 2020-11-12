# Data mining project
## Building the features, dataset and classifiers for Fake accounts detection

* The objective of the project is to perform a comparative study on different classifier which can be used for find fake account detection on Twitter. 

* This implementation is based on [this paper](https://www.iit.cnr.it/node/25087). The data set being used has the following structure.

| has_name | has_image | has_address | has_bio | profile_has_url | present_in_list | friend_count | follower_count | tweet_count | friends_to_follower_ratio | label |
|----------|-----------|-------------|---------|-----------------|-----------------|--------------|----------------|-------------|---------------------------|-----|

| Feature                   | Data Type | Description                                                                   |
|---------------------------|-----------|-------------------------------------------------------------------------------|
| has_name                  | boolean   | Checks if account has a name                                                  |
| has_image                 | boolean   | Checks if account has all three images, profile background and something else |
| has_address               | boolean   | Checks if account has address                                                 |
| has_bio                   | boolean   | Checks if account has a bio                                                   |
| profile_has_url           | boolean   | Checks if account has a URL in the profile description                        |
| present_in_list           | boolean   | Checks if account is a part of a list for another account                     |
| friend_count              | integer   | The number of accounts the considered account follows                         |
| follower_count            | integer   | The number of accounts following the considered account                       |
| tweet_count               | integer   | The number of tweets posted by the account                                    |
| friends_to_follower_ratio | float     | The ratio of friends to followers, if followers are 0 then set to 1,00,000    |
| Label                     | boolean   | Tells if the account is real or not                                           |

In the data collected there are about 5000+ accounts information with about 3000+ fake accounts. The data set was divided in 80/20 ratio for trainng and testing; maintaining the same distribution within each category.

All the above features can be computed from the profile of the twitter account, and arent very computationally expensive. There are other features which are based on the relations between accounts, like average neighbours followers, tweet similarity etc which are more difficult to calculate comparatively.

Some of the classifiers which have been used on the gathered data set are - decision tree, random forest, Adaboost, SVM etc.
