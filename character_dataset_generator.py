from pyfiglet import Figlet
import random
import pandas as pd
f = Figlet(font="banner3-D")

#print(f.renderText('Character Recognition Dataset'))

###Generate the pattern and store into a 9x11 dimensional matrix###
def make_char(letter):
    character = f.renderText(letter).split('\n')

    for temp in range(0,len(character)):
        character[temp] = list(character[temp])
    character.pop()
    for temp1 in range(0,len(character)):
        for temp2 in range(0,len(character[temp1])):
            if(character[temp1][temp2] != "#"):
                character[temp1][temp2] = "."
    return(character)

###Render text for display###
def render_text(character):
    output = ["" for i in range(len(character))];
    for temp1 in range(0,len(character)):
        for temp2 in range(0,len(character[temp1])):
            output[temp1] = output[temp1]+character[temp1][temp2]
        print(output[temp1])
    return(output)

###Make distortions###

#Make one distortion
def distort_text_once(d1_character):
    distort_output_once = d1_character
    random_X = random.randint(1,(len(d1_character)-1))
    random_Y = random.randint(1,(len(d1_character[0])-1))
    for temp in range(0,random_X):
        distort_output_once[random_X][random_Y] = "$"
    return(distort_output_once)

#Make random number of distortions
def distort_text(d_character,distortion_scale):
    distort_output = d_character
    random_number = random.randint(1,distortion_scale)
    print("Approximate number of changes: ",random_number);
    for i in range(0,random_number):
        distort_output = distort_text_once(distort_output)
    return(distort_output)

#####################################################################################################################

###Main###

##Append to the following list the things that you want to get for its character recognition dataset.
letters = []
inp = input("Enter a character: ")
letters.append(inp)
for letter in letters:
    write_to_csv = []
    for i in range(50):
        character = make_char(letter);
        for j in range(1,(len(character))//2):
            character = make_char(letter);
            out_d = render_text(distort_text(character,(len(character)*j)))
            write_to_csv.append(distort_text(character,(len(character)*j)))

    df = pd.DataFrame(write_to_csv)
    df.to_csv(letter+".csv")

      


    
