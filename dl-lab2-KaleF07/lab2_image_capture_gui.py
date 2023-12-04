# Adapted from code found in this thread:
# https://stackoverflow.com/questions/32342935/using-opencv-with-tkinter

from PIL import Image, ImageTk, ImageOps
import tkinter as tk
from tkinter import ttk
import argparse
import cv2
import os
import re

class ImageCaptureFrame(ttk.Frame):
    def __init__(self, parent=None, output_path = "./"):
        """ Initialize frame which uses OpenCV + Tkinter. 
            The frame:
            - Uses OpenCV video capture and periodically captures an image
              and show it in Tkinter
            - A save button allows saving the current image to output_path.
            - Consecutive numbering is used, starting at 00000000.jpg.
            - Checks if output_path exists, creates folder if not.
            - Checks if images are already present and continues numbergin.
            
            attributes:
                vs (cv2 VideoSource): webcam to capture images from
                output_path (str): folder to save images to.
                count (int): number used to create the next filename.
                current_image (PIL Image): current image displayed
                btn (ttk Button): press to save image
                panel (ttk Label): to display image in frame
        """
        super().__init__(parent)
        self.pack()
        
        # 0 is your default video camera
        self.vs = cv2.VideoCapture(0) 
        
        # Creates directory if not already existing.
        if (os.path.exists(output_path) != True):
            self.create_directory(output_path)
        self.output_path = output_path
        
        # Get current largest file number already in folder
        self.count = self.get_current_count(output_path) + 1
        print("[INFO] current count {}".format(self.count))
        
        # Prepare an attribute for the image
        self.current_image = None 
        
        # Custom method to execute when window is closed.
        parent.protocol('WM_DELETE_WINDOW', self.destructor)

         # Button to save current image to file
        btn = ttk.Button(self, text="Save", command=self.save_image)
        btn.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Label to display image
        self.panel = ttk.Label(self)  
        self.panel.pack(padx=10, pady=10)

        # start the display image loop
        self.video_loop()

    def get_current_count(self, folder):
        """Checks for existing images and returns current file number.
        
            folder(str): directory to search for existing images
            
            return: (int) the current highest number in jpg filename
                          or -1 if no jpg files present.
        """
        imgs = []
        valid_images = [".jpg"]
        for i in os.listdir(folder):
            ext = os.path.splitext(i)[1]
            if ext.lower() not in valid_images:
                continue
            imgs.append(Image.open(os.path.join(folder,i)))
        
        return len(imgs)
        
    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter 
            
            The image is processed using PIL: 
            - crop left and right to make image smaller
            - mirror 
            - convert to Tkinter image
            
            Uses after() to call itself again after 30 msec.
        
        """
        # read frame from video stream
        ok, frame = self.vs.read()  
        # frame captured without any errors
        if ok:  
            # convert colors from BGR (opencv) to RGB (PIL)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
            # convert image for PIL
            self.current_image = Image.fromarray(cv2image)  
            # camera is wide: crop 200 from left and right
            self.current_image = ImageOps.crop(self.current_image, (200,0,200,0)) 
            # mirror, easier to locate objects
            self.current_image = ImageOps.mirror(self.current_image) 
            # convert image for tkinterfor display
            imgtk = ImageTk.PhotoImage(image=self.current_image) 
            # anchor imgtk so it does not get deleted by garbage-collector
            self.panel.imgtk = imgtk  
             # show the image
            self.panel.config(image=imgtk)
        # do this again after 30 msec
        self.after(30, self.video_loop) 

    def save_image(self):
        """ Save current image to the file 
        
        Current image is saved to output_path using
        consecutive numbering in 
        zero-filled, eight-number format, e.g. 00000000.jpg.
        
        """
        # Create filename for image
        current = '00000000'
        self.count = self.get_current_count(self.output_path) + 1
        new = current[len(str(self.count)):] + str(self.count)
        filename = new + '.jpg'
        
        path = os.path.join(self.output_path, filename)
        print('new save:', path)
        ret, frame = self.vs.read()
        if ret:
            saved = cv2.imwrite(path, frame)
            print('save successful.')

    def create_directory(self, folder):
        """ Creates a directory if not found

        Uses the output path given to create a new
        directory if it does not already exist.

        """
        try:
            os.makedirs(folder) # creates new directory
            print("Successfully created the directory %s" % folder)
        except OSError:
            print("Creation of the directory %s failed." % folder)
            return -1
            

    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing...")
        self.vs.release()  # release web camera
        cv2.destroyAllWindows()  # close OpenCV windows
        self.master.destroy() # close the Tk window

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", default="./",
    help="path to output directory to store images (default: current folder")
args = parser.parse_args()

# start the app
print("[INFO] starting...")
gui = tk.Tk() 
gui.title("Image Capture")  
ImageCaptureFrame(gui, args.output)
gui.mainloop()
