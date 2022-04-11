from logger import Logger

def main():
    myLog = Logger("etc/", "test")
    
    '''
    # Test getLastError
    print("Ultimo errore: %s"%myLog.getLastError())
    print("----------------------------------------------------------------")
    # Test getLevel
    print("Livelli filtro: %s"%str(myLog.getFilter()))
    print("----------------------------------------------------------------")
    # Test getAvailableFilter
    print("Filtri disponibiuli: %s"%str(myLog.getAvailableFilter()))
    print("----------------------------------------------------------------")
    '''
    '''
    # Test addFilter
    print("Aggiungo filtri corretti:\n")
    if myLog.addFilter([20,"WARNING"]):
        print("Filtri aggiunti correttamente")
        print("Livelli filtro: %s"%str(myLog.getFilter()))
        print("----------------------------------------------------------------")
    else:
        print("Errore aggiunta filtri")
        print(myLog.getLastError())
        print("----------------------------------------------------------------")
    
    # Test delete filters
    if myLog.removeFilter([20, "WARNING"]):
        print("Filtri rimossi correttamente")
        print("Livelli filtro: %s"%str(myLog.getFilter()))
        print("----------------------------------------------------------------")
    else:
        print("Errore rimozione filtri")
        print(myLog.getLastError())
        print("Livelli filtro: %s"%str(myLog.getFilter()))
        print("----------------------------------------------------------------")
    

    print("Aggiungo filtri errati interi:\n")
    if myLog.addFilter([20,0,25,[12]]):
        print("Filtri aggiunti correttamente")
        print("Livelli filtro: %s"%str(myLog.getFilter()))
        print("----------------------------------------------------------------")
    else:
        print("Errore aggiunta filtri")
        print(myLog.getLastError())
        print("----------------------------------------------------------------")
    print("Loggo ok:\n")
    if myLog.log(20,"messaggio"):
        print("log ok")
        print("----------------------------------------------------------------")
    else:
        print("Errore log")
        print(myLog.getLastError())
        print("----------------------------------------------------------------")
    print("Loggo errore:\n")
    '''
    #myLog.addFilter([20])
    if myLog.log("ERROR","messaggio", istanza="pippo"):
        myLog.log(100,"log ok")
        #print("log ok")
        #print("----------------------------------------------------------------")
    else:
        myLog.log(100,"Errore log")
        myLog.log(100,myLog.getLastError())
        #print("Errore log")
        #print(myLog.getLastError())
        #print("----------------------------------------------------------------")


if __name__ == '__main__':
    main()