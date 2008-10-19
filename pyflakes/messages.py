class Message(object):
    message = ''
    message_args = ()

    def __init__(self, filename, lineno, col=None):
        self.filename = filename
        self.lineno = lineno
        self.col = col

    def __str__(self):
        return '%s:%s%s: %s' % (self.filename, self.lineno,
            ('(%d)' % self.col) if self.col is not None else '',
            self.message % self.message_args)

class UnusedImport(Message):
    message = '%r imported but unused'
    def __init__(self, filename, lineno, col, name):
        Message.__init__(self, filename, lineno, col)
        self.message_args = (name,)

class RedefinedWhileUnused(Message):
    message = 'redefinition of unused %r from line %r'
    def __init__(self, filename, lineno, name, orig_lineno):
        Message.__init__(self, filename, lineno)
        self.message_args = (name, orig_lineno)

class ImportShadowedByLoopVar(Message):
    message = 'import %r from line %r shadowed by loop variable'
    def __init__(self, filename, lineno, name, orig_lineno):
        Message.__init__(self, filename, lineno)
        self.message_args = (name, orig_lineno)

class ImportStarUsed(Message):
    message = "'from %s import *' used; unable to detect undefined names"
    def __init__(self, filename, lineno, modname):
        Message.__init__(self, filename, lineno)
        self.message_args = (modname,)

class UndefinedName(Message):
    message = 'undefined name %r'
    def __init__(self, filename, lineno, col, name):
        Message.__init__(self, filename, lineno, col)
        self.message_args = (name,)

class UndefinedLocal(Message):
    message = "local variable %r (defined in enclosing scope on line %r) referenced before assignment"
    def __init__(self, filename, lineno, col, name, orig_lineno):
        Message.__init__(self, filename, lineno, col)
        self.message_args = (name, orig_lineno)

class DuplicateArgument(Message):
    message = 'duplicate argument %r in function definition'
    def __init__(self, filename, lineno, col, name):
        Message.__init__(self, filename, lineno, col)
        self.message_args = (name,)

class RedefinedFunction(Message):
    message = 'redefinition of function %r from line %r'
    def __init__(self, filename, lineno, col, name, orig_lineno):
        Message.__init__(self, filename, lineno, col)
        self.message_args = (name, orig_lineno)

class LateFutureImport(Message):
    message = 'future import(s) %r after other statements'
    def __init__(self, filename, lineno, col, names):
        Message.__init__(self, filename, lineno, col)
        self.message_args = (names,)
