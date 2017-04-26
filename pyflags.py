import traceback
import sys

class Flags():
    
    def __init__(self):
        self.flags = []
        self.original_args = []
        self.leftover_args = []
    
    def parse_sysargs(self):
        return self.parse_all(sys.argv[1:])
       
    def parse_all(self,args):
        #TODO: maybe implement positionals
        self.orig_args = args.copy()
        vals = {}
        
        for flag in self.flags:
            present = flag.parse(args)
            #either the value or None
            vals[flag.flag] = flag.val

        
        self.leftover_args = args
        
        return vals
    
    
    """ 
    sets up a customizable flagparser  
    :param flag -> the flag to be parse i.e. "-r", "--help"
    :param argcount -> optional the number of args after the flag to be read
    0 for simple boolean flags(True if present, False else)
    :param func -> optional function to be called with the args,
    if None the arguments are returned as list
    """
    def flag(self, flag, argcount = 0, func = None):
        if func is None:
            func = Flag.return_unparsed
            
        
        newflag = Flag(flag, argcount, func)
        self.flags.append(newflag)
        
    def boolean(self, flag):
        newflag = Flag(flag, argcount=Flag.BOOLEAN, func = Flag.return_unparsed)
        self.flags.append(newflag)
    
    def simple(self, flag, func = None):
        if func is None:
            func = Flag.return_unparsed
        
        newflag = Flag(flag, argcount = 1, func = func)
        self.flags.append(newflag)
        
class Flag():
    BOOLEAN = 0
        
    def __init__(self, flag, argcount, func):
        self.flag = flag
        self.argcount = argcount
        self.func = func
        
    def parse(self, args):
        self.val = None
        
        if self.flag in args:   
            index = args.index(self.flag)
            
            #boolean flags
            if self.argcount == Flag.BOOLEAN:
                self.val = True
                args.pop(index)
                return True
            
            #normal flags
            try:
                #slice the list so only the args after the flag are passed
                flagargs = args[index+1:index+1+self.argcount]
                self.val = self.func(flagargs)    
                
                for i in range(0, self.argcount+1):
                    args.pop(index)
                return True
                
            except:
                traceback.print_exc()
                return False      
            
        else:
            #boolean flags: absence means no:
            if self.argcount == Flag.BOOLEAN:
                self.val = False
            
            #normal flags + booleans
            return False
    
    @staticmethod
    def return_unparsed(args):
        return args
        
if __name__ == "__main__":
    pass
    