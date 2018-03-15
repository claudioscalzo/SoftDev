import gdb
import sys

class MyGdbCommand(gdb.Command):

    def __init__(self):
        super().__init__("fpointers", gdb.COMMAND_USER)

    def invoke(self, argument, from_tty):
        args = gdb.string_to_argv(argument)
        address = int(args[0], 16)
        size = int(args[1], 16)

        # Debug
        # print("Argument is: " + str(address))
        # print("Size is: " + str(size))

        limit = address + size

        a = address
        while a <= limit:
            res = gdb.execute("x/1gx " + str(hex(a)), to_string=True)
            orig = int(res.split("\t")[0].replace(":",""), 16)
            dest = int(res.split("\t")[1], 16)
            
            # Debug
            # print() + " - " + str(hex(dest)))

            orighex = hex(orig)
            desthex = hex(dest)

            if dest >= address and dest <= limit:
                print("Pointer at " + str(orighex) + " --> " + str(desthex))

            a += 1

MyGdbCommand()
