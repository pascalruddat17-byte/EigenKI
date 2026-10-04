# EigenKI – eigenes kleines Sprachmodell

Kein fremdes Sprachmodell, keine API und keine Antwort-Suchtabelle: Ein selbst implementiertes Zeichen-RNN wurde aus zufälligen Gewichten auf 30 selbst geschriebenen deutschen Beispieldialogen trainiert. Jeder Ausgabebuchstabe wird aus den gelernten Gewichten berechnet und zufällig aus wahrscheinlichen Zeichen gewählt. Trainingsbeispiele sind Lernmaterial; das Modell kann sie dennoch auswendig lernen.

## Benutzen
`index.html` öffnen. Die trainierten Gewichte sind integriert. Keine Installation für den Chat nötig. Für eine Online-Version dieselbe Datei als `index.html` auf einem statischen Webhost, beispielsweise GitHub Pages, veröffentlichen. Die Berechnung findet im Browser statt, auch wenn die Seite online gehostet wird. Es ist keine serverseitige Online-KI.

## Grenzen
Dies ist ein sehr kleines Lernexperiment mit 48 versteckten Einheiten. Es hat kein breites Weltwissen, keine Websuche und kann neue Fragen nicht zuverlässig beantworten. Auch einfache Nachrichten können unsinnige Antworten erzeugen. Unterschiedliche Antworten sind kein Nachweis für Verständnis. Trainingserfolg auf den Beispielen ist keine allgemeine Gesprächsqualität.

## Erneut trainieren
Python 3 und NumPy installieren: `python -m pip install numpy`

1. Eigene erlaubte Texte in `training.txt` ergänzen. Format beibehalten: `Mensch: ...`, `KI: ...`, danach `§` als Dialoggrenze.
2. `python train.py --steps 2500`
3. `python package.py`

`train.py` enthält Vorwärtsberechnung, Backpropagation through time und Adagrad. `model.json` enthält die tatsächlichen trainierten Gewichte. `template.html` enthält die Browser-Inferenz. Nach erneutem Training erzeugt package.py die Datei EigenKI.html; diese als index.html veröffentlichen. Mehr Trainingsschritte allein lösen die Grenzen des sehr kleinen Datensatzes nicht.

## Stand
Keine fremden vortrainierten Gewichte. Keine vorgegebenen Antworten als Fallback; technische Fehlermeldungen stehen separat in der Oberfläche. Der Gesprächsverlauf liegt nur im Arbeitsspeicher und wird beim Neuladen verworfen.
