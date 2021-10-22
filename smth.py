# x = input("enter the name of the season")
# if x = "winter"
#     print("December January February")
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
    countdown(n-1)
    countdown(-1)
