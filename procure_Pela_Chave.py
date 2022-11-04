def procure_pela_chave(caixa_princiipal):
    
    for item in caixa:
        if item.e_uma_caxa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print "achei uma chave!"