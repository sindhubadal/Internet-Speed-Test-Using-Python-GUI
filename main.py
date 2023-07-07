from tkinter import *

import speedtest
#
# import threading


# def speedcheck():
def run_speedtest():
    sp = speedtest.Speedtest()

    sp.get_servers()

    down = str(round(sp.download() / (10 ** 6), 3)) + "Mbps"

    up = str(round(sp.upload() / (10 ** 6), 3)) + "Mbps"

    lab_down.config(text=down)

    lab_up.config(text=up)

    # # Create a thread to run the speed test
    #
    # speed_thread = threading.Thread(target=run_speedtest)
    #
    # speed_thread.start()


sp = Tk()

sp.title("INTERNET SPEED TEST")

sp.geometry("500x600")

sp.config(bg="pink")

lab = Label(sp, text="INTERNET SPEED TEST", font=("Times New Roman", 20, "bold"), bg="white", fg="black")

lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Downloading-Speed", font=("Comic", 20, "bold"), bg="pink", fg="black")

lab.place(x=60, y=120, height=50, width=380)

lab_down = Label(sp, text="00", font=("Comic", 20, "bold"), bg="white", fg="black")

lab_down.place(x=105, y=160, height=50, width=280)

lab = Label(sp, text="Uploading-Speed", font=("Comic", 20, "bold"), bg="pink", fg="black")

lab.place(x=60, y=250, height=50, width=380)

lab_up = Label(sp, text="00", font=("Comic", 20, "bold"), bg="white", fg="black")

lab_up.place(x=105, y=290, height=50, width=280)

button = Button(sp, text="Check Speed", font=("Times New Roman", 20, "bold"), bg="red", relief=RAISED,
                command=run_speedtest)

button.place(x=105, y=370, height=50, width=280)

sp.mainloop()