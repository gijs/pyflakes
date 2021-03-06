# (c) 2005 Divmod, Inc.  See LICENSE file for details

class Message(object):
    message = ''
    message_args = ()

    def __init__(self, filename, lineno, col = None, level = 'W', message_args = None):
        self.filename = filename
        self.lineno = lineno
        self.col = col
        self.level = level
        if message_args:
           self.message_args = message_args 

    def __str__(self):
        if self.col is not None:
            return '%s:%s(%d): [%s] %s' % (self.filename, self.lineno, self.col, self.level, self.message % self.message_args)
        else:
            return '%s:%s: [%s] %s' % (self.filename, self.lineno, self.level, self.message % self.message_args)


class UnusedImport(Message):
    message = '%r imported but unused'

    def __init__(self, filename, lineno, name):
        Message.__init__(self, filename, lineno, message_args=(name,))

class RedefinedWhileUnused(Message):
    message = 'redefinition of unused %r from line %r'

    def __init__(self, filename, lineno, col, name, orig_lineno):
        Message.__init__(self, filename, lineno, message_args=(name, orig_lineno))

class ImportShadowedByLoopVar(Message):
    message = 'import %r from line %r shadowed by loop variable'

    def __init__(self, filename, lineno, col, name, orig_lineno):
        Message.__init__(self, filename, lineno, message_args=(name, orig_lineno))

class ImportStarUsed(Message):
    message = "'from %s import *' used; unable to detect undefined names"

    def __init__(self, filename, lineno, col, modname):
        Message.__init__(self, filename, lineno, col, message_args=(modname,))

class UndefinedName(Message):
    message = 'undefined name %r'

    def __init__(self, filename, lineno, col, name):
        Message.__init__(self, filename, lineno, col, 'E', (name,))

class UndefinedLocal(Message):
    message = "local variable %r (defined in enclosing scope on line %r) referenced before assignment"

    def __init__(self, filename, lineno, col, name, orig_lineno, orig_col):
        Message.__init__(self, filename, lineno, message_args=(name, orig_lineno))


class DuplicateArgument(Message):
    message = 'duplicate argument %r in function definition'

    def __init__(self, filename, lineno, col, name):
        Message.__init__(self, filename, lineno, col, message_args=(name,))


class RedefinedFunction(Message):
    message = 'redefinition of function %r from line %r'

    def __init__(self, filename, lineno, name, orig_lineno):
        Message.__init__(self, filename, lineno, message_args=(name, orig_lineno))


class LateFutureImport(Message):
    message = 'future import(s) %r after other statements'

    def __init__(self, filename, lineno, col, names):
        Message.__init__(self, filename, lineno, message_args=(names,))
