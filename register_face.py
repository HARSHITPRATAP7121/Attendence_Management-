import cv2 
import pandas as pd   
import face_recognition as fr

def register(name):
    fname='features.csv'
    try:
        df =pd.read_csv(fname)
    except:
        df=pd.DataFrame({'name':[],'enc':[]})

    fd = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    counter=0
    vid =cv2.VideoCapture(0)
    names=[]
    feats=[]


    while True:
        ack,img = vid.read()
        if ack:
            faces=fd.detectMultiScale(img,1.2,10,minSize=(150,150))
            if len(faces) == 1:
                x,y,w,h=faces[0]
                face_img=img[y:y+h,x:x+w,:].copy()
                face_enc=fr.face_encodings(face_img) # extract the feature of image
                if len(face_enc) == 1:
                    counter += 1
                    names += [name]
                    feats += [face_enc[0].tolist()]
                    #f=pd.DataFrame({'name':[name],'enc':face_enc})
                    #df=pd.concat([df,f],axis=0,ignore_index=True)
                if counter == 20:
                    f=pd.DataFrame({'name':names,'enc':feats})
                    df=pd.concat([df,f],axis=0,ignore_index=True)
                    df.to_csv(fname)
                    break

            cv2.imshow('Preview',img)
            key=cv2.waitKey(1)
            if key == ord('x'):
                break 
    cv2.destroyAllWindows()
    vid.release()