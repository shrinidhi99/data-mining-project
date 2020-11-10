## Data mining project

* The objective of the project is to build a classifier which can find fake accounts on Twitter. The data set being constructed has the following structure.

| has_name | has_image | has_address | has_bio | profile_has_url | present_in_list | follower_count | tweet_count | friends_to_follower_ratio | age |
|----------|-----------|-------------|---------|-----------------|-----------------|----------------|-------------|---------------------------|-----|

| Feature                   | Data Type | Description                                                                   |
|---------------------------|-----------|-------------------------------------------------------------------------------|
| has_name                  | boolean   | Checks if account has a name                                                  |
| has_image                 | boolean   | Checks if account has all three images, profile background and something else |
| has_address               | boolean   | Checks if account has address                                                 |
| has_bio                   | boolean   | Checks if account has a bio                                                   |
| profile_has_url           | boolean   | Checks if account has a URL in the profile description                        |
| present_in_list           | boolean   | Checks if account is a part of a list for another account                     |
| follower_count            | integer   | The number of accounts following the considered account                       |
| tweet_count               | integer   | The number of tweets posted by the account                                    |
| friends_to_follower_ratio | float     | The ratio of friends to followers, if followers are 0 then set to 1,00,000    |
| Label                     | boolean   | Tells if the account is real or not                                           |
