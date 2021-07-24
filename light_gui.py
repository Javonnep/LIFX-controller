#!"which python"

from tkinter import *
import light_controller

# some important variables
scenes = light_controller.show_scenes()
window = Tk(className="lights!")
var = StringVar()
x = IntVar()
height = 100 + len(light_controller.show_scenes()) * 40
window.geometry("300x{}".format(height))


def activate():
    """
    this function is a helper to call some other important functions involved in changing between different scenes.
    """
    num = int(var.get())
    return light_controller.activate_scene(light_controller.show_scene_id(scenes[num]))


onbutton = Radiobutton(window,
                       text="Turn on",  # adds text to radio buttons
                       value=-25,
                       padx=2,  # adds padding on x-axis
                       pady=5,
                       font=("ZenLoop", 20),
                       compound='right',  # adds image & text (left-side)
                       indicatoron=0,  # eliminate circle indicators
                       command=lambda: light_controller.on()

                       )
onbutton.pack(anchor=CENTER)

for index in range(len(scenes)):
    scenebutton = Radiobutton(window,
                              text=scenes[index],
                              variable=var,
                              value=index,
                              padx=2,
                              pady=5,
                              font=("ZenLoop", 20),
                              indicatoron=0,
                              command=activate

                              )
    scenebutton.pack(anchor=CENTER)

offbutton = Radiobutton(window,
                        text="Turn off",
                        value=-2,
                        padx=2,
                        pady=5,
                        background=None,
                        font=("ZenLoop", 20),
                        indicatoron=0,
                        command=lambda: light_controller.off()
                        )
offbutton.pack(anchor=CENTER)

window.mainloop()
