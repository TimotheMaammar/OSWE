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

### Recherche du Javascript custom dans une page

    cat page.html | grep -E "script.*src" | grep -Ev "vendor|lib|plugin"

### Recherche de Websockets 

    grep -r  "send(" ./ --exclude="compressed*"
    grep -r  "setup(" ./ --exclude="compressed*"
