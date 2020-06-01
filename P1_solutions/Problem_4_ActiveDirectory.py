class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
   
    groups = group.get_groups()
    users = group.get_users()
   
    if user in users:
        # status = "True"
        return True
    else:        
        for gr in groups:
            if is_user_in_group(user,gr):
            # status = "True"
                return True
 
    return False
   

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

usr1 = "user1"
usr2 = "user2"
usr3 = "user3"
usr4 = "user4"

grp =  Group("headquater")
sub_grp1 = Group("office1")
sub_grp2 = Group("office2")
sub_sub_grp = Group("remote_group")

grp.add_user(usr1)
grp.add_user(usr2)
grp.add_group(sub_grp1)
grp.add_group(sub_grp2)
sub_grp1.add_user(usr3)
sub_grp2.add_group(sub_sub_grp)
sub_sub_grp.add_user(usr4)

# print(is_user_in_group(usr4, sub_grp2))
#Test 1
print ("Pass" if (is_user_in_group(usr1, grp) == True) else "Fail")

#Test 2
print ("Pass" if (is_user_in_group(usr3, sub_grp1) == True) else "Fail")

#Test 3
print ("Pass" if (is_user_in_group(usr3, sub_sub_grp) == False) else "Fail")

#Test 4
print ("Pass" if (is_user_in_group(sub_child_user,sub_child) == True) else "Fail")

