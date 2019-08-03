#-- include('examples/showgrabfullscreen.py') --#
import pyscreenshot as ImageGrab

if __name__ == "__main__":
    # fullscreen
    vid_list = []
    for i in range(5):
        im=ImageGrab.grab()
        vid_list.append(im)
    for image in vid_list:
        image.show()
#-#
