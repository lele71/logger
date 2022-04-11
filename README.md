**Class Logger**

Produce un file di log, nella posizione specificata in fase di istanza, nel formato:

aaaammgg-nome\_app.log, nome\_app è passato in fase di istanza tipicamente è il nome dell’applicazione che genera il log.

Di default logga qualsiasi messaggio, per filtrare i messaggi usare il metodo addFilter(), mentre per rimuovere filtri usare il metodo removeFilter().

**Istanza:**

logger(position, appName, level=’noset’)



**Livelli di log:**



|**Level**|**Numeric value**|
| :- | :- |
|CRITICAL|50|
|ERROR|40|
|WARNING|30|
|INFO|20|
|DEBUG|10|
|NOTSET|0|


***Metodi pubblici:***

- *bool log(level, msg, timestamp = ‘None’*):
  logga un messaggio **msg** a livello **level.** Level può essere indifferentemente un int che rappresenta il codice oppure una string con il livello (indifferente il maiuscolo o il minuscolo), qualsiasi altra cosa genera un errore ed un return False con messaggio “Level not correct”.**
  Se viene passato anche un timestamp questo sarà quello scritto nel file, altrimenti il timestamp verrà generato in fase di scrittura, attenzione se il messaggio di log per qualsiasi motivo non viene scritto immediatamente il timastamp dell’evento e quello riportato a log potrebbero essere differenti.
  Stringa prodotta:
  aaa-mm-gg hh:mm:ss.ms appName <level> msg
  Se level è presente in una chiamata di addFilter non verrà prodotto alcun log.
  Ritorna:
  True se tutto è andato a buon fine
  False se qualcosa è andato storto.
  Se ritorna false memorizza l’errore che può essere richiesto con getLastError()**

- *bool addFilter(filter[])*:
  aggiunge uno più filtri. Possono essere usati sia int che string anche misti. Se un int o una string non vengono riconosciuti si genera un return False con messaggio di errore “Level %s not correct”, i livelli corretti vengono invece applicati. La capitalizzazione non è rilevante.
  Usage:
  addFilter([20,10])
  addFilter([10, “info”])
  addFilter([“debug”,”INFO”])
  Le chiamate a log() con filter = a 20 o 10 non produrranno alcun log.
  Ritorna:
  True se tutto è andato a buon fine
  False se qualcosa è andato storto.
  Se ritorna false memorizza l’errore che può essere richiesto con getLastError()
- *bool removeFilter(filter[])*:
  rimuove uno o più filtri. Possono essere usati sia int che string anche misti. Se un int o una string non vengono riconosciuti si genera un return False con messaggio di errore “Level %s not correct”, i livelli corretti vengono invece applicati. La capitalizzazione non è rilevante.
  Usage:
  removeFilter([20,10])
  removeFilter([10, “info”])
  removeFilter([“debug”,”INFO”])
  Le chiamate a log() con filter = a 20 o 10 ora produrranno log sempre ammesso che fossero prima inserite in una chiamata di addFilter(), altrimenti tutto rimarrà invariato.
  Ritorna:
  True se tutto è andato a buon fine
  False se qualcosa è andato storto.
  Se ritorna false memorizza l’errore che può essere richiesto con getLastError()
- *str getLastError():*
  Restituisce l’ultimo errore occorso.
- *list getFilter():*
  Restituisce i filtri attivi come array.
- *dict getAvailableFilter():*
  Restituisce l’elenco dei filtri disponibili codificati

