print ('Pukul berapa pak Amir sampai di kota C?')
jarakAkeB = 125
jarakBkeC = 256
kecAkeB = 62
kecBkeC = 70
waktuJamAkeB = jarakAkeB // kecAkeB
waktuMenitAkeB = round ((jarakAkeB % kecAkeB)/kecAkeB*60)
waktuJamBkeC = jarakBkeC // kecBkeC
waktuMenitBkeC = round ((jarakBkeC % kecBkeC)/kecBkeC*60)
jamBerangkat = 6
menitBerangkat = 0
istirahatdiB = 45
waktuJamAsampaiC = (jamBerangkat + waktuJamAkeB + waktuJamBkeC)
waktuMenitAsampaiC = (menitBerangkat + waktuMenitAkeB + istirahatdiB + waktuMenitBkeC)
if (waktuMenitAsampaiC >= 60):
    waktuJamAsampaiC += 1
    waktuMenitAsampaiC -= 60
print("Jadi, Pak Amir sampai di kota C pada pukul %d.%d" % (waktuJamAsampaiC,waktuMenitAsampaiC))
