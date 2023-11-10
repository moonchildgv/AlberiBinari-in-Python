class AlberoBin:
    # COSTRUTTORE
    def __init__(self, val):
        self.val: int = val
        self.sin: AlberoBin = None
        self.des: AlberoBin = None
        self.parent: AlberoBin = None

# Si definisca un metodo che riceve un albero binario di interi e restituisce un boolean e in particolare
# il metodo restituisce vero se e solo la parte informativa (valore) di tutti i nodi foglia è un valore
# maggiore di k
def analizzaFoglia(a: AlberoBin, k: int):
    if a is None:
        return True
    if a.sin is None and a.des is None:
        return a.val > k
    return analizzaFoglia(a.sin, k) and analizzaFoglia(a.des, k)

# Si definisca un metodo che riceve un albero binario di interi e restituisce un intero che corrisponde
# al costo del cammino (da a a foglia) di costo massimo dove il costo di un cammino è dato dalla
# somma dei valori dei nodi che d
def camminoMax(a: AlberoBin):
    if a is None:
        return 0
    return a.val + max(camminoMax(a.sin), camminoMax(a.des))

# Si definisca un metodo che riceve un albero binario di interi e un intero x che restituisce true se e
# solo se esiste almeno un nodo in a tale che x appare sia nel sottoalbero sin che nel sottoalbero
# des di n
def presente(a: AlberoBin, x: int):
    if a is None:
        return False
    if a.val == x:
        return True
    return presente(a.sin, x) or presente(a.des, x)

def verifica(a: AlberoBin, x: int):
    if a is None: 
        return False
    return (presente(a.sin, x) and presente(a.des, x) or verifica(a.sin, x) or verifica(a.des, x))

# Contare i nodi che hanno esattamente un solo Figlio
def soloUnFiglio(a: AlberoBin):
    if a is None:
        return 0
    if a.sin is None and a.des is not None:
        return 1 + soloUnFiglio(a.des)
    if a.sin is not None and a.des is None:
        return 1 + soloUnFiglio(a.sin)
    return soloUnFiglio(a.sin) + soloUnFiglio(a.des)

# Somma di tutti gli elementi dell'albero
def somma(a : AlberoBin):
    if a is None:
        return 0
    return a.val + somma(a.sin) + somma(a.des)

# Si definisca un metodo che riceve un albero binario di interi in input e restituisce un booleano. Il
# metodo restituisce true se e solo se tutti i nodi foglia dell’albero in input hanno valore uguale a
# quello della radice. (in questo caso 5)
def ugualeRadice(a: AlberoBin):
    if a is None:
        return False
    return analizza(a, a.val)

def analizza(a: AlberoBin, radice: int):
    if a is None:
        return False
    if a.sin is None and a.des is None:
        return a.val == radice
    return analizza(a.sin, radice) and analizza(a.des, radice)

# Si definisca un metodo ricorsivo che riceve in input un albero binario di ricerca e due interi, 
# l=lower bound e u=upper bound e e restituisce un intero. Questo metodo deve restituire il numero di nodi
# dell’albero che hanno valori compresi nell’intervallo definitivo tra i due parametri in input.
def contaNodiRange(a: AlberoBin, l: int, u:int):
    if a is None:
        return 0
    if a.val > l and a.val < u:
        return 1 + contaNodiRange(a.sin, l,u) + contaNodiRange(a.des,l,u)
    return contaNodiRange(a.sin, l,u) + contaNodiRange(a.des,l,u)


# Si definisca un metodo che riceve in input un albero binario e restituisce un intero che corrisponde
# al numero di valori che appaiono in a almeno due volte. Tali valori devono essere conteggiati in
# ragione delle loro occorrenze. (output: 2 perché ci sono due 4)
def contaRipetuti(a: AlberoBin):
    d = {}
    contaR(a,d)
    sum = 0
    for k,v in d.items():
        if v >= 2:
            sum+=v
    return sum

def contaR(a: AlberoBin, d: dict):
    if a is None:
        return 0
    if a.val in d:
        d[a.val]+=1
    else:
        d[a.val]=1
    contaR(a.sin,d)
    contaR(a.des,d)

# Si definisca un metodo che riceve in input due alberi binari (a e b) e restituisce un booleano. Il
# metodo restituisce true se e solo se esiste un nodo nel primo albero a, al livello liv_a, che compare
# anche nel secondo albero b ad un livello più profondo rispetto a liv_a e dunque liv_b > liv_a.
def verificaa(a : AlberoBin, b: AlberoBin):
    if a is None or b is None:
        return False
    return controlloA(a,b,0)
def controlloA(a: AlberoBin, b:AlberoBin, liv_a:int):
    if a is None:
        return False
    if ePresente(a.val, b, liv_a, 0):
        return True
    return controlloA(a.sin, b, liv_a+1) or controlloA(a.des, b, liv_a+1)

def ePresente(x: int, b:AlberoBin, liv_a:int, liv_b:int):
    if b is None:
        return False
    if b.val == x and liv_b > liv_a:
        return True
    return ePresente(x, b.sin, liv_a, liv_b+1) or ePresente(x, b.des, liv_a, liv_b+1)


# Scrivere un metodo verificacammino che riceve un albero binario ed un altro parametro x che è un float, e
# restituisce vero se esiste un cammino (consideriamo dalla radice alla foglia) la cui media dei valori lungo il
# cammino sia >=x
def verificaCammino(a: AlberoBin, x:float):
    return verificaaa(a, x, 0,0)

def verificaaa(a: AlberoBin, x:float, sum:float, n:int):
    if a is None:
        return True
    if a.sin is None and a.des is None:
        return (a.val+sum)/n+1 >= x
    return verificaaa(a.sin, x, sum+a.val,n+1) or verificaaa(a.des, x, sum+a.val, n+1)


# Si scriva un funzione maggiore( a: AlberoBin, b: AalberoBin) che riceve in input due alberi e restituisce vero se tutti i valori
# di a sono contenuti in b.
def maggiore(a: AlberoBin, b:AlberoBin):
    if a is None:
        return True
    if b is None:
        return False
    if not contenuto(a.val, b):
        return False
    return maggiore(a.sin, b) and maggiore(a.des, b)

def contenuto(x:int, b:AlberoBin):
    if b is None:
        return False
    if b.val == x:
        return True
    return contenuto(x, b.sin) or contenuto(x,b.des)

# Altezza dell'albero
def altezza(a:AlberoBin):
    if a is None:
        return 0
    return 1+max(altezza(a.sin), altezza(a.des))

# Almeno una foglia == 0
def almenoUnaFogliaUgualeAZero(a:AlberoBin):
    if a is None:
        return False
    if a.sin is None and a.des is None:
        return a.val == 0 
    return almenoUnaFogliaUgualeAZero(a.sin) or almenoUnaFogliaUgualeAZero(a.des)

# Ritorna il numero di nodi che nell'albero hanno esattamente 2 figli.
def dueFigli(a: AlberoBin):
    if a is None:
        return 0
    if a.sin is not None and a.des is not None:
        return 1 + dueFigli(a.sin) + dueFigli(a.des)
    return dueFigli(a.sin) + dueFigli(a.des)

# ritorna la larghezza massima dell'albero, ovvero la differenza tra la posizione del nodo 
# che si trova più a destra nell'albero e la posizione del nodo che si trova più a sinistra.
# tips: la larghezza equivale al numero di nodi in ogni livello (NON UFFICIALE!!!)
def larghezza(a: AlberoBin):
    if a is None:
        return 0
    if a.sin is not None:
        return 1 + larghezza(a.sin)
    return 1

# Dato un albero in input e un intero z, restituisca true se e solo se presi 2 nodi distinti non foglia, 
# a livelli pari vale che x.val *y.val == z
def traccia0623(a:AlberoBin, z:int) -> bool:
    if a is None:
        return False
    return condizione(a,z,0)
def condizione(a:AlberoBin, z:int, l:int):
    if a.sin is not None or a.des is not None and l % 2 == 0:
        return a.sin.val * a.des.val == z
    return condizione(a,z,l+1)

# Restituisce true se e solo se per ogni nodo non foglia x dell’albero a vale che x.val 
# è pari alla somma dei valori dei nodi contenuti nel sottoalbero sx di x
def traccia0922(a:AlberoBin):
    if a is None:
        return False
    somma = sommaSx(a.sin)
    return controllo(a, somma)

def controllo(a: AlberoBin, somma: int):
    if a.sin is not None or a.des is not None:
        return a.val == somma
    
def sommaSx(a:AlberoBin):
    if a is None:
        return 0
    return a.val + sommaSx(a.sin) + sommaSx(a.des)

# Calcola la somma di tutti i nodi foglia maggiori di x
def sumGreaterThan(a:AlberoBin, x:int):
    if a is None:
        return 0
    return calcola(a.sin, x) + calcola(a.des, x)

def calcola(a:AlberoBin, x:int):
    if a is None:
        return 0
    if a.sin is None and a.des is None and a.val > x:
        return a.val + calcola(a.sin, x) + calcola(a.des, x)
    return calcola(a.sin, x) + calcola(a.des, x)        
    

# Restituisce True se e solo se tutti i nodi foglia f di a contengono un valore 
# che non appare in nessun altro nodo di a 
def verificaUnicita(a:AlberoBin):
    verificaUni(a,a)

def verificaUni(a:AlberoBin, albero:AlberoBin):
    if a is None:
        return True
    if a.sin is None and a.des is None:
        return conta(a.val, albero) == 1
    return verificaUni(a.sin, albero) and verificaUni(a.des,albero)

def conta(x: int, a:AlberoBin):
    if a is None:
        return 0
    if a.val == x:
        return 1 + conta(x,a.sin) + conta(x,a.des)
    return conta(x, a.sin) + conta(x, a.des)

# Si definisca un metodo che riceve in input un albero binario e un intero e restituisce il nodo
# simmetrico del modo x. Per simmetrico di un nodo si fa riferimento al nodo che esiste alla posizione
# simmetrica del nodo x nel sottoalbero opposto della radice
def trovaSimmetrico(a: AlberoBin, x: int):
    if a is None:
        return 0
    if a.val == x:
        return x
    return simmetrico(a.sin, a.des, x)

def simmetrico(sin:AlberoBin, des:AlberoBin, x:int):
    if sin.val == x:
        return des.val
    if des.val == x:
        return sin.val
    return simmetrico(sin.sin, des.des, x)


# Si definisca un metodo che riceve in input un albero binario e un intero liv. 
# Il metodo restituisce true se e solo se la foglia che si trova a minore profondità 
# (nodo foglia più vicino alla radice) in su un livello minore di liv
def pocoProfondo(a: AlberoBin, liv:int):
    return eProfondo(a, liv, 0)
def eProfondo(a: AlberoBin, liv:int, liv_corrente:int):
    if a is None:
        return False
    if a.sin is None and a.des is None:
        return (liv_corrente+1) < liv
    return eProfondo(a.sin, liv, liv_corrente+1) and eProfondo(a.des, liv, liv_corrente+1)


# Esempio di albero binario
#        5
#       / \
#      3   7
#     / \   \
#    4   4   9

# Creazione dell'albero binario
albero = AlberoBin(5)
albero.sin = AlberoBin(3)
albero.sin.sin = AlberoBin(4)
albero.sin.des = AlberoBin(4)
albero.des = AlberoBin(7)
albero.des.des = AlberoBin(9)

print("   ",albero.val)
print("  ","/","\ ")
print(" ",albero.sin.val, " ",albero.des.val)
print("","/","\ ", "","\ ")
print(albero.sin.sin.val," ",albero.sin.des.val," ",albero.des.des.val)


# Test della funzione analizzaFoglia
k = 1
risultato = analizzaFoglia(albero, k)
print(f"La foglia più grande di {k} esiste: {risultato}")

# Test della funzione camminoMax
print("il costo del cammino (da a a foglia) massimo è:", camminoMax(albero))

# Test della funzione verifica
x = 4
print(f"il valore {x} appare nel sottoalbero sin e des:",verifica(albero,4))

# Test della funzione soloUnFiglio
print("quanti nodi con un solo figlio ha quest'albero? ",soloUnFiglio(albero))

# Test della funzione somma
print("La somma di tutti valori dell'albero è: ", somma(albero))

# Test della funzione ugualeRadice
print("Sono tutti i valori uguali al valore della radice:", ugualeRadice(albero))

# Test della funzione contaNodiRange
low = 5
up = 10
print("quanti valori compresi tra",low,"e",up,"nell'albero:", contaNodiRange(albero,low,up))

# Test della funzione contaRipetuti
print("qual è la somma dei valori ripetuti 2 volte:",contaRipetuti(albero))

# Test della funzione verificaa
print("esiste un nodo del primo albero che compare ad un livello più profondo del secondo albero:", verificaa(albero, albero))

# Test della funzione verificaCammino
x = 5
print("esiste un cammino la cui media dei valori lungo il cammino sia >=",x,verificaCammino(albero,x))

# Test della funzione massimo
print("tutti i valori del primo albero sono contenuti nel secondo: ", maggiore(albero, albero))

# Test della funzione altezza
print("l'altezza dell' albero è:", altezza(albero))

# Test della funzione almenoUnaFogliaUgualeAZero
print("esiste almeno una foglia uguale a 0:", almenoUnaFogliaUgualeAZero(albero))

# Test della funzione dueFigli
print("quanti sono i nodi con due figli:", dueFigli(albero))

# Test della funzione larghezza
print("qual è la larghezza del'albero:", larghezza(albero))

# Test della funzione traccia0623
print(traccia0623(albero, 21))

# Test della funzione traccia0922
print(traccia0922(albero))

# Test della funzione sumGreaterThan
print(sumGreaterThan(albero, 8))

# Test della funzione trovaSimmetrico
x = 4
print("qual è il simmetrico del nodo",x,":", trovaSimmetrico(albero,x))