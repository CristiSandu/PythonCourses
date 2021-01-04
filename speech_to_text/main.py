import pyttsx3
import PyPDF2

book = open("The Silmarillion (Illustrated ebook).pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(4)
text = page.extractText()
#speaker.setProperty('rate')
print(text)
text2 = '''

În mod tradițional, programele pe care le-ați implementat până acum au fost scrise pentru calcul serial. Astfel, o problemă care trebuia rezolvată era împărțită într-un set discret de instrucțiuni, care erau executate pe un singur procesor în mod secvențial, una după cealaltă. La un moment dat de timp, o singură instrucțiune putea fi executată.

De cealaltă parte, programarea paralelă reprezintă utilizarea simultană a mai multor resurse de calcul pentru a rezolva o problemă. Din punct de vedere al pașilor de rezolvare, problema trebuie întâi împărțită în componente discrete care pot fi rezolvate concurent. Apoi, fiecare astfel de componentă trebuie mai departe împărțită în câte un set de instrucțiuni. În final, pentru a obține paralelism, instrucțiuni ale componentelor diferite ale problemei se pot executa simultan pe procesoare diferite. Pentru a se putea realiza acest lucru, este necesar un mecanism de coordonare a execuției diferitelor componente ale problemei.

Pentru a putea paraleliza în mod eficient o problemă, ea trebuie să poată fi împărțită logic în componente separate care pot fi executate simultan, iar durata execuției paralele a acestor componente trebuie să fie mai mică atunci când avem mai multe resurse de calcul decât atunci când avem o singură astfel de resursă. Pentru a putea executa un program paralel, este necesar să avem fie o mașină de calcul cu mai multe procesoare/core-uri, fie un număr arbitrar de astfel de mașini de calcul conectate printr-o rețea (dar aici extindem conceptul de programare paralelă către programarea distribuită).

Atunci când implementăm un program paralel, trebuie să ținem cont de mai multe considerente de design, cum ar fi:

    cum partiționăm problema?
    cum balansăm încărcarea?
    cum realizăm comunicația între componentele care rulează în paralel?
    ce dependențe de date avem?
    cum sincronizăm componentele paralele ale programului nostru?
    cât de mare este efortul de a paraleliza o problemă?

De-a lungul acestui semestru, vom încerca să adresăm cât mai multe din aceste probleme.
Fire de execuție

Un fir de execuție (sau thread în engleză) este definit ca un flux independent de instrucțiuni care pot fi planificate de către sistemul de operare. Din punct de vedere al unui programator, un fir de execuție poate fi descris cel mai bine ca o funcție care rulează independent de programul principal, iar un program paralel (cu mai multe fire de execuție, sau multi-threaded) poate fi privit ca toată mulțimea de astfel de funcții care pot fi planificate să ruleze simultan și/sau independent de către sistemul de operare.

Atenție! Există o distincție foarte importantă între conceptul de proces și cel de thread! Veți intra în detaliu la alte materii, dar, în acest moment, este foarte important de reținut faptul că un proces este o instanță de rulare a unui program (și deci două procese distincte nu partajează spațiul de adrese, care include stiva de program, variabile, date, etc.), pe când un thread este o unitate de lucru a unui proces (deci mai multe thread-uri pot avea acces partajat la variabile și alte date).

Datorită faptului ca firele de execuție ale aceluiași proces partajează resurse, modificările făcute de către un thread asupra acelor resurse (cum ar fi, de exemplu, închiderea unui fișier) vor fi observate de toate thread-urile acelui proces. Mai mult, doi pointeri cu aceeași valoare referă aceleași date, iar scrierea și citirea în/din aceeași zonă de memorie este posibilă, dar necesită sincronizare explicită din partea programatorului (mai multe detalii despre ce înseamnă sincronizarea și cum se realizează veți afla în laboratorul 2).

În general, programele care pot beneficia de implementare multi-threaded au câteva trăsături comune:

    conțin componente computaționale care se pot executa în paralel
    au date pe care se poate opera în paralel
    se blochează ocazional așteptând după I/O
    trebuie să răspundă la evenimente asincrone
    anumite componente de execuție au o prioritate mai mare decât altele.

'''
speaker.say(text2)
speaker.runAndWait()