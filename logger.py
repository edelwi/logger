# -*- coding: utf-8 -*-
# Logger v.0.05m
# Evgeniy Semenov 12 12 2016

import time
#import codecs
class logger:
    def __init__(self, filename,store_level=0,debug_level=0):
        """
            store_level: 0 - No store messages (default)
                         1 - Faults
                         2 - Errors and Faults
                         3 - Warnings, Errors and Faults
                         4 - Messages, Warnings, Errors and Faults
                         5 - All
            debug_level: 0 - No out (default)
                         1 - DEBUG_1 (d) out only
                         2 - DEBUG_1 and DEBUG_2 (d and b) out
                         3 - Out all debug type (d,b and g) messages
        """
        self._file=open(filename,'a')
        self._Filename=filename
        self._n=0
        self._e=0
        self._w=0
        self._m=0
        self._f=0
        self._d=0
        self._b=0
        self._g=0
        self._store_level=store_level
        self._store=[]
        self._debug=debug_level
    def msg(self, msgtype, text, plusstdout=0):
        '''
        msgtype: 'e' - Add [Error] to message
                 'w' - Add [Warning] to message
                 'f' - Add [Fault] to message
                 'm' - Add [Message] to message
                 'n' - Add some string
        plusstdout: 1 - Add formated message to stdout
                    0 - Out to logfile only
        '''
        datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()) )
        if msgtype=='e':
            message='[Error]:   '+datetime+' | '+text
            self._e+=1
        elif msgtype=='w':
            message='[Warning]: '+datetime+' | '+text
            self._w+=1
        elif msgtype=='f':
            message='[Fault]:   '+datetime+' | '+text
            self._f+=1
        elif msgtype=='m':
            message='[Message]: '+datetime+' | '+text
            self._m+=1
        else:
            message=text
            self._n+=1

        if plusstdout:
            print message

        if self._store_level==1 and msgtype=='f':
            self._store.append(message)
        elif self._store_level==2 and (msgtype in ('f','e')):
            self._store.append(message)
        elif self._store_level==3 and (msgtype in ('f','e','w')):
            self._store.append(message)
        elif self._store_level==4 and (msgtype in ('f','e','w','m')):
            self._store.append(message)
        elif self._store_level==5:
            self._store.append(message)

        self._file.write(message+'\n')
        self._file.flush()
        m=message+'\n'
        return str(m)

    def dbg(self,msgtype, text, plusstdout=0):
        '''
        msgtype: 'd' - Add [DEBUG_1] to message
                 'b' - Add [DEBUG_2] to message
                 'g' - Add [DEBUG_3] to message
        plusstdout: 1 - Add formated message to stdout
                    0 - Out to logfile only
        '''
        if self._debug==0:
            return None
        datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()) )
        if msgtype=='d':
            message='[DEBUG_1]: '+datetime+' | '+text
            self._d+=1
        elif msgtype=='b':
            message='[DEBUG_2]: '+datetime+' | '+text
            self._b+=1
        elif msgtype=='g':
            message='[DEBUG_3]: '+datetime+' | '+text
            self._g+=1

        if self._debug==1 and msgtype=='d':
            self._file.write(message+'\n')
            self._file.flush()
            if plusstdout:
                print message
            m=message+'\n'
            return str(m)
        elif self._debug==2 and (msgtype in ('d','b')):
            self._file.write(message+'\n')
            self._file.flush()
            if plusstdout:
                print message
            m=message+'\n'
            return str(m)
        elif self._debug>=3 and (msgtype in ('d','b','g')):
            self._file.write(message+'\n')
            self._file.flush()
            if plusstdout:
                print message
            m=message+'\n'
            return str(m)

    def getlogs(self):
        return self._store;

    def __del__(self):
        self._file.close()
    def close(self):
	   self.__del__()
if __name__=='__main__':
    log=logger('test.log',store_level=0,debug_level=3)
    log.msg('n','=*='*20,1)
    log.msg('e','Some error message!',1)
    log.msg('w','Some warning message!',1)
    log.msg('f','Some fault message!',1)
    log.msg('m','Some message!',1)
    print log.msg('m','Some message!',0)
    print '-----------------------'
    print log.getlogs()
    log._debug=0
    log.dbg('d','Не должен ничего вывести',1)
    log._debug=1
    log.dbg('d','TEST1 debug D',1)
    log.dbg('b','TEST1 debug B',1)
    log.dbg('g','TEST1 debug G',1)
    log._debug=2
    log.dbg('d','TEST2 debug D',1)
    log.dbg('b','TEST2 debug B',1)
    log.dbg('g','TEST2 debug G',1)
    log._debug=3
    log.dbg('d','TEST3 debug D',1)
    log.dbg('b','TEST3 debug B',1)
    log.dbg('g','TEST3 debug G',1)

    log.close()


