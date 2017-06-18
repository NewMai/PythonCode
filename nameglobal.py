from idaapi import *

def leakchars(funcs):
    res = ''
    for f in funcs:
        res += chr(GetOperandValue(f, 1))
    return res

def flagbyaddrs(start, end):
    return leakchars(Functions(start, end + 1))

def getmain(start):
    for head in Heads(start, SegEnd(start)):
        mnem = GetMnem(head)
        op0 = GetOpnd(head, 0)
        if mnem == 'lea' and op0 == 'rdi':
            return GetOperandValue(head, 1)

def getcheck(main):
    for head in Heads(main, SegEnd(main)):
        mnem = GetMnem(head)
        op0 = GetOpnd(head, 0)
        if mnem == 'call':
            if op0.find('sub') != -1:
                return GetOperandValue(head, 0)
    
def getfuncs():
    start = BeginEA()
    main = getmain(start)
    check = getcheck(main)
    res = []
    for head in Heads(check, FindFuncEnd(check)):
        mnem = GetMnem(head)
        op0 = GetOpnd(head, 0)
        if mnem == 'call':
            res.append(GetOperandValue(head, 0))
    
    return res[0:-1]
strs = []
addrs = []
for head in Heads(0x00000000004032C0, FindFuncEnd(0x00000000004032C0)):
    #print hex(head)
    e = GetMnem(head)

    if e.find('lea') !=-1:
        strs.append('ptr' + GetOpnd(head, 1))
    elif e.find('mov') != -1:
        op1 = GetOpnd(head, 1)
        #print op1
        if op1.find('rax') != -1:
            addrs.append(GetOperandValue(head, 0))
count = 0
for addr in addrs:
    MakeName(addr, strs[count])
    count += 1

    
print 'strs is '
print strs
print 'addrs is '
print addrs
print len(strs) == len(addrs)

        
    