romantic_movie1 = ("The Pricess Bride",1987,98,
                   "The story of a man and a women who lived happily ever after.",
                  ["Buttercup","Westley","Fezzik","Inigo Montoya","Vizzini"])

romantic_movie2 = ("Groundhog Day", 1993, 101,
                  "He is having the day of his life..... over and over again.",
                  ["Phil Connors"])

romantic_movie3 = ("Amelie",2001, 122, "One person can change your life forever.",
                   ["Amelie Poulain","Nino Quincampoix","The Garden Gnome"])


print(f'Here are my favourite romance movies:\n'
      f'{romantic_movie1[0]} ({romantic_movie1[1]}): {romantic_movie1[3]}\n'
      f'{romantic_movie2[0]} ({romantic_movie2[1]}): {romantic_movie2[3]}\n'
      f'{romantic_movie3[0]} ({romantic_movie3[1]}): {romantic_movie3[3]}')

employees ={
         "name": ["Ron Swanson","Leslie Knope","Andy Dwyer","April Ludgate"],
         "age": 55,
         "department": ["Management","Middle Management","Shoe Shining","Administration"],
         "phone": ["555-1234","555-4321","555-1122","555-3345"],
         "salary": "100,000"
            }

for i in range(len(employees["name"])):
    name = employees["name"][i]
    department = employees["department"][i]
    phone = employees["phone"][i]
    print(f"{name} in {department} can be reached at {phone}.")