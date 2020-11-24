# Super quick-start guide per git

Questa è una guida pratica per l'uso di Git.

## Cos'è Git
Un software di versionamento distribuito estremamente popolare. Ti permette di tenere traccia dello stato
di una cartella (cioé dei file al suo interno) in vari istanti del tempo e consente di sincronizzare più copie della cartella,
che possono essere su uno stesso computer o su più computer; dunque è uno strumento per organizzare i file su uno o più computer.

In pratica è un programma, esattamente come word, adobe reader o steam, e in quanto tale è necessario installarlo per poterlo utilizzare sul proprio computer.

Oltre alla versione stand-alone, scaricabile dal [sito ufficiale](https://git-scm.com/), numerosi software di sviluppo permettono di "integrarlo" al loro interno (tramite dei plug-in, ad esempio), permettendo di utilizzarlo direttamente dalla loro interfaccia.
La versione base consiste in un'interfaccia a **linea di comando**, ovvero il programma si utilizza scrivendo dei comandi all'interno di una finestra di **terminale**; seppur meno accattivante, l'interfaccia a linea di comando è quella che offre maggiore flessibilità ed accesso diretto a tutte le sue funzionalità. Tuttavia sono presenti anche delle [versioni](https://git-scm.com/downloads/guis) che offrono un'interfaccia grafica dove è possibile eseguire le operazioni cliccando su pulsanti e navigando finestre (che non vedremo qui).

Inoltre sono presenti diversi siti (e.g. [github](https://github.com/)) che permettono di utilizzare git per gestire repository presenti online, cartelle che non sono fisicamente sulla nostra macchina (ma di cui possiamo avere una copia "di lavoro" sul nostro PC, sincronizzata con quella online e quelle dei nostri collaboratori sui rispettivi computer).  

Vediamo innanzitutto alcuni termini fondamentali e poi andiamo dritti al sodo con qualche "ricetta" utile.

## Concetti base
- **Repository (o repo):** cartella che utilizza il sistema di versionamento git, che sia sul vostro pc o su qualche altro pc nella rete. Al suo interno troverete la sottocartella *.git* (a meno che non si tratti di un bare repository), in cui Git tiene i file per il suo funzionamento (è una cartella nascosta, la vostra interfaccia potrebbe non mostrarvela). Se vi trovate in un repository potete utilizzare i comandi di git per eseguire operazioni (provate a scrivere `git status` sul terminale mentre al suo interno e poi provate quando siete in un'altra cartella a caso nel vostro computer e notate la differenza)
- **Snapshot (o Commit):** "checkpoint" del repository. Rappresenta lo stato del repository in un qualche momento passato. In qualsiasi momento potete "caricare" lo stato della cartella a un commit passato (**to checkout**) o crearne uno nuovo (**to commit**) per salvare i cambiamenti fatti a uno o più file. Ogni commit è identificato univocamente da un codice alfanumerico (uno *Hash* code) ed è corredato da un messaggio, compilato dall'autore del commit, che dovrebbe dare spiegazioni su cosa è stato aggiunto/rimosso/modificato. 
- **to add/stage files:** notificare a git che le modifiche effettuate su determinati files nel repo fino a questo momento dovranno essere registrate nel prossimo commit (contano come "modifiche" anche la creazione e l'eliminazione del file). Cioé, git non salva tutto automaticamente, bisogna dirgli esplicitamente quali modifiche predere in conto.
- **Branch:** puntatore ad UN SINGOLO snapshot. Più branch possono puntare allo stesso snapshot. In ogni momento è possibile visualizzare il branch dove si è eseguendo `git status` (se non si è su nessun branch viene riportato l'hash dello snapshot attuale assieme a una notifica del fatto che siamo in uno "headless state"). Quando si effettua un commit, il branch attuale avanza sul nuovo snapshot.
- **HEAD:** Puntatore allo snapshot attuale.
- **Merge:** operazione che consente di "fondere" le modifiche introdotte in uno snapshot qualsiasi con quelle dello snapshot che si sta visualizzando attualmente (HEAD), eventualmente generando un nuovo snapshot e/o spostando l'attuale branch. Alcuni scenari possibili:
  - Se HEAD è un predecessore del target, nessun nuovo snapshot viene generato, e HEAD e l'eventuale branch attuale vengono spostati sul target
  - Se HEAD e il target divergono (ovvero hanno introdotto modifiche diverse a partire da un certo snapshot in poi) ci sono due scenari possibili:
    - I due snapshot differiscono solo di modifiche  sovrapponibili, dunque il merge avviene automaticamente senza intoppi
    - I due snapshot hanno un **conflitto** poiché alcuni file sono stati modificati in entrambi in maniera incompatibile (e.g. uno ha modificato un paragrafo di un file di testo e l'altro l'ha cancellato.), dunque sarà necessario risolvere il conflitto per poter concludere l'operazione, oppure si annulla tutto.
- **Conflitto:** situzione che si verifica quando due snapshot hanno introdotto modifiche incompatibili ai file nel repo. Si palesa durante le operazioni di merge e rebase, sospendendo l'operazione in corso in attesa che l'utente apporti le modifiche desiderate ai file (andando praticamente a comporre la versione "finale" cucendo le linee delle versioni divergenti del file, eventualmente introducendo ulteriori aggiustamenti) per poter proseguire, o che venga annullata l'operazione.
- **Remote:** Qualsiasi altro repo di cui quello presente è a conoscenza. Può trattarsi di altri repo locali (i.e. in qualche altra cartella dello stesso computer) o remoti (e.g. su github o all'interno della LAN). Grazie ad essi possiamo sincronizzare il nostro repo a qualsiasi altro (e in alcuni casi anche fare il contrario, sempre scrivendo comandi dalla nostra macchina).
- **Fetch:** Effettuare una copia locale di un branch (ovvero di tutti gli snapshot che lo precedono che non abbiamo già nel repo) di un remote senza alterare la nostra "copia di lavoro". I nomi dei branch copiati saranno preceduti dal nome del remote (e.g. se effetuo un `fetch` del branch `master` dal repo `origin`, all'interno del mio repo apparirà un branch `origin/master`, perfettamente uguale all'originale, mentra il branch `master` locale rimane invariato).
- **Pull:** Consiste nell'effettuare un `fetch` e conseguentemente un merge, permettendo quindi di aggiornare la copia locale del branch con quella di un remote. Se la copia locale ha introdotto delle variazioni il merge potrebbe dare luogo a un conflitto.
- **Push:** Inviare a un remote i cambiamenti (i.e. gli snapshot) introdotti fino al corrente branch, dunque è un'operazione che va a cambiare il remote lasciando il nostro repo invariato (se non per l'aggiornamento della rappresentazione locale del remote). Il push viene annullato nel caso in cui il branch remoto abbia una storia divergente dalla nostra copia locale (ovvero, è su uno snapshot che non è parte della catena di snapshot che, nella nostra copia locale, portano allo stato attuale); in tal caso dovremo ri-sincronizzare il nostro repo effettuando un pull e risolvendo eventuali conflitti prima di effettuare il push. Non è possibile effettuare push verso remote su cui non si possiedono i permessi (infatti, in contesti di sviluppo Open, spesso si parla di "pull-request" più che di "push", ma questa è un'altra storia ancora).
## How-tos

### Configurazione iniziale git
1. Aprire il terminale
2. `git config --global user.name "<nome>"` per impostare il proprio nome
3. `git config --global user.email "<indirizzo@email.dom>"` per impostare la propria email
4. `git config -l` per visualizzare tutte le impostazioni e controllare che i valori desiderati siano stati impostati

**Bonus (molto consigliato)**  
Per impostare un ALIAS (i.e. un comando personalizzato) per mostrare una "rappresentazione grafica" del repo in maniera pratica:
1. `git config --global alias.graph "log --all --decorate --oneline --graph"`
2. `git graph` per provare il comando

### Creare un repository locale

#### Creare un repository vuoto
1. entrare nella cartella in cui si vuole creare il repository
2. aprire un terminale (su windows aprire la git-bash)
3. `git init <nomeRepository>`
4. entrare nella cartella appena creata da terminale e controllare che il repo sia OK eseguendo `git status`

#### Creare un repository a partire da una cartella esistente (con o senza file)
1. entrare nella cartella che si vuole trasformare in repository
2. aprire un terminale (su windows aprire la git-bash)
3. `git init`
4. Controllare che il repo sia OK eseguendo `git status`

### Guardarsi intorno

#### Visualizzare l'help dei comandi
`git --help` oppure `git <comando> -h` per help specifico su `<comando>`.
#### Visualizzare lo stato di un repository
`git status`
#### Visualizzare la storia del repository
`git log`

### Clonare un repository
1. Copiare il path del repository da copiare (e.g. `/usr/tizio/repolocale` oppure `https://github.com/utente/reporemoto`)
2. entrare nella cartella in cui si vuole clonare il repository
3. aprire un terminale
4. `git clone pathdelrepository` (e.g. `git clone /usr/tizio/repolocale` o `git clone https://github.com/utente/reporemoto`)

### Creare un nuovo commit (i.e. salvare le modifiche)
1. Effettuare le modifiche desiderate ai file e controllare con `git status` che i file desiderati risultino modificati (in rosso)
2. Aggiungere i file al commit con `git add <filename>`, o `git add -A` per aggiungere tutto
3. `git status` per controllare che i cambiamenti che salveremo sono quelli desiderati (in verde)
4. `git commit` per creare il nuovo screenshot (e avanzare il branch corrente su di esso)

### Ignorare dei files nel repo
Basta creare un file chiamato `.gitignore` all'interno del repo (windows potrebbe darvi filo da torcere), aprirlo con un qualsiasi editor di testo e scrivere su ogni linea il file o i globbing pattern dei file o cartelle da ignorare. Aggiungere il file al repo è un'idea sana.

### Checkout a un branch o un commit (i.e. ripristinare lo stato del repository a uno dato)
1. Assicurarsi che non vi siano cambiamenti non salvati controllando con `git status` (in tal caso, fare un commit oppure annulare i cambiamenti e ripristinare lo stato della cartella all'ultimo snapshot... ci sarebbe anche la possibilità stash, ma per ora non ne parliamo)
2. `git checkout <nomebranch>` per passare a un branch oppure `git checkout <hashsnapshot>`  per andare a uno snapshot specifico SENZA essere su nessun branch (HEADLESS mode)

### Annullare dei cambiamenti non ancora "committati"
Questo metodo è utilizzabile quando vogliamo riportare dei file allo stato in cui erano all'ultimo commit.
- Se il file è staged (ie verde in `git status`) bisogna prima rimuoverlo dalla staging area (ovvero dire a git che non vogliamo più includere le sue modifiche più recenti al prossimo commit): come indicato da `git status`, basterà scrivere `git restore --staged <nomefile>`
- Se il file non è staged (ie rosso in `git status`) scrivere  `git restore <nomefile>`. ATTENZIONE: le modifiche fatte andranno perse
- Con `git reset --hard` riportiamo TUTTO esattamente nello stato dello snapshot da cui eravamo partiti a fare modifiche. Le modifiche fatte su TUTTI i file vengono perse.

### Risolvere un conflitto
Il conflitto potrebbe manifestarsi durante un merge (eg. durante un pull).
1. `git status` per vedere quali file sono in conflitto.
   1. Se ci sono dei file presenti in uno solo dei due snapshot che sono stati cancellati dall'altro sarà possibile scegliere se tenerli o rimuoverli nel merge scrivendo `git add <nomefile>` o `git rm <nomefile>` rispettivamente 
   2. Se ci sono file in conflitto che sono stati modificati in entrambi gli snapshot, il file in questione verrà modificato in maniera da mostrare chiaramente i punti dove avviene il conflitto (si parla di file testuali). Aprire il file incriminato e modificarlo come opportuno, dopodiché aggiungerlo nuovamente al commit con `git add <nomefile>`. Una volta che tutti i file in conflitto risulteranno "risolti" (`git status` li elenca colorati di verde) sarà possibile proseguire.
2. `git commit`

### Effettuare un `push` (inviare i cambiamenti a un remote)
1. `git status` per assicurarvi
   1.  che siete sul branch che desiderate inviare
   2.  Che abbiate già effettuato il commit dei cambiamenti che desiderate inviare
   3.  che il branch sia collegato al branch remoto desiderato. Nel caso in cui il branch non sia collegato ad alcun branch remoto (ad esempio, se avete creato il branch in locale e non avete ancora fatto un push con esso) bisognerà settare l' *upstream*: per settarlo basta seguire le istruzioni che appaiono se si tenta di effettuare una qualsiasi operazione che coinvolge il remote (`fetch`, `push` e `pull`), e proseguire. Infine, nota che lo status riporterà anche se il branch locale risulta up-to-date con la sua controparte remota, tuttavia tale informazione è aggiornata all'ultimo fetch, dunque non potete ancora fidarvi!
   
2.  `git fetch` per aggiornare la vostra copia locale della versione remota del branch. A questo punto `git status` vi dovrebbe dire se risultate avanti al branch remoto o se, malauguratamente, il branch remoto ha preso una strada diversa da quella del vostro (può succedere se altri hanno caricato cambiamenti prima di voi oppure voi stessi avete caricato cambiamenti usando copie diverse del repo, ad es, direttamente tramite git-hub, repl e la vostra copia locale). Date un'occhiata a `git graph` (vedi [configurazione iniziale git](#Configurazione-iniziale-git) per capire la situazione locale vs quella remota.
3.  Se il branch locale risulta più avanti di quello remoto procedete con `git push` e non dovete fare altro. In caso contrario dovrete prima effettuare un `git pull`, risolvere eventuali conflitti (vedi punto di prima) ed infine effettuare il `git push`.