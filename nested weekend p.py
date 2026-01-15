#nested decisions in python
print("************welcome to weekend planner**********")
name=input("enter your name:")
mood=input("enter your mood (happy/ sad/ tired):").lower()
budget=int(input("enter your budget ($):"))
weather=input("Weather today? (sunny /rainy/cold):").lower()
company=input("who are you with? (alone/friend/family):").lower()

print("\n planning weekend..\n")
if mood=="happy":
    if budget>1000:
        if weather=="sunny":
            if comapny=="friends":
                print(f"dear {name}, for an outdoor movie + street food party!")
            
            else:
                print("watch block buster movie!")
        else:
            print("Order pizza + Netflix at home")
    else:
        print("watch comedy movie on mobile with snacks!!!")
elif mood=="sad":
    if comapny=="alone":
        print("watch motivatioal movie and order comfort food!")
    else:
        if budget > 500:
            print("Ice-cream + Feel-good movie with loved ones!")
        else:
             print("Team + old classic movie!")
elif mood=="tired":
    if weather=="cold":
        print("sleep early + light Music!")
    else:
        if budget > 300:
            print("Fast food + and watch comedy show!")
        else:
            print("Relax with music book!")
else:
    print("Mood not recpgnized, just relax and enjoy your time!")
    