from pexpect import pxssh
from common.commondefs import false
from common.commondefs import none
import marshal

class ImportTest:
    def __init__(self):
        print("imported successfully") # Log success
class Bot:
    # init class instance
    def __init__(self, host, user, password):
        self.host = host # Fetch and store host reference
        self.user = user # Fetch and store username
        self.password = password # Fetch and store user password
        self.session = self.ssh() # Fetch and store ssh session

    # secure shell into bot
    def ssh(self):
        try:
            bot = pxssh.pxssh() # Open ssh client instance
            bot.login(self.host, self.user, self.password, auto_prompt_reset=false) # Login to ssh terminal
            return bot
        except Exception as e: # Account for exceptions
            print('connection failure') # Handle exception
            print(e) # Print exception

    # sending a command to the client
    def send_command(self, command):
        if self.session is none:
            self.session = self.ssh()
        self.session.sendline(command)
        self.session.prompt() # match the prompt
        return self.session.before # everything before the prompt

    # dump to bytes
    def to_bytes(self):
        return marshal.dumps(self)

    # dump params to bytes
    def params_to_bytes(self):
        arr = [self.host, self.user, self.password]
        return marshal.dumps(arr)

    # read from bytes
    def from_bytes(self, b):
        self = marshal.loads(b)

def byte_params_to_bot(b):
    arrVal = marshal.loads(b)
    return Bot(arrVal[0], arrVal[1], arrVal[2])