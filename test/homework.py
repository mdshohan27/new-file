myfamily={
   " person1":{"name":"Alex","year":1995},
   " person2":{"name":"Sophia","year":1998},
   " person3":{"name":"Ethan","year":2002}
}
for family,details in myfamily.items():
    print(f"Family:{family}")
    print(f'Name:{details['name']}')
    print(f'year:{details ['year']}')