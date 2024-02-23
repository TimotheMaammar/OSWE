## Partie 5 : ManageEngine Applications Manager AMUserResourcesSyncServlet SQL Injection RCE

### Recherche de toutes les affectations à une variable nommée "query" (expression régulière)

    ^.*?query.*?select.*?

### Fonctions HTTP à chercher dans un servlet Java

    doGet
    doPost
    doPut
    doDelete
    doCopy
    doOptions


## Partie 9 : openITCOCKPIT XSS and OS Command Injection - Blackbox

### Recherche de points d'entrée pour une XSS DOM-Based

    grep -ir "document.write" ./ --include *.html

