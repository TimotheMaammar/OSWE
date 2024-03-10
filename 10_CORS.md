## Header

Payload à tenter dans les requêtes HTTP pour vérifier si les CORS envoyés sont reflétés : 

    Origin: http://evil.com

## Javascript

Exemples en Javascript permettant de vérifier les CORS :

### GET 

     fetch("http://example.com")
           .then(function (response) {
            return response.text();
           })
           .then(function (text) {
            console.log(text);
           })

### POST 
    
     fetch("https://example.com",
           {
            method: 'post',
            headers: {
                "Content-type": "application/json;"
            }
           })
