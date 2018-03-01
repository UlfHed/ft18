# FT18
MiniProject DI2006 - Forensic Tool

## Metoder
- [x] En funktion som hittar alla filer i en katalog (eller på hela hårddisken). Inputen till funktionen är en path till en viss katalog man vill lista ut, t.ex. ”C:/nina/java”. Funktionen skall skapa en tupler eller lista med alla filer som hittas. Tänk på att du måste gå ner i alla underkataloger som finns i respektive katalog mm.

- [x] En funktion som kan hitta och lista ut alla filer av en viss typ (alltså filerna som har en viss ändelse pdf, txt, doc, ljudfiler, bildfiler, mm). Indata till funktionen är just filändelsen och mappen du skall leta i. Utdata är en lista med alla filer med just den filändelsen.

- [x] En funktion som söker efter en viss information i en viss
typ av fil. T.ex. namn, personnummer, mm i textfiler.
Funktionen returnerar alla filnamn där filerna innehåller
respektive information.

- [x] För vissa typer av filer är det svårt att läsa
innehållet. Ta reda på om det inte finns program som
konverterar dessa filer så att du sedan kan hitta
information. T.ex. pdf filer kan konverteras till ps
innan läsning.

- [x] En funktion som söker efter modifierade filer senast ett
viss datum

- [x] En funktion som kryptetar filer. Du skall kunna kryptera
och dekryptera filer. För denna kryptering skall du
använda datastrukturen Dictionary( kap 9) på följande
sätt:
-skapa en dictionary där du associerar koder till
varje bokstav, dvs, en bokstav ersätts med en annan
bokstav, siffra eller tecken, t.ex
codes= {’A’: ’p’, ’B’: ’7’, ’C’: ’#’ …… ’a’: ’B’ , ….m}
Med detta exempel bokstaven ” A” kommer att ersättas vid
kryptering med ”p” osv.

- [x] Filanalys. Datafiler är oftast mycket stora. Många gånger
i forensiskt arbete vill man kunna se skillnader mellan
innehållet i två filer eller hitta en fil som är närmast
likt någon annan fil som man har som undersökningsfil. I
ditt program skall du kunna jämföra två olika filer för
att se skillnader i innehåll. För detta skall du använda
datastrukturen Set (kap 9) och operationerna som erbjuds.
Outputen kan vara t.ex en lista med orden som inte i
filen A men inte i B samt orden som finns i filen B men
inte i A. Du kan också visualisera skillnaden på annat
sätt.

## Interface
- [x] CLI
- [x] GUI

## Extra
### HashSet
- [x] Hashset är något som används flitigt inom IT-forensiskt
arbete. Ett hashset är en fil som innehåller hashsummor
för olika typer av filer, dessa filer kan vara filer som
kan anses suspekta eller så kan det vara kända ofarliga
filer tex omodifierade operativsystemfiler. Er uppgift är
att när filer läses in körs en funktion som tar fram
hashvärdet för varje fil, detta kontrolleras sedan mot
ert egenskapade hashset. Ni kan själva välja om ni vill
kontrollera mot suspekta filer eller mot kända ofarliga
filer eller båda. Om ni väljer suspekta bör dessa kanske
skrivas ut för sig eller markeras på något sätt. Om ni
väljer kända ofarliga filer så kan ni välja att inte
skriva ut dessa eller markera dessa på något annat sätt.

### Hårdvaru-mjukvaro egenskaper
- [x] Inom IT-forensik är det viktigt att dokumentera så mycket
som möjligt. Detta görs främst för att kunna återskapa
utvinningen och kunna bevisa att allt gjordes enligt alla
konstens regler. Det kan därför vara bra att ta fram alla
uppgifter som går att få tag på om utrustningen som
används. Er uppgift är att skriva ut information om
datorn som programmet körs på. Information som kan vara
intressent är vilken hårdvara (ram, cpu, gpu etc) och
mjukvara (operativsystem etc).


### Automatisk generering av rapport
- [ ] I det IT-forensiska arbetet ingår det nästan alltid
rapportgenerering, dvs en rapport som innehåller
information som kan vara intressant för tex en rättegång
och eller en individ. Er uppgift är att användaren av
programmet kan välja och markera filer som kan anses
suspekta och spara dessa. Användaren ska också kunna
skriva in egna kommentarer om hen så önskar. Rapporten
skall sedan sparas i ett lämpligt format så som pdf eller
dylikt, om bilder är markerade som suspekta så skall
dessa visas som bilder i dokumentet och till sist ska
användaren kunna bestämma var rapporten ska sparas.
