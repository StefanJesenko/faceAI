Stefan Jesenko

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|03.05.2024| 0.0.1   |Ich habe mich dazu entschieden eine KI zu machen die gesichter erkennen kann.|
|10.05.2024| 0.0.1   |Ich habe mich heute darüber Informiert welche Architektur ich für meine KI benutzen möchte.|
|17.05.2024| 0.1.0   |Ich habe mir heute ein Datenset herausgesucht das ich benutzen kann um die KI zu trainieren.|
|24.05.2024| 0.3.0   |Heute habe ich ein Skript geschrieben das das Datenset in train test und valid aufteilt und die Daten normalisiert.|
|31.05.2024| 0.7.0   |Heute habe ich das Model programmiert und ein trainings skript gemacht.|
|07.06.2024| 1.0.0  |Ein Prototyp der KI ist jetzt fertig, es müsste aber weiter trainiert werden damit es gesichter erkennen kann. Aktuell kann die KI nur erkennen ob etwas nah an der Kamera ist oder nicht.|


## 1 Informieren

### 1.1 Ihr Projekt

In diesem Projekt mache ich ein CNN das durch die Kamera Gesichter erkennen kann.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ  | Beschreibung                       |
| ---- | --------------- | ---- | ---------------------------------- |
| 1    |Muss|Funktional|Als Benutzer möchte ich, dass das Programm erkennt ob es ein Gesicht sieht oder nicht, damit ich dieses Model sinnvoll verwenden kann.|
| 2    |Muss|Funktional|Als Benutzer möchte ich, dass das Programm mir sagt wie sicher es ist das das ein Gesicht ist, damit ich sehe wie sicher sich die KI ist.|
| 3    |Muss|Funktional|Als Programmierer möchte ich, dass das Programm auf die Kamera zugreift, damit ich ein Medium habe über das die KI die Gesichter sehen kann.|
| 4    |Muss|Rand|Als Programmierer möchte ich, dass das celebA Dataset verwendet wird, weil dieses eine grosse Auswahl an Bildern bitet.|
| 5    |Muss|Rand|Als Programmierer möchte ich, dass das die LeNet Architektur verwendet wird, weil diese Simpel und einfach ist.|
| 6    |Kann|Rand|Als Programmierer möchte ich, dass das Model mit Pytorch funktioniert, weil ich dieses schon am besten kenne.|



### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  |Programm wird gestartet|Kein Gesicht vor der Kamera|"Kein Gesicht erkannt"|
| 1.2  |Programm wird gestartet|Gesicht vor der Kamera|"Gesicht wurde erkannt"|
| 2.1  |Programm wird gestartet|Gesicht ist gut erkennbar im Sichtfeld der Kamera.|Prozentzahl über 90|
| 2.2  |Programm wird gestartet|Gesicht ist schlecht oder garnicht erkennbar im Sichtfeld der Kamera.|tiefere Prozentzahl unter 50|
| 3.1  |Programm wird gestartet| - |Kamera wird verwendet|
| 4.1  |Model wird trainiert| - |Daten stammen aus dem CelebA Dataset.|
| 5.1  | - | - |Das Model basiert auf der LeNet CNN Architektur.|
| 6.1  | - | - |Das Model funktioniert mit Pytorch.|


## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 4.A  |17.05.2024|Stefan Jesenko|Dataset wird bereitgestellt.|60min|
| 6.A  |17.05.2024|Stefan Jesenko|Die nötigen Pytorch Bibliotheken werden heruntergeladen.|45min|
| 3.A  |24.05.2024|Stefan Jesenko|Wenn das Script verwendet wird wird die Kamera geöffnet.|45min|
| 3.B  |24.05.2024|Stefan Jesenko|Die Kamera wird in einem Fenster auf dem Bildschirm angezeigt.|45min|
| 5.A  |24.05.2024|Stefan Jesenko|Die Architektur wird nach LeNet geplant und umgesetzt|90min|
| 1.A  |31.05.2024|Stefan Jesenko|Das Model wird trainiert und getestet.|45min|
| 1.B  |31.05.2024|Stefan Jesenko|Das beste Model kann die Kamera verwenden und ein Gesicht erkennen.|45min|
| 2.A  |31.05.2024|Stefan Jesenko|Es wird angezeigt wie sicher sich das Model in seiner entscheidung ist.|45min|



## 3 Entscheiden

Ich habe mich dazu entschieden das CelebA Dataset zu benutzen, weil es sehr umfangreich ist und ich werde eine LeNet Architektur verwenden, weil diese nicht so komplex ist.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 4.A  |17.05.2024|Stefan Jesenko|45min|70min|
| 6.A  |17.05.2024|Stefan Jesenko|45min|60min|
| 3.A  |24.05.2024|Stefan Jesenko|45min|60min|
| 3.B  |24.05.2024|Stefan Jesenko|45min|50min|
| 5.A  |31.05.2024|Stefan Jesenko|90min|100min|
| 1.A  |31.05.2024|Stefan Jesenko|45min|180min|
| 1.B  |31.05.2024|Stefan Jesenko|45min|90min|
| 2.A  |31.05.2024|Stefan Jesenko|45min|45min|



## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |14.06.2024|OK|Stefan Jesenko|
| 1.2  |14.06.2024|OK|Stefan Jesenko|
| 2.1  |14.06.2024|OK|Stefan Jesenko|
| 2.2  |14.06.2024|OK|Stefan Jesenko|
| 3.1  |14.06.2024|OK|Stefan Jesenko|
| 4.1  |14.06.2024|OK|Stefan Jesenko|
| 5.1  |14.06.2024|NOK|Stefan Jesenko|
| 6.1  |14.06.2024|OK|Stefan Jesenko|

Das Produkt ist eigentlich Funktional, das Model braucht nur mehr Training um die Genauigkeit zu erhöhen. (Ich konnte das Model nicht auf Github hochladen, weil die Datei zu gross ist.)





## 6 Auswerten

[Link zum Portfolio](https://portfolio.bbbaden.ch/view/view.php?t=e08dcc560e1886c8e92d)
