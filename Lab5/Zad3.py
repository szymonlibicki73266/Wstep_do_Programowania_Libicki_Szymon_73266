import time

def sekundnik(czas):
    while czas:
        mins, secs = divmod(czas, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        czas -= 1
    print("Czas minął!")