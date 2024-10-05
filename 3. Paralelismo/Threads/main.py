from threading import Thread, Lock
from tkinter import *

class Aula12():
    def exemplo1(self):
        class MyThread(Thread):
            def __init__ (self, id):
                Thread.__init__(self)
                self.id = id
            def run(self):
                print("Ola mundo com threads")
                print(f'Thread número {self.id}\n')
        #_________fim da classe___________________#
        threads,numThreads=[],10
        for i in range(numThreads): threads.append(MyThread(i))
        for i in range(numThreads): threads[i].start()
        print('Fim.')

    def exemplo2(self):
        class MyThread(Thread):
            def __init__ (self, id,barreira):
                Thread.__init__(self)
                self.id = id
                self.barreira=barreira
            def run(self):
                with self.barreira:
                    print("Ola mundo com threads")
                    print(f'Thread número {self.id}\n')
        #_________fim da classe___________________#
        barreira,threads,numThreads=Lock(),[],400
        for i in range(numThreads):
            threads.append(MyThread(i,barreira))
        for i in range(numThreads):
            threads[i].start()
            threads[i].join()
        print('Fim.')

    def exemplo3(self):
        class MyThread(Thread):
            def __init__(self,id):
                Thread.__init__(self)
                self.id = id
            def run(self):
                j=self.id
                c[j]=a[j]+b[j]
        #_________fim da classe___________________#
        a,b,c=[],[],[]
        numThreads,threads=10000,[]
        for i in range(numThreads): a.append(0)
        for i in range(numThreads): b.append(i)
        for i in range(numThreads): c.append(0)
        for i in range(numThreads): threads.append(MyThread(i))
        for i in range(numThreads): threads[i].start()
        for i in range(numThreads): threads[i].join()
        for j in range(numThreads): print(f'{j}) {a[j]}+{b[j]}={c[j]}')
        
    def exemplo4(self):
        class MyThread(Thread):
            def __init__ (self, idThread,quantThreads):
                Thread.__init__(self)
                self.id=idThread
                self.qntT=quantThreads
            def run(self):
                i=self.id
                max=len(a)
                while i<max:
                    c[i]=a[i]+b[i]
                    i+=self.qntT
        #_________fim da classe___________________#
        numThreads,tamLista,a,b,c,threads=4,10000,[],[],[],[]
        for i in range(tamLista):a.append(0)
        for i in range(tamLista):c.append(0)
        for i in range(tamLista):b.append(i)
        for id in range(numThreads):threads.append(MyThread(id,numThreads))
        for id in range(numThreads):threads[id].start()
        for id in range(numThreads):threads[id].join()
        for i in range(tamLista):print(f'i){i}) {a[i]}+{b[i]}={c[i]}')

    def exemplo5(self):
        class MyThread(Thread):
            def __init__ (self, idThread,quantThreads):
                Thread.__init__(self)
                self.id=idThread
                self.qnt=quantThreads
                
            def run(self):
                tamFaixa=int(len(a)/self.qnt)
                ini=self.id*tamFaixa
                fim=ini+tamFaixa
                for i in range(ini,fim):
                    c[i]=a[i]+b[i]
        #_________fim da classe___________________#
        numThreads,tamLista,a,b,c,threads=4,10000,[],[],[],[]
        for i in range(tamLista): a.append(0)
        for i in range(tamLista): c.append(0)
        for i in range(tamLista): b.append(i)
        for id in range(numThreads):threads.append(MyThread(id,numThreads))
        for id in range(numThreads):threads[id].start()
        for id in range(numThreads):threads[id].join()
        for i in range(tamLista):print(f'i={i}) {a[i]}+{b[i]}={c[i]}')

    def exemplo6(self):
        class MyThread(Thread):
            def __init__ (self, idThread,numThreads):
                Thread.__init__(self)
                self.id=idThread
                self.qnt=numThreads
                self.somaParcial=0

            def run(self):
                tamFaixa=int(len(a)/self.qnt)
                ini=self.id*tamFaixa
                fim=ini+tamFaixa
                for i in range(ini,fim):
                    self.somaParcial+=a[i]
        #------------------------------------#
        soma,numThreads,tamLista,a,threads=0,20,10000,[],[]
        for i in range(tamLista):a.append(1)
        for id in range(numThreads):
            threads.append(MyThread(id,numThreads))
        for id in range(numThreads):threads[id].start()
        for id in range(numThreads):threads[id].join()
        for id in range(numThreads):
            soma+=threads[id].somaParcial        
        print(f'{soma}')

    def exemplo7(self):
        continuar=True
        def parar():
            nonlocal continuar
            continuar=False

        def iniciar():
            nonlocal continuar
            continuar=True
            #controla a impressão do texto
            cont=0
            while(continuar):
                texto.insert('1.0',f'Linha{cont}\n')
                cont+=1
            #controla a animação
            carac=['\\','|','/','-']
            i=0
            while continuar:
                labelAnimacao.configure(text=f'Aguarde: {carac[i]}')
                i=(i+1)%4

        app = Tk()
        app.geometry("400x300+50+50")
        frameCtrl=Frame(app,background='light gray')
        frameTexto=Frame(app)
        botaoIniciar=Button(frameCtrl,text='Iniciar',command=iniciar)
        botaoParar=Button(frameCtrl,text='Parar',command=parar)
        frameCtrl.pack(side='left',expand=False, fill='both')
        frameTexto.pack(side='right',expand=True, fill='both')        
        labelAnimacao = Label(frameTexto,text='\\')
        texto=Text(frameTexto)
        texto.insert('0.0','Pressione iniciar.')
        labelAnimacao.pack(side='top',fill='x')
        texto.pack(expand=True,fill='both')
        botaoIniciar.pack(fill='x')
        botaoParar.pack(fill='x')
        mainloop()

    def exemplo8(self):
        continuar=True
        class ThreadTexto(Thread):
            def run(self):
                cont=0
                while(continuar):
                    texto.insert('1.0',f'Linha{cont}\n')
                    cont+=1
        class ThreadAnimacao(Thread):
            def run(self):
                carac=['\\','|','/','-']
                i=0
                while continuar:
                    labelAnimacao.configure(text=f'Aguarde: {carac[i]}')
                    i=(i+1)%4
        def parar():
            nonlocal continuar
            continuar=False
        def iniciar():
            nonlocal continuar
            continuar=True
            ThreadTexto().start()        
            ThreadAnimacao().start() 
        app = Tk()
        app.geometry("400x300+50+50")
        frameCtrl=Frame(app,background='light gray')
        frameTexto=Frame(app)
        botaoIniciar=Button(frameCtrl,text='Iniciar',command=iniciar)
        botaoParar=Button(frameCtrl,text='Parar',command=parar)
        frameCtrl.pack(side='left',expand=False, fill='both')
        frameTexto.pack(side='right',expand=True, fill='both')        
        labelAnimacao = Label(frameTexto,text='\\')
        texto=Text(frameTexto)
        texto.insert('0.0','Pressione iniciar.')
        labelAnimacao.pack(side='top',fill='x')
        texto.pack(expand=True,fill='both')
        botaoIniciar.pack(fill='x')
        botaoParar.pack(fill='x')
        mainloop()        
if __name__ == '__main__':
    exec =Aula12()
    exec.exemplo8()