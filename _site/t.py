#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
import json
filetoread='cat.json'
def load_existed(filetoread):

    try:
        data=json.loads(open(filetoread).read())
        return data

    except ValueError:
        print 'data  loading error'

    cat_data=load_existed(filetoread)

def walk_dict(d,mess,ln,new_dict,crumbs):
    inter=1
    lc=list(mess)
    last_crumb=crumbs.split( )

    for k,v in sorted(d.items(),key=lambda x: x[0]):
        if mess=='':
            mess=str(inter)
            lc=list(mess)
            last_crumb=crumbs.split( )
        if isinstance(v, dict) :
            ln=len(v)
            lc[len(lc)-1]=str(inter)
            mess="".join(lc)
            crumbs=" ".join(last_crumb)
            if len(crumbs.split( ))>0:
                crumbs=crumbs+" "+k
            else:
                crumbs=k
            #print mess,'-->',k,">"
            new_dict[mess]=crumbs
            mess=mess+'.1'
            walk_dict(v,mess,ln,new_dict,crumbs)
        else:
            if ln>0:
                ln=ln-1
                lc[len(lc)-1]=str(inter)
                mess="".join(lc)
                crumbs=" ".join(last_crumb)
                crumbs=crumbs+" "+k+" "+v
            #print  mess,'-->',"%s -> %s" % (k, v)
            new_dict[mess]=crumbs
        inter=inter+1
    return new_dict

if __name__ == '__main__':
    cat_data = load_existed(filetoread)
    new_data=walk_dict(cat_data,"",0,{},'')
    print "-"*30
    #print new_data
    for v in sorted(new_data):
        print v, new_data[v]
