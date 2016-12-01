import Subclasses_Encryptie
import Encryptie
import time

def Encryption(matrix,key):
    ### Eerste fase
    i = 0
    Subclasses_Encryptie.AddRoundKey(matrix,key,i)

    ### Tweede fase
    for phase in range(9):
        i += 1
        Subclasses_Encryptie.SubBytes(matrix)
        Subclasses_Encryptie.ShiftRows(matrix)
        Subclasses_Encryptie.MixColumns(matrix)
        Subclasses_Encryptie.AddRoundKey(matrix,key,i)

    ### Derde fase
    i += 1
    Subclasses_Encryptie.SubBytes(matrix)
    Subclasses_Encryptie.ShiftRows(matrix)
    Subclasses_Encryptie.AddRoundKey(matrix,key,i)
    return matrix


final_result = Encryptie.final_result

def Ontcijfering(final_result):
    # Lees de EncryptieCode
    zero_state = Subclasses_Encryptie.ZereState

    # Sleutels
    Key = Subclasses_Encryptie.Key
    MAC = Subclasses_Encryptie.MAC

    # Aanmaken van de state
    number = final_result[1]
    state = Subclasses_Encryptie.MakeCTR(number)
    EncryptionState = Encryption(state,Key)


    ### DECRYPTIE ###

    ### Lees de tag
    EncryptedMessage = final_result[0]
    Tag2 = Encryption(zero_state,MAC)
    Subclasses_Encryptie.ImplementMessage(Tag2,EncryptedMessage)
    Encryption(Tag2,MAC)
    ### Lees de Message
    Subclasses_Encryptie.ImplementMessage(EncryptedMessage,EncryptionState)
    if final_result[2] == Tag2:
        return Subclasses_Encryptie.BlokToList(EncryptedMessage)

Message = Ontcijfering(final_result)
