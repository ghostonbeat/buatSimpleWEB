from os import *
from touch import *
from shutil import *

path = getcwd()
folder = ['/proyekweb', '/proyekweb/component', '/proyekweb/content']
file =  [folder[0]+'/index.php', folder[1]+'/Header.html', folder[1]+'/Footer.html', folder[2]+'/style.sass', folder[2]+'/javascript.js']
pohon = 'tree '+path+folder[0]

def buatFolder():
    for i in range(len(folder)):
        mkdir(path+folder[i])

def buatKomponen():
    for i in range(len(file)):
        touch(path+file[i])

def hapusLama():
    rmtree(path+folder[0])

def main():
    buatFolder()
    buatKomponen()
    system(pohon)
    """Catatan : Pastikan sistem Linux Distro memiliki program Tree"""
    print("paket proyek berhasil dibuat!! selamat mengerjakan!!")

if __name__ == '__main__':
    try:
        main()
    except:
        hapusLama()
        print("reset proyek")
        main()
