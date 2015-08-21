#import pyperclip

#cipher_text = pyperclip.paste()
cipher_text = raw_input('encypted string...')
l = len(cipher_text)
de1,de2,de = '','',''
i,a = 0,0

if l % 2 == 0 :
    de1 = cipher_text[0:(l/2)]
    de2 = cipher_text[(l/2):(l-1)]

else:
    de1 = cipher_text[0:(l/2)+1]
    de2 = cipher_text[(l/2):(l-1)]

if len(de1) > len(de2) :
    while i in range(0,len(de1)) :
        de = de + de1[a]
        de = de + de2[a]

    de = de + de1[(len(de1) - 1)]

elif len(de1) == len(de2) :
    while a in range(0,len(de1)):
        de = de + de1[a]
        de = de + de2[a]

print 'the decrypted string is', de
#pyperclip.copy (de)


