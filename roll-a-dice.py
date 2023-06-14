import random
response=input("Do you want to roll a dice ")

def countdown_timer(response):
    while response == "y":
        no=random.randint(1,6)
        yes=random.randint(1,6)

        timer=f'{no}:{yes}:'
        print(timer,end="\r")
        random.sleep(1)
        response=response-1
    print("time up")
    
countdown_timer (int(response))    

