#Problem 1


    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        new_dict = {}
        temp1 = string.ascii_lowercase
        temp2 = string.ascii_uppercase
        for letters in temp1:
            if ord(letters) - 97 + shift < 26:
                new_dict[letters] = chr(ord(letters) + shift)
            else:
                new_dict[letters] = chr(ord(letters) + shift - 26)

        for letters in temp2:
            if ord(letters) - 65 + shift <= 26:
                new_dict[letters] = chr(ord(letters) + shift)
            else:
                new_dict[letters] = chr(ord(letters) + shift - 26)

        return(new_dict)
        
   def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new_string=""
        for i in range(len(self.message_text)):
            new_string[i]= self.build_shift_dict(shift)[self.message_text[i]]

        return new_string
      
 #problem 2       
 
 class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''

        Message.__init__(self, text)
        self.shift=shift
        self.valid_words=self.get_valid_words()
        self.message_text=text
        self.encrypting_dict=self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)



    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        copied=self.encrypting_dict.copy()
        return copied


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing

        '''

        self.shift=shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)



#Problem 3

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = self.get_valid_words()

     def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        counter=0
        best_story=[]
        best_shift=0
        temp=counter
        for shift_val in range (1, 26):

            new_story=self.apply_shift(shift_val).split()
            counter=0
            for test_word in new_story:
                if is_word(self.valid_words, test_word):
                    counter+=1

            if counter>temp:
                temp=counter
                best_shift=shift_val
                best_story=self.apply_shift(shift_val)

        return (counter, best_story)

    
    
    
#Problem 4


x=get_story_string()
decryption=CiphertextMessage(x)
print(decryption.decrypt_message())
 
