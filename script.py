file_followers = open('friends.csv', 'a')
file_1 = open('TWT.csv/friends.csv', 'r')

Lines = file_1.readlines()

file_followers.writelines(Lines)

file_1.close()
file_followers.close()
