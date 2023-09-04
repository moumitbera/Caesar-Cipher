import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):

    FinalOutput=[]
    if direction == "decode":
        shift = shift*-1
    
    for i in text:

        if i in alphabet: 
            index = alphabet.index(i)

            finalIndex = index+shift
            
            if(finalIndex<0):
                finalIndex = finalIndex+25
            
            elif(finalIndex>25):
                finalIndex = finalIndex-25
            
            shiftLetter = alphabet[finalIndex]
            FinalOutput.append(shiftLetter)
        else:
            FinalOutput.append(i)

    print(f"The {direction}d text is {''.join(FinalOutput)}")
        
goAgain = True
while goAgain: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%len(alphabet)
    caesar(text=text, shift=shift, direction=direction)
    askGoAgain = input("Do you want to run the code again?\n").lower()
    if(askGoAgain=="no"):
        goAgain = False
    print()
print("Thanks for using our service. Have a good day!")