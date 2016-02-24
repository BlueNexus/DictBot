import os
import config


class Bot:

    memory = {}
    commandlist = ["commands", "add", "remove", "show", "import", "export"]
    
    def __init__(self):
        newMemory = self.import(config.FILENAME)
        self.memory.update(newMemory)

    def handleCommands(self, cmd):
        if cmd == self.commandlist[0]:
            print(self.commandlist)
        elif cmd == self.commandlist[1]:
            ID = str(raw_input("Enter the identifier of the definition being added: "))
            defn = str(raw_input("Enter the definition of " + str(ID)))
            self.add(ID, defn)
        elif cmd == self.commandlist[2]:
            ID = str(raw_input("Enter the identifier of the definition being removed: "))
            self.remove(ID)
        elif cmd == self.commandlist[3]:
            ID = str(raw_input("Enter the identifier of the definition being shown: "))
            self.show(ID)
        elif cmd == self.commandlist[4]:
            new = self.import(config.FILENAME)
            self.memory.update(new)
        elif cmd == self.commandlist[5]:
            self.export(config.FILENAME)
        else:
            print("Unknown command")

    def add(self, ID, definition):
        self.memory[ID] = definition

    def remove(self, ID):
        if ID in self.memory:
            del self.memory[ID]
        else:
            print(str(ID) + " is not defined.")

    def show(self, ID):
        if ID in self.memory:
            print(self.memory.get(ID))
        else:
            print(str(ID) + " is not defined.")

    def import(self, fname):
        newMemory = {"ID": "Definition"}
        with open(fname, 'r') as f:
            for line in f:
                splitLine = line.split()
                newMemory[str(splitLine[0])] = ",".join(splitLine[1])
        return newMemory

    def export(self, fname):
        pairs = [(k, v) for (k, v) in self.memory.iteritems()]
        with open(fname, 'w+') as f:
            for p in pairs:
                q = str(p)
                q = q.translate(None, '()')
                f.write("%s\n" % q)

bot = Bot()
while True:
    command = str(raw_input("Enter a command: "))
    bot.handleCommands(command)
