import pyAesCrypt
import os

# descrypt function

def decryption(file, password):
    
    # buffer size
    buffer_size = 512 * 1024
    
    # call method descrypt
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    
    # show info about processing
    print("[File '" + str(os.path.splitext(file)[0]) + "' decryptes]")

    # delete origin file
    os.remove(file)

# folder scaning
def foldersScaning(dir, password):
    
    # check folders
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # if find file use function
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # if find folers scaning again
        else:
            foldersScaning(path, password)
            
password = input('Your password is: ')
foldersScaning(r"C:\Users\Карина\Desktop\test", password)