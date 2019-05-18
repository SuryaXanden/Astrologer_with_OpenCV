import random, re, cv2, pyttsx3
from glob import glob
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from time import sleep
import numpy as np

engine = pyttsx3.init()

good = [
            "You are very kind hearted person.",
            "You have good sense of humour.",
            "You are strong than you think.",
            "Your family would not be the same without you.",
            "You never give up.",
            "Never compare yourself with others.",
            "You will marry two woman in your lifetime.",
            "Never be afraid to be yourself.",
            "You are very brave.",
            "You love to go out with friends.",
            "You love to be a single.",
            "Your health life is good.",
            "You love to stand on your own toes.",
            "You love to dance during the rain.",
            "You like to smile without reason.",
            "You are a happy go person.",
            "Your love life is good.",
            "You always say the truth.",
            "You love reading.",
            "You never share your personal problem.",
            "You don't share your secrets.",
            "You are romantic.",
            "You love watching cartoons.",
            "You love going out for long drive.",
            "You love your pets.",
            "You are scared of dogs.",
            "You love your parents.",
            "You have a fear of insects.",
            "You are dare devil.",
            "You are a sleeping beauty.",
            "You are a foodie.",
            "You are a cosmoholic.",
            "You make a good leader.",
            "You are very humble.",
            "You like sports.",
            "You are very photogenic.",
            "You are very beautiful.",
            "You love to dance.",
            "You like your friends.",
            "You love watching action movies.",
            "You love watching romantic movies.",
            "You like to go shopping.",
            "You love to be in field of agriculture.",
            "You love reading novels.",
            "You love to play games in computer.",
            "You love vintage bikes and cars.",
            "You love to plant the flowers.",
            "You love editing music.",
            "You are were creative.",
            "You are hyper active.",
            "You are smart.",
            "You are a self-motivated worker.",
            "You are an inspiration for others.",
            "You are a successful person.",
            "You look energetic.",
            "Your smile makes everyone happy.",
            "Your beauty has no boundaries.",
            "You are marvelous.",
            "You are an interesting person.",
            "You have a great smile.",
            "You always think positive.",
            "You have great ideas.",
            "Your words are meaningful.",
            "You make every one proud.",
            "You are a good story teller.",
            "Every one love your creativity.",
            "You spread love every where.",
            "You love children.",
            "You respect elder’s.",
            "You love watching animated movies.",
            "You have a helping hand.",
            "You will be a millionaire.",
            "You are an open minded person.",
            "You have a positive attitude.",
            "You like to edit photos.",
            "You are very innovative.",
            "You have beautiful eyes.",
            "You are good at studies.",
            "You are very determined.",
            "You are very enthusiastic.",
            "You are very impulsive.",
            "You like individual sports.",
            "You are very imaginative.",
            "You are witty.",
            "You are cheerful.",
            "You are very motivational.",
            "You are a genius.",
            "You have a good voice.",
            "Your confidence is refreshing.",
            "Your great at being creative.",
            "Your hair is nice.",
            "You’re so impressive.",
            "You’re so attractive.",
            "You love to grow beard."
]

bad = [
        "You depend on your parents money.",
        "You drink a lot of coffee.",
        "You are moody.",
        "You bluff too much.",
        "You do not like reading.",
        "You don't  like to help others.",
        "You don't like to hanging around friends.",
        "You don't hide secrets.",
        "You are a lazy goose.",
        "You don't like taking a bath.",
        "You have breakfast without brushing your teeth.",
        "You waste your time.",
        "You do lame jokes.",
        "You are very careless.",
        "Your pocket is always empty.",
        "You drink too much.",
        "You are stone hearted person.",
        "You don't like to go shopping.",
        "You don't like the pets.",
        "Your dressing sense is not too good.",
        "You don't like traveling.",
        "You don't like to play the games in computer.",
        "You don't like sports.",
        "You don't like flowers.",
        "You don't like to plant.",
        "You talk rubbish.",
        "You are too harsh.",
        "You are bad at writing.",
        "You don't like to watch cartoon.",
        "You act like a fool."
]

def predict(good, bad):
    Results = []
    
    while len(Results) <= 2:
        found = random.choice(good)
        if found not in Results:
            Results.append(found)

    while len(Results) <= 3:
        found = random.choice(bad)
        if found not in Results:
            Results.append(found)
    return Results

def speak(string):
    engine.say(string)
    engine.runAndWait()
        
char_list = [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "J",
                "K",
                "L",
                "M",
                "N",
                "P",
                "R",
                "S",
                "T",
                "U",
                "V"
]

hell_heaven = [
    "Heaven",
    "Hell"
]

list_of_files = glob( "Characters/*.*" )

found = 0
def read_face():    
    faceCascade = cv2.CascadeClassifier( "haarcascade_frontalface_default.xml" )

    def see( image ):
        global found
        gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
        faces = faceCascade.detectMultiScale( gray, 2 )
        background = Image.fromarray( image )
        for ( x, y, w, h ) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow('Recognized face', image)
            cv2.waitKey(0)
            found = 1
            break

    cap = cv2.VideoCapture( cv2.CAP_ANY )

    while True:
        ret, frame = cap.read( )
        if ret == True:
            see( cv2.flip(frame,1) )
            if cv2.waitKey(1) == 27 or found:
                break

    cap.release( )
    cv2.destroyAllWindows( )

try:
    while True:
        speak("Press 0 to scan a face")
        print("\n"*50)
        try:
            ip = int(input("Press 0 to scan a face: "))
            if ip == 0:
                read_face()
                print("\n"*50)
                speak("Enter your name")
                name = input( "Enter your name: " )
                print("\n"*50)
                name = re.sub( "[^a-zA-Z ]", "", name )
                if name:
                    get_predictions = predict(good,bad)
                    print("Hi {}\n".format(name))
                    speak("Hi, {}\n".format(name))
                            
                    print("Predictions about you:\n")
                    speak("Predictions about you:\n")
                    for i in get_predictions:
                        print(i)
                        speak(i)

                    crush = random.choice(char_list)
                    print("\nYour crush's name starts with the letter: {}".format(crush))
                    speak("\nYour crush's name starts with the letter {}".format(crush))

                    hell_or_heaven = random.choice(hell_heaven)
                    print("\nYou might go to: {}".format(hell_or_heaven) )
                    speak("\nYou might go to {}".format(hell_or_heaven) )

                    file = random.choice(list_of_files)
                    char = re.sub("\..+","",file)
                    char = re.sub(r".+\\","",char)

                    print("\nWhich character suits you: {}".format(char))
                    speak("\nWhich character suits you, {}".format(char))

                    img = mpimg.imread(file)
                    plt.figure(num = char)
                    imgplot = plt.imshow(img)
                    plt.show()
                    sleep(1)
                    speak("Press a key to continue")
                    x = input("Press a key to continue...")
                else:
                    speak("Name invalid!")
            else:
                speak("Try again!")
        except Exception as e:
            print(e)
except Exception as e:
    print(e)