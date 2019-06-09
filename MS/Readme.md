# Main Script
Cette partie du projet expose une api rest qui permet d'intéragire avec le périférique.

## API
### /

#### GET

return



### /param

#### GET 

​	-> querystring key

#### POST

​	-> querystring key  et  valeur



-> paramêtre:
t_before INT
t_after INT
-> à voir à quel point les types sont différents au moment de l'écriture dans le fichier



### /stream

​	-> query string : start / stop

-> adresse à laquel on peut récupérer le flux ( en stream )

-> une clé générée pour le chiffrement symétric du flux. -> 



### /record

-> param de temps avant

-> param de temps après




## Configuration File
Un fichier va permettre de stocker diverse variable qui peuvent être consultée par les scripts du périphérique et être modifiée par le Backend à travers le endpoint `/config`