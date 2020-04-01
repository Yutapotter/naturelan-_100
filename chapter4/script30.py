import MeCab


def parse_neko():
    with open("neko.txt") as data_file,\
        open("neko.txt.mecab","w") as out_file:
    
        mecab=MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))

def neko_lines():  
    with open("neko.txt.mecab") as file_parsed:
        lines=file_parsed.readlines()
        morphemes=[]
        for line in lines:
            try:
                cols=line.split("\t")
                
                arr=cols[1].split(",")
                surface=cols[0]
                base=arr[6]
                pos=arr[0]
                pos1=arr[1]
                morpheme={
                    "surface":surface,
                    "base":base,
                    "pos":pos,
                    "pos1":pos1
                }
                morphemes.append(morpheme)

            except IndexError:
                pass
        
        return morphemes


        
    
    
        

