import os
import touch
import shutil

path = './'
folder = ['proyekweb', 'proyekweb/component', 'proyekweb/content']
bahan =  [folder[0]+'/index.php', folder[1]+'/style.scss', folder[1]+'/javascript.js', folder[2]+'/Header.html', folder[2]+'/Footer.html', folder[2]+'/Main.php']
akar = path+folder[0]

def buatFolder():
    for i in range(len(folder)):
        os.mkdir(path+folder[i])

def buatKomponen():
    for i in range(len(bahan)):
        touch.touch(path+bahan[i])

def hapusLama():
    shutil.rmtree(path+folder[0])
    
def pohon():
    akr = []
    for root in os.walk(akar):  
        akr.append(root)

    print(" "+folder[0])
    for i in range(len(akr[0][1])):
        print("|")
        print("+--- "+akr[0][1][i])
        for j in range(len(akr[1+i][2])):
            print("|   |")
            print("|   +--- "+str(akr[1+i][2][j]))
    for i in range(len(akr[0][2])):
        print("|")
        print("+--- "+akr[0][2][i])

def main():
    buatFolder()
    buatKomponen()
    pohon()
    print("paket proyek berhasil dibuat!! selamat mengerjakan!!")

if __name__ == '__main__':
    try:
        main()
    except:
        hapusLama()
        print("reset proyek")
        main()
