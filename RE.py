import tkinter as tk
from tkinter import simpledialog
from tkinter.messagebox import askyesno, showinfo, showerror
from cryptography.fernet import Fernet
import pyperclip
import keyboard
import win10toast
def encrypt():
    data = pyperclip.paste().encode('utf-8')
    fern = Fernet(key)
    pyperclip.copy(fern.encrypt(data).decode('utf-8'))
    n=win10toast.ToastNotifier()
    n.show_toast(title="Encrypt and chat", msg="message encrypted..paste to send encrypted message")
def decrypt():
    try:
        data = pyperclip.paste().encode('utf-8')
        fer = Fernet(key)
        dec = str(fer.decrypt(data).decode('utf-8'))
    except Exception as e:
        showerror('An error occurred', f"On decrypting data, the following exception occured (probably the key or the message to be decrypted is invalid): \n {e}")
        dec = "ERROR: <an error occured while decrypting this message>"
    pyperclip.copy(dec)
    n=win10toast.ToastNotifier()
    n.show_toast(title="Encrypt and chat", msg=f"decrypted message reads: {dec}")
    showinfo('decrypted message', f"deccrypted message: \n {dec}")
root = tk.Tk()
root.title("Encrypt and chat")
l1 = tk.Label(root, text="Encrypt and chat")
l1.pack()
showinfo("How to use?", """
Instructions on how to use the program:\n
Key is copied to your clipboard after you either ask for a new key or type the new key into dialog box.\n
To use the program. share the program with your friends and ask them to download and set it up. once thats done, run the program\n
this time when the dialog asks if u require a new key. select "yes" and then the new key will be copied to your clipboard.\n
share the new key with your friends over a secure channel\n
Once the deired recipient recieves the key, they have to run the program and select "no" at the prompt asking you "if u require a new key".\n
once they select "no" they will have to type in the key sent by you and finally run the program by clicking "ok".
 and then use the following steps to encrypt or decrypt.\n
to encrypt: select and copy (ctrl+c) the text to encrypt and press ctrl+e to encrypt.. press ctrl+V to paste the encrypted data\n
to decrypt: select and paste (ctrl+c) the text to decrypt and press ctrl+d to decrypt.. then press ctrl+v to see the decrypted text\n
decrypted text also appears on the notification shown after decyption\n""")
answer = askyesno("new key", "do you require a new key?")
if answer: key = Fernet.generate_key()
else:
    keystr = simpledialog.askstring('enter key', 'enter key')
    if keystr is not None: key = keystr.encode('utf-8')
    else: root.quit()
print(key)
pyperclip.copy(str(key.decode('utf-8')))
keyvar = tk.StringVar(root, "current key: "+str(key.decode('utf-8')))
l2 = tk.Label(root, textvariable=keyvar)
l2.pack()
keyboard.add_hotkey("ctrl+e", encrypt)
keyboard.add_hotkey("ctrl+d", decrypt)
root.mainloop()