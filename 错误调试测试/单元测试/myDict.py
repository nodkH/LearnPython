#!/usr/bin/env python3
#2019年1月10日



class Dict(dict):
    def __init__(self, **kw):
        super.__init__(self,**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value




