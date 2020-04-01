import CaboCha

def neko_parse():
    with open("neko.txt") as data_file,\
        open("neko.txt.cabocha","a") as write_file:
        cabocha=CaboCha.Parser()
        for i in data_file:
            write_file.write(cabocha.parse(i).toString(CaboCha.FORMAT_LATTICE))

class Morph():
    def __init__(self,surface,base,pos,pos1):
        self.surface=surface
        self.base=base
        self.pos=pos
        self.pos1=pos1
    
    def __str__(self):
        return "surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]".format(self.surface,self.base,self.pos,self.pos1)


def neko_lines():
    with open("neko.txt.cabocha") as file_parsed:
        morphes=[]
        for line in file_parsed:
            if line=="EOS\n":
                yield morphes
                morphes=[]
            
            else:
                if line[0] == '*':
                    continue
                cols=line.split("\t")
                res_cols=cols[1].split(",")
                surface=cols[0]
                base=res_cols[6]
                pos=res_cols[0]
                pos1=res_cols[1]

                morphes.append(Morph(surface,base,pos,pos1))

 



neko_parse()
for num,i in enumerate(neko_lines()):
    
    if num==3:
        for j in i:
            print(j)