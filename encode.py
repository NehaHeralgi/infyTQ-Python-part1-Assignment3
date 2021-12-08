'''

Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. 
Repetition of character has to be replaced by storing the length of that run.
Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

'''
#lex_auth_012693816331657216161

def encode(message):
    enc=''
    prev=''
    c=1 
    
    if not message:
        return ''
        
    for char in message:
        if char!=prev:
            if prev:
                enc=enc+str(c)+prev
            c=1 
            prev=char
            
        else:
            c=c+1 
    
    else:
        enc=enc+str(c)+prev
    return enc
    

#Provide different values for message and test your program
encoded_message=encode("AAAABBBBCCCCCCCC")
print(encoded_message)