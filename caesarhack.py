message = input('Enter encrypted message without nubers and specials symbols(english): ')
SYМBOLS = 'ABCDEFGHIJKLМNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 

for key in range(len(SYМBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYМBOLS:
            symbolIndex = SYМBOLS.find(symbol)  
            translatedIndex = symbolIndex - key 
            if translatedIndex < 0: 
                translatedIndex = translatedIndex + len(SYМBOLS)
            translated = translated + SYМBOLS[translatedIndex] 

        else : 
            translated = translated + symbol 
        print ('Key #%s: %s' % (key, translated))
input()
