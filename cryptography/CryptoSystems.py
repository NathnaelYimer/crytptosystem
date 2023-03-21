"""
CryptSystem Implementation
"""

import random
"""
Affine Cipher: 

Theorem: a has a multiplicative inverse modulo n if and only if gcd(a,n) = 1

"""

class Affine:

    def encrypt(message,key):

        if Affine.getGcd(key[0],26) != 1:
            return "error, they the value of the first key and 26 have to relatively prime"
        message.lower() 

        """
        the above code makes it a little difficult to understand the encrypted code for example "I" and "a" can be guessed if 
        they are left as they are from the rule of grammar.(and easier to implement)
        
        """""


        encryptedMessage =""
        for charachter in message:
            if charachter.isalpha():#checking if the character is in the alphabet
                Rep = ord(charachter) - 97 # -97 to convert the number in the range between 0-25
                encChar = ((Rep * key[0] + key[1]) % 26) + 97
                encryptedMessage = encryptedMessage + chr(encChar)
            else:
                encryptedMessage = encryptedMessage + charachter

        return encryptedMessage

                    
    def decrypt(message,key):
        message.lower() # same reason as the line in the encrypt method
        invKey = Affine.getInverseMod(key[0])
        decryptedMessage =""
        for charachter in message:
            if charachter.isalpha():
                hexRep = ord(charachter) - 97
                decChar = (invKey*(hexRep-key[1])% 26) + 97
                decryptedMessage = decryptedMessage + chr(decChar)
            else:
                decryptedMessage = decryptedMessage + charachter
        
        return decryptedMessage
                
        

    def getGcd(divdend,divisor): 

        """"
        the code still works even if we put the largest number first,
        because it swaps them after first recursion call
        
        """
        remainder = divdend % divisor
        if remainder == 0:
            return divisor
        else:
            return Affine.getGcd(divisor,remainder)
    
    def getInverseMod(a,mod=26): 
        #this funcion uses pow ,a builtin function inside the maths module, and calcualte the inverse by using Fermat's little theorem
        if Affine.getGcd(a,mod) != 1: # this has been checked in encrypt method but just incase
            return "error"
        return pow(a,-1,mod)


"""

Example Code: 
x = Affine.encrypt("i am a robot",[3,5])
Affine.decrypt("d fp f evivk",[3,5])



"""


"""
Next: Transpostion Cipher there are a lot of variation of Transpotion cipher, the one implemented down below is called
"""
    

class Transpositon:

     

    def encrypt(message,key):
        blockedMessage = Transpositon.block(message,key) #calls the fucntion block to separate the message into blocks
        encryptedBlock = Transpositon.shuffleBlock(blockedMessage,key)
        encryptedMessage =""
        for word in encryptedBlock:
            encryptedMessage +=word
        return encryptedMessage
    
    def decrypt(message,key):
        blockedMessage = Transpositon.block(message,key)
        decryptedBlock = Transpositon.reshuffleBlock(blockedMessage,key)
        decryptedMessage =""
        for word in decryptedBlock:
            decryptedMessage += word
        return decryptedMessage

    def block(message,key):
        message=message.replace(" ","")
        if len(message) % len(key) != 0:
            message= message +"*"*(len(key) - (len(message) % len(key))) 
        block = []
        for i in range(int(len(message) / len(key))):
            block.append(message[:len(key)])
            message = message[len(key):]
        return block

    def shuffleBlock(blocked,key):
        shuffledBlock = []
        for word in blocked:
            tempConta = [None] * len(word)
            for i in range(len(key)):
                tempConta[key[i]-1] = word[i]
            
            tempWord = ""
            for j in tempConta:
                tempWord += j
            shuffledBlock.append(tempWord)


        return shuffledBlock

    def reshuffleBlock(shuffledBlock,key):
        reshuffledBlock = []
        for word in shuffledBlock:
            tempConta = [None] * len(word)
            for i in range(len(key)):
                tempConta[i] = word[key[i]-1]
            
            tempWord = ""
            for j in tempConta:
                tempWord += j
            reshuffledBlock.append(tempWord)
        return reshuffledBlock


"""
Example code:
x= Transpotion.encrypt("pirate attack",[3,2,1,4])
Transpostion.decrypt(x,[3,2,1,4])

"""

"""

Lastly: RSA


"""
class RSA:

    def getInverseMod(a,mod):#the same one as in the Affine class
        if RSA.getGcd(a,mod) != 1:
            return "inverse can't be found"
        else:
            return pow(a,-1,mod)

    def getGcd(divdend,divisor):#the same one as in the affine class
        remainder = divdend % divisor
        if remainder == 0:
            return divisor
        else:
            return RSA.getGcd(divisor,remainder)
    
    def isPrime(number):
        if number > 1:
            for i in range(2, int(number ** 0.5)): 
                """
                 From our class discussion: we need to check upto it's square root only, 
                 other factors are a multiple the one below the square root and itself 

                """
                if(number%i) == 0:
                    return False
            else:
                return True
        
        else:
            return True
    

    def generateKey(P,Q):

        #Rules to generate key: P and Q can't be equal, they have to be both prime

        if P == Q: 
            return "they can't be the same"
        if not(RSA.isPrime(P) and RSA.isPrime(Q)):
            return "both of them have to be prime"
        
        n = P * Q
        phi = (P-1) * (Q-1)
        e = random.randrange(1,phi)
        """ 
        since the value of e and phi have to be relatively prime, this will generate random numbers until it finds that number 

        """
        while RSA.getGcd(e,phi) != 1:
            e =random.randrange(1,phi)
        
        d = RSA.getInverseMod(e,phi)
        publickey = [e,n]
        privateKey = [d,n]

        return publickey,privateKey


    def encrypt(message,publicKey): # the public key have in the format of [e,n]

        encryptedMessage = [(ord(char) ** publicKey[0])%publicKey[1] for char in message] #calculate the encryped message using the formula
        return encryptedMessage
    
    def decrypt(message,privateKey):

        decryptedMessage1 = [chr((char**privateKey[0]) % privateKey[1]) for char in message] # decrypting using the formula
        decryptedMessage = ""
        for character in decryptedMessage1: 
            decryptedMessage += character
        
        return decryptedMessage


        
"""
Example:

publicKey,privateKey = RSA.generateKey(19,23)

enc= RSA.encrypt("I am a robot",publicKey)
print(enc)
print(RSA.decrypt(enc,privateKey))

for decrypting the key has to be the one generated by the function
"""


def main():
    message = input("Enter the message to be decrypted: ")
    print("Choose a CryptoSystem(a number asscociated):\n1:Affine Cipher\n2:Transpositon\n3:RSA\n")
    cryptWay = input()
    if cryptWay == "1" or cryptWay.lower =="affine": #some people might not read the instruction
        encMessage = Affine.encrypt(message,[3,5])
        print("The Message encrypted in Affine Cipher is ",encMessage)
        print("The Message decrypted back: ", Affine.decrypt(encMessage,[3,5]))
    elif cryptWay == "2" or cryptWay.lower == "transpositon":
        encMessage = Transpositon.encrypt(message,[3,2,1,4])
        print("The Message encrypted in Transpositon Cipher is ",encMessage)
        print("The Message decrypted back: ", Transpositon.decrypt(encMessage,[3,2,1,4]))
    elif cryptWay == "3" or cryptWay.lower=="rsa":
        publicKey,privateKey = RSA.generateKey(19,23)
        encMessage= RSA.encrypt(message,publicKey)
        print("The Message encrypted in RSA is", encMessage)
        print("The Message decrypted back: ",RSA.decrypt(encMessage,privateKey))


if __name__ == '__main__':
    print("\nWelcome to CryptoSystems \n" +"*" *30)
    main()
    quit = input("Do you want to quit? y/n: ").lower()
    while quit == "n":
        main()
        quit=input("Do you want to quit? y/n: ").lower











    

        





        









        



