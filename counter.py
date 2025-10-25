from tkinter import *
from tkinter import filedialog

WINDOW_SIZE = "500x500"
WINDOW_COLOR = "#333232"
MAIN_FONT = "Impact"
BASE_TITLE = "Elden Ring - Death Counter"
ICON_FILE_PATH ="config\icon.png"
SAVE_FILE_PATH = "config\count.txt"

death_count : int = 0

def window_creator():
    window = Tk()
    window.title(BASE_TITLE)
    window.geometry(WINDOW_SIZE)
    window.resizable(False, False)
    window.config(bg = WINDOW_COLOR)
    icon_image = PhotoImage(file = ICON_FILE_PATH)
    window.iconphoto(True, icon_image)

    LoadSaveFile()

    return window

def OnIncreaseClick():
    global death_count
    death_count += 1
    counter_label.config(text=str(death_count))

def ResetCount():
    global death_count
    death_count = 0
    counter_label.config(text=str(death_count))

def AutoSaveFileOnExit():
    SaveFile()
    main_window.destroy()

def SaveFile(): 
    try: 
        save = open(SAVE_FILE_PATH, "w")
        fileCountText = str(death_count)
        save.write(fileCountText)
        save.close()
    except:
        print("⚠️ Could not save the file.")

def LoadSaveFile():
    try:
        load = open(SAVE_FILE_PATH, "r")
        content = load.read()

        global death_count
        death_count = int(content)
    except:
        print("⚠️ No save file found.")


main_window = window_creator()

counter_label = Label(main_window,
                      text = str(death_count),
                      font = (MAIN_FONT, 100, "bold"),
                      bg = WINDOW_COLOR,
                      fg = "#FFFFFF")

counter_button = Button(main_window,
                        text="+1",
                        font=(MAIN_FONT, 20),
                        fg= WINDOW_COLOR,
                        activeforeground= WINDOW_COLOR,
                        width=15,
                        pady=20,
                        command=OnIncreaseClick)

reset_button = Button(main_window,
                      text="RESET",
                      font = (MAIN_FONT, 20),
                      fg= WINDOW_COLOR,
                      activeforeground=WINDOW_COLOR,
                      width=15,
                      pady=20,
                      command=ResetCount)

save_button = Button(main_window,
                      text="SAVE",
                      font = (MAIN_FONT, 20),
                      fg= WINDOW_COLOR,
                      activeforeground=WINDOW_COLOR,
                      width=15,
                      pady=20,
                      command=SaveFile)

counter_label.pack()
counter_button.pack()
reset_button.pack()
save_button.pack()

main_window.protocol("WM_DELETE_WINDOW", AutoSaveFileOnExit)
main_window.mainloop()