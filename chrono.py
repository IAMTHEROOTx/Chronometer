import time

print("WELCOME IN MINUTOR")
print("IAMTHEROOTx made this script")

sec_timer = 0
sec_intervalle = 0

start = (input("You ready to start the minutor: "))

if start == "Yes" or "yes" or "YES":
    sec_timer = int(input('Enter a time in seconds: '))
    sec_intervalle = float(input('Enter an interval of seconds between each secondes: '))
    print("MINUTOR ON") 
    while sec_timer > 0:
        print(f"Il vous manque {sec_timer} secondes.")
        sec_timer -= 1
        time.sleep(sec_intervalle)
    print("The time is done!!!")
else:
    print("You quit the MINUTOR")
