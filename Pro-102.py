import cv2
import dropbox
import time
import random 

start_time=time.time()

def takesnapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on 
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name= "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("Snapshot Taken")    

    #release the camera
    videoCaptureObject.release()
    # close all the window that might be opened while the process
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token = "_o8QsfDI4G8AAAAAAAAAAXwiHe0PGxfdb6msNSYTAmiD0uPXhY1X3uhkIAi4UJYY"
    file=img_name
    file_from=file
    file_to="/test/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")   


def main():
    while(True):
        if((time.time()-start_time)>=60):
            name=takesnapshot()   
            upload_files(name)  


main()            
