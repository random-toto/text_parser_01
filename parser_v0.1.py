
import os
import re
os.chdir('/tmp/6')
l = os.listdir()
#~ print(l)


tlt = re.compile('Tout le Temps')
mat = re.compile('Matin')
jr = re.compile('Journée')
nt = re.compile('Nuit')
ent = re.compile('^[0-9]+')

toutletemps = False
matin = False
jour = False
nuit = False


print("""
def Route3(periode_heure = 0):
    '''
    '''
    a = valid_heure(periode_heure)
    b = valid_periode(periode_heure)
    if a:
        c = heure2periode(a)
    if b:
        c = b
    r = rangeRandom()""")
n = []
m = dict()
with open('route.txt', 'r') as fr:
    for i, line in enumerate(fr):
        if tlt.findall(line):
            toutletemps = True
            matin = False
            jour = False
            nuit = False
            m = dict()
        
        if mat.findall(line):
            toutletemps = False
            matin = True
            jour = False
            nuit = False
            n .append(m)
            m = dict()

        if jr.findall(line):
            toutletemps = False
            matin = False
            jour = True
            nuit = False
            n.append(m)
            m = dict()

        if nt.findall(line):
            toutletemps = False
            matin = False
            jour = False
            nuit = True
            n.append(m)
            m = dict()
            
        if ent.findall(line):
            m[line.split(';')[1]] = line.split(';')[2] + ':' + line.split(';')[3].strip()
    n.append(m)


#~ print(n)
#~ print()
#~ print()
#~ print()
o = []
for dic in n:
    p = dict()
    for ele in dic:
        uni = dic[ele].split(':')
        q = []
        for i in uni:
            if '%' in i:
                q.append(float(i.replace('%', '').strip())/100)
                p[ele] = q
                
            else:
                q.append(i)
                #~ print(i)
                p[ele] = q
    #~ print(p)
    o.append(p)

#~ o.append(q)
#~ print(o)


#~ """    
somme = 0
if len(o) == 4:
    for i in o[0]:
        somme += (o[0][i][1])
    for i, dic in enumerate(o):
        t = []
        for j, ele in enumerate(dic):
            t.append(ele)
            valeur = 0
            for k in t:
                valeur += dic[k][1]
            if not i:
                #~ print(ele, dic[ele], sep = ':')
                #~ print("        if r < ", dic[ele][1],':' , sep = '')
                print("    if r < ", round(valeur, 2),':' , sep = '')
                print("        return ('", ele.strip(), "', ", sep = '', end = '')
                if '-' in dic[ele][0]:
                    print("randInt(", dic[ele][0].strip().split('-')[0], ',', dic[ele][0].strip().split('-')[1], '))', sep = '')
                else:
                    print(dic[ele][0].strip(), ")", sep = '')
            if i:
                if not j:
                    if i == 1:
                        print("    if c == 'matin':")
                    if i == 2:
                        print("    if c == 'jour':")
                    if i == 3:
                        print("    if c == 'nuit':")
                valeur += somme
                #~ somme = 0
                print("        if r <= ", round(valeur, 2),':' , sep = '')
                print("            return ('", ele.strip(), "', ", sep = '', end = '')
                if '-' in dic[ele][0]:
                    print("randInt(", dic[ele][0].strip().split('-')[0], ',', dic[ele][0].strip().split('-')[1], '))', sep = '')
                else:
                    print(dic[ele][0].strip(), ")", sep = '')                
        #~ print()

elif len(o) == 3:
    print()
#"""


