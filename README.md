Stefan Jesenko

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|03.05.2024| 0.0.1   |Ich habe mich dazu entschieden eine KI zu machen die gesichter erkennen kann.|
|       | ...     |                                                              |
|       | 1.0.0   |                                                              |

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




### 1.4 Diagramme

✍️ Hier können Sie PAPs, Use Case- und Gantt-Diagramme oder Ähnliches einfügen.

## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 4.A  |17.05.2024|Stefan Jesenko|Dataset wird bereitgestellt.|45min|
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
| 1.A  |       |           |               |                   |
| ...  |       |           |               |                   |

✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |

✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

### 5.2 Exploratives Testen

| BR-№ | Ausgangslage | Eingabe | Erwartete Ausgabe | Tatsächliche Ausgabe |
| ---- | ------------ | ------- | ----------------- | -------------------- |
| I    |              |         |                   |                      |
| ...  |              |         |                   |                      |

✍️ Verwenden Sie römische Ziffern für Ihre Bug Reports, also I, II, III, IV etc.

## 6 Auswerten

✍️ Fügen Sie hier eine Verknüpfung zu Ihrem Lern-Bericht ein.
