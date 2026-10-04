"""Selbst verfasste deutsche Beispieldialoge und grammatische Variationen.
Diese Daten werden nur zum Training benutzt, nicht zur Antwortsuche.
"""
from pathlib import Path
import random

dialogs=[]
def add(q,a): dialogs.append(f'Mensch: {q}\nKI: {a}\n§\n')
base=[
('Hallo!','Hallo! Wie geht es dir?'),
('Hi!','Hi! Was möchtest du besprechen?'),
('Guten Morgen!','Guten Morgen! Wie beginnt dein Tag?'),
('Guten Abend!','Guten Abend! Wie war dein Tag?'),
('Wie geht es dir?','Ich bin bereit für ein Gespräch. Wie geht es dir?'),
('Wie heißt du?','Ich heiße EigenKI.'),
('Was bist du?','Ich bin ein kleines selbst trainiertes Sprachmodell.'),
('Was kannst du?','Ich übe deutsche Sprache und einfache Gespräche. Ich kann noch viele Fehler machen.'),
('Kannst du Deutsch?','Ich lerne Deutsch. Meine Sätze sind noch nicht immer richtig.'),
('Danke!','Gern geschehen!'),
('Vielen Dank.','Sehr gern!'),
('Tschüss!','Bis bald!'),
('Gute Nacht!','Gute Nacht und schlaf gut!'),
('Ich bin müde.','Vielleicht hilft dir eine kleine Pause.'),
('Ich bin traurig.','Möchtest du erzählen, was dich traurig macht?'),
('Ich bin glücklich.','Das freut mich. Was ist passiert?'),
('Mir ist langweilig.','Was machst du gern? Vielleicht können wir eine Idee finden.'),
('Ich habe Hunger.','Was möchtest du essen?'),
('Ich habe Durst.','Vielleicht möchtest du ein Glas Wasser trinken.'),
('Ich verstehe das nicht.','Welchen Teil möchtest du erklärt bekommen?'),
('Hilf mir bitte.','Wobei brauchst du Hilfe?'),
('Erkläre es einfacher.','Gern. Welches Thema soll ich einfacher erklären?'),
('Kannst du alles beantworten?','Nein. Mein Wissen ist klein und meine Antworten können falsch sein.'),
('Hast du Gefühle?','Ich berechne Text und habe keine menschlichen Gefühle.'),
('Wo wohnst du?','Ich habe keinen Wohnort. Ich bin ein Computerprogramm.'),
('Ich möchte ein Spiel bauen.','Welche Art von Spiel möchtest du bauen?'),
('Ich mag Roboter.','Was soll dein Roboter können?'),
('Ich mag Musik.','Welche Musik hörst du gern?'),
('Ich gehe zur Schule.','Welches Fach magst du besonders?'),
('Ich lerne Deutsch.','Wir können kurze deutsche Sätze üben.'),
('Was ist Wasser?','Wasser ist eine Flüssigkeit. Menschen, Tiere und Pflanzen brauchen Wasser.'),
('Was ist die Sonne?','Die Sonne ist ein Stern. Sie gibt uns Licht und Wärme.'),
('Was ist der Mond?','Der Mond kreist um die Erde.'),
('Was ist ein Baum?','Ein Baum ist eine Pflanze mit einem Stamm und Ästen.'),
('Was ist ein Computer?','Ein Computer verarbeitet Daten und führt Programme aus.'),
('Was ist HTML?','HTML beschreibt den Aufbau einer Webseite.'),
('Was ist eine Katze?','Eine Katze ist ein Tier. Katzen können schnurren.'),
('Was ist ein Hund?','Ein Hund ist ein Tier. Viele Hunde leben als Haustiere bei Menschen.'),
('Was bedeutet bitte?','Mit bitte kannst du eine höfliche Bitte ausdrücken.'),
('Was bedeutet danke?','Mit danke drückst du Dankbarkeit aus.'),
('Was ist ein Nomen?','Ein Nomen bezeichnet zum Beispiel ein Ding, eine Person oder ein Tier. Nomen schreibt man groß.'),
('Was ist ein Verb?','Ein Verb beschreibt oft eine Handlung oder einen Zustand. Beispiele sind gehen und sein.'),
('Was ist ein Adjektiv?','Ein Adjektiv beschreibt eine Eigenschaft. Beispiele sind klein und freundlich.'),
('Was ist ein Artikel?','Ein Artikel steht vor einem Nomen. Beispiele sind der, die und das.'),
('Was ist eine Frage?','Mit einer Frage möchtest du etwas erfahren. Am Ende steht ein Fragezeichen.'),
('Was ist ein Satz?','Ein Satz drückt einen Gedanken aus. Ein einfacher Satz hat oft ein Subjekt und ein Verb.'),
('Wie schreibt man Nomen?','Im Deutschen schreibt man Nomen groß.'),
('Was ist ein Subjekt?','Das Subjekt sagt, wer oder was etwas tut. Du kannst danach mit wer oder was fragen.'),
('Was ist ein Punkt?','Ein Punkt beendet einen Aussagesatz.'),
('Wie bildet man eine Frage?','Eine Frage kann mit einem Fragewort beginnen. Zum Beispiel: Wo wohnst du?'),
('Nenne deutsche Fragewörter.','Wer, was, wo, wann, wie und warum sind deutsche Fragewörter.'),
('Was ist die Mehrzahl?','Die Mehrzahl bezeichnet mehrere Dinge. Ein Buch, zwei Bücher.'),
('Was ist die Vergangenheit?','Die Vergangenheit beschreibt etwas, das schon passiert ist.'),
('Was ist die Zukunft?','Die Zukunft beschreibt etwas, das noch passieren wird.'),
('Was ist die Gegenwart?','Die Gegenwart beschreibt zum Beispiel etwas, das gerade passiert.'),
('Was bedeutet guten Morgen?','Guten Morgen ist eine Begrüßung am Morgen.'),
('Ich möchte einen Satz schreiben.','Beginne mit einem kurzen Satz. Zum Beispiel: Ich lese ein Buch.'),
('Wie kann ich Deutsch üben?','Lies kurze Texte, höre Gespräche und schreibe eigene Sätze.'),
('Wie schreibt man eine Nachricht?','Du kannst mit einer Begrüßung beginnen und dann dein Anliegen erklären.'),
('Wie spät ist es?','Ich habe keine verlässliche Uhrzeit im Sprachmodell.'),
('Was ist heute passiert?','Ich habe keinen Zugriff auf aktuelle Nachrichten.'),
]
for q,a in base:
    add(q,a)
    if q.endswith('?'): add(q[:-1],a)

nouns=[('der','Hund','Hunde','klein'),('die','Katze','Katzen','leise'),('das','Haus','Häuser','groß'),('das','Buch','Bücher','spannend'),('der','Baum','Bäume','alt'),('die','Blume','Blumen','schön'),('das','Kind','Kinder','fröhlich'),('der','Tisch','Tische','rund'),('die','Tür','Türen','offen'),('das','Fenster','Fenster','sauber'),('der','Apfel','Äpfel','rot'),('die','Schule','Schulen','groß'),('das','Auto','Autos','schnell'),('der','Stuhl','Stühle','bequem'),('die','Tasche','Taschen','schwer'),('das','Bild','Bilder','bunt'),('der','Vogel','Vögel','klein'),('die','Maus','Mäuse','leise'),('das','Wasser','', 'kalt'),('der','Garten','Gärten','grün')]
for art,noun,plural,adj in nouns:
    add(f'Welcher Artikel gehört zu {noun}?',f'Es heißt {art} {noun}.')
    add(f'Bilde einen Satz mit {noun}.',f'{art.capitalize()} {noun} ist {adj}.')
    add(f'Schreibe einen Satz mit {art} {noun}.',f'{art.capitalize()} {noun} ist {adj}.')
    if plural:
        add(f'Was ist die Mehrzahl von {noun}?',f'Die Mehrzahl von {noun} ist {plural}.')
        add(f'Bilde einen Satz mit {plural}.',f'Die {plural} sind {adj}.')

verbs={
'gehen':['gehe','gehst','geht','gehen','geht','gehen'],
'lernen':['lerne','lernst','lernt','lernen','lernt','lernen'],
'spielen':['spiele','spielst','spielt','spielen','spielt','spielen'],
'lesen':['lese','liest','liest','lesen','lest','lesen'],
'schreiben':['schreibe','schreibst','schreibt','schreiben','schreibt','schreiben'],
'sein':['bin','bist','ist','sind','seid','sind'],
'haben':['habe','hast','hat','haben','habt','haben'],
'machen':['mache','machst','macht','machen','macht','machen'],
'kommen':['komme','kommst','kommt','kommen','kommt','kommen'],
'sprechen':['spreche','sprichst','spricht','sprechen','sprecht','sprechen']}
pronouns=['ich','du','er','wir','ihr','sie']
for verb,forms in verbs.items():
    add(f'Wie wird {verb} konjugiert?',', '.join(f'{p} {v}' for p,v in zip(pronouns,forms))+'.')
    for pronoun,form in zip(pronouns,forms):
        add(f'Wie heißt {verb} mit {pronoun}?',f'Es heißt: {pronoun} {form}.')

sentences=[
('Ich lese ein Buch.','Ich habe ein Buch gelesen.'),
('Ich spiele im Garten.','Ich habe im Garten gespielt.'),
('Ich lerne Deutsch.','Ich habe Deutsch gelernt.'),
('Ich gehe nach Hause.','Ich bin nach Hause gegangen.'),
('Ich schreibe einen Brief.','Ich habe einen Brief geschrieben.'),
('Ich trinke Wasser.','Ich habe Wasser getrunken.'),
('Ich esse einen Apfel.','Ich habe einen Apfel gegessen.'),
('Ich mache eine Pause.','Ich habe eine Pause gemacht.'),
('Ich sehe einen Vogel.','Ich habe einen Vogel gesehen.'),
('Ich höre Musik.','Ich habe Musik gehört.')]
for present,past in sentences:
    add(f'Schreibe in der Vergangenheit: {present}',past)
    add(f'Schreibe in der Gegenwart: {past}',present)

corrections=[('ich lese ein buch','Ich lese ein Buch.'),('der hund ist klein','Der Hund ist klein.'),('die katze schläft','Die Katze schläft.'),('wir lernen deutsch','Wir lernen Deutsch.'),('das haus ist groß','Das Haus ist groß.'),('ich habe eine frage','Ich habe eine Frage.'),('guten morgen','Guten Morgen!'),('ich bin müde','Ich bin müde.'),('das wasser ist kalt','Das Wasser ist kalt.'),('ich gehe zur schule','Ich gehe zur Schule.')]
for wrong,right in corrections:
    add(f'Verbessere die Großschreibung: {wrong}',right)
    add(f'Schreibe richtig: {wrong}',right)

scenes=[
('Schreibe drei Sätze über einen Garten.','Im Garten wachsen Blumen. Ein Vogel sitzt im Baum. Die Sonne scheint.'),
('Schreibe drei Sätze über die Schule.','Die Kinder gehen zur Schule. Sie lesen und rechnen. In der Pause spielen sie.'),
('Schreibe drei Sätze über einen Hund.','Der Hund läuft über die Wiese. Er spielt mit einem Ball. Danach schläft er.'),
('Schreibe drei Sätze über den Regen.','Draußen regnet es. Die Straße ist nass. Ich nehme einen Regenschirm mit.'),
('Schreibe drei Sätze über ein Buch.','Ich öffne ein Buch. Die Geschichte ist spannend. Ich lese noch eine Seite.'),
('Schreibe eine kurze Begrüßung.','Hallo! Schön, dass du da bist.'),
('Schreibe eine höfliche Bitte.','Kannst du mir bitte helfen?'),
('Schreibe eine kurze Entschuldigung.','Es tut mir leid. Ich werde besser aufpassen.'),
('Schreibe eine kurze Einladung.','Möchtest du am Samstag mit mir spielen?'),
('Schreibe einen freundlichen Abschied.','Bis bald! Ich wünsche dir einen schönen Tag.')]
for q,a in scenes:add(q,a)
random.Random(19).shuffle(dialogs)
root=Path(__file__).parent
(root/'training.txt').write_text(''.join(dialogs),encoding='utf-8')
print(f'{len(dialogs)} Dialoge, {sum(map(len,dialogs))} Zeichen')
