#!/usr/bin/env python# -*- coding: utf-8 -*-import importlibimport sysimport types# import pyctest#http://python3-cookbook.readthedocs.io/zh_CN/latest/c10/p11_load_modules_from_remote_machine_by_hooks.htmldef dynamic_import(module):    return importlib.import_module(module)def load(fname = 'pyctest'):    fpth = fname + '.py'    f = open(fpth,'r')    pycode = f.read()    f.close()    m = types.ModuleType('pyctest')    print pycode    pyctest = {}    exec pycode in m.__dict__    m = sys.modules.setdefault('pyctest', m)    # print pyctest    # print sys.modules['pyctest'].__name__    # # print sys.modules['pyctest'].__file__    # print sys.modules['pyctest'].__package__    return mdef main():    # print sys.modules    # print sys.modules.keys()        # print sys.modules['pyctest'].__path__    # print sys.modules['pyctest'].__loader__    m = load()    print(m.pyctest())    print(m.xxx)if __name__ == '__main__':    main()