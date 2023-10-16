users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
all_users = len(users)
uniq_users=[]
for user in users:
    if user not in uniq_users:
        uniq_users.append(user)
people=len(uniq_users)
print({'Общее количество': all_users, 'Уникальные посещения': people})