pyflags - no-nonsense flagparsing  
==============================================  
Need to parse commandline flags or text commands?
Want to decide how to handle each flag or need to handle multiple args at once? 
Well look no further!  
Inspired by [go's flag](https://golang.org/pkg/flag/), an easy to use commandline parser  
  
Usage:
```python
from pyflags import Flags

f = Flags()
f.simple("-n", func = lambda args : int(args[0])) # convert the arg after the flag to int
f.flag("-datetime", argcount = 2, func = lambda args : dateutil.parser.parse("%s %s" %(args[0],args[1])) # returns the 2 consecutive args parsed as datetime
f.boolean("-bool") # returns true if in the given args, false if absent 
f.flag("--collect", argcount = 2) # returns the 2 consecutive args as a list

vals = f.parse_all(args) #returns a dict of all the parse args, None if absent for non-boolean flags
#or parse sys.argv via f.parse_sysargs()

originals = f.original_args
leftovers = f.leftover_args

#use the stuff
```


  
  
TODO:  
- [ ] build parser for positionals
- assign the values to variables declared beforehand (goflag's default behaviour)
