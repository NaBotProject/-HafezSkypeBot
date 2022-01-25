from skpy import SkypeEventLoop,SkypeNewMessageEvent
from getpass import getpass
import csv
import random
import threading

class MySkype(SkypeEventLoop):
    def onEvent(self, event):            
        for request in self.contacts.requests():
                request.accept()
        if isinstance(event, SkypeNewMessageEvent) \
          and not event.msg.userId == self.userId :
            for request in self.contacts.requests():
                request.accept()
            chosen_row = random.choice(data)
            msg = "amirrezashams.ir" if event.msg.content == "about" else chosen_row[1]+"\n\n\n"+chosen_row[2]
            msg = msg.replace("_x000D_","")
            event.msg.chat.sendMsg(msg)


if __name__ == "__main__":
    fileName = ('/path/to/data.csv')
    with open(fileName) as f:
        reader = csv.reader(f)
        data = list(reader)
    sk = MySkype("username@example.org", "password", autoAck=True)
    print("Ready!")
    sk.loop()
