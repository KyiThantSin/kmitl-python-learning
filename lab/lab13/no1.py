def list_member(member, data):
     if member not in data:
         return False
     elif data[0] == member:
         return True
     else:
         return list_member(member, data[1:])

print(list_member(2,[1,2,3,7]))
print(list_member(8,[1,2,3,7]))