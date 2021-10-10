print ('Liter bensin yang diperlukan Pak Budi')
def bbm (jarakAkeC,penggunaanbbm):
    return jarakAkeC/penggunaanbbm
jarakAkeC = float(input('jarak dari A ke C : '))
penggunaanbbm = float(input('Rata rata penggunaan bbm perliter : '))
total_kebutuhan = bbm (jarakAkeC,penggunaanbbm)
print ('Total kebutuhan bensin yang diperlukan Pak Budi adalah sebanyak :', total_kebutuhan , 'liter')
