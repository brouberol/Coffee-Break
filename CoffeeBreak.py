#!/usr/bin/python2.6

import gtk
import os.path
from sys import argv
from math import ceil
import gobject
import pynotify
from time import time
gtk.gdk.threads_init()


class CoffeeBreak:

    def __init__(self):
        self.icon = gtk.status_icon_new_from_file(os.path.realpath(self.get_dir() + "Coffee_icon_small.png"))
        self.icon.set_tooltip("You still have {0} of coffee break.\n Enjoy!".format(self.calc_time(BREAK_TIME)))
        self.icon.connect('activate',self.icon_click) # icon_click changes status 
        self.icon.set_visible(True)

        path = self.get_dir() + "Coffee_icon.png"
        n = pynotify.Notification ("Coffee Break","Enjoy your {0} of coffee break !".format(self.calc_time(BREAK_TIME)),path)
        n.show()            

        self.menu = gtk.Menu()
        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        self.menuItem.connect('activate', self.quit_cb, self.icon)
        self.menu.append(self.menuItem)
	
	self.icon.connect('popup-menu', self.popup_menu_cb, self.menu)

	self.status = "coffee"
        self.deltaT = 10
        self.start_working_time = time()

    def popup_menu_cb(self, widget, button, time, data = None):
        if button == 3: #right click
            if data:
                data.show_all()
                data.popup(None, None, gtk.status_icon_position_menu,3, time, self.icon)

    def quit_cb(self, widget, data = None):
        gtk.main_quit()

    def get_dir(self):
        return os.path.dirname(os.path.realpath(__file__)) + os.path.sep
    
    def calc_time(self, t, Break = None):
        if Break == None:
            minutes = ceil(t/60)
            if minutes > 1 :
                return "{0} minutes".format(int(abs(minutes)))
            else:
                return "{0} minute".format(int(abs(minutes)))
        else:
            minutes = ceil((Break - t)/60)
            if minutes > 1 :
                return "{0} minutes".format(int(abs(minutes)))
            else:
                return "{0} minute".format(int(abs(minutes)))

    def set_status(self, status):
        if status == "coffee":
            self.icon.set_from_file(self.get_dir() + "Coffee_icon_small.png")
        else:
            self.icon.set_from_file(self.get_dir() + "Coffee_icon_grey_small.png")
        self.status = status
       
    def icon_click(self, dummy):
        if self.status == "coffee":
            self.set_status("working")
	    self.icon.set_tooltip("Coffee break : procrastination fighter")
        else:
            self.set_status("coffee")
 	    self.start_working_time = time()
 
    def update(self):
        """This method is called everytime after deltaT seconds"""
        delta = time() - self.start_working_time
        if self.status == "working":
            pass
        else:
            self.icon.set_tooltip("You still have {0} of coffee break.\n Enjoy them !".format(self.calc_time(delta, BREAK_TIME)))
            if self.status == "coffee": 
                if delta > BREAK_TIME:
                    self.set_status("working")
                    self.start_working_time = time()
                    self.back_to_work()
                    self.icon.set_tooltip("CoffeeBreak : procrastination fighter")
 
        source_id = gobject.timeout_add(self.deltaT*1000, self.update) #*1000 : valeur compensatoire de ralentissement

    def back_to_work(self):
        initCaps()
        iconpath = self.get_dir() + "Coffee_icon.png"
        soundpath = self.get_dir() + "alert.ogg"
        n = pynotify.Notification ("CoffeeBreak","Your coffee break is over. Back to work =)", iconpath)   
        n.show() 
        os.system("paplay {0}".format(soundpath))     

    def main(self):
        source_id = gobject.timeout_add(self.deltaT, self.update)
        gtk.main()


 
capabilities = {'actions':             False,
                'body':                False,
                'body-hyperlinks':     False,
                'body-images':         False,
                'body-markup':         False,
                'icon-multi':          False,
                'icon-static':         False,
                'sound':               False,
                'image/svg+xml':       False,
                'private-synchronous': False,
                'append':              False,
                'private-icon-only':   False}

def initCaps ():
        caps = pynotify.get_server_caps ()
        if caps is None:
                print "Failed to receive server caps."
                sys.exit (1)

        for cap in caps:
                capabilities[cap] = True


#MAIN()
if __name__ == "__main__":

    # If no time limite given as argument, standard duration = 10 min
    if len(argv) > 1:
        BREAK_TIME = int(argv[1])*60
    else:
        BREAK_TIME = 60*0.2 # 10 minutes

    app = CoffeeBreak()
    app.main()

