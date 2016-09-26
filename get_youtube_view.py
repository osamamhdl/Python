import time
import webbrowser

user = int(input('How many time do you want it to view? '))
# How many time do you want it to view?

if user < 1:
	print("Enjoy your Time\n" +time.ctime())
for count in range(user):
    time.sleep(5) 
    webbrowser.open("https://www.youtube.com/watch?v=o6A7nf3IeeA")
