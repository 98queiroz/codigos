'''
https://rszalski.github.io/magicmethods/

falando de metodos magicos..

#construtor da classe - 
    def __new__(cls, *args, **kwargs):
        #criando apenas uma instancia desse objeto.

        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste
        #toda classe deriva do object então é a mesma coisa chamar assim:
        #return object.__new__(cls)
        
        def __call__(self, *args):
        for i in args:
            print(i)       
        
        
'''


class A:    

    #contrutor - ele é executado assim que a classe é instanciada.(inicializador)
    def __init__(self) -> None:
       ...
    
    def __call__(self, *args, **kwds):
        print(args)
        print(kwds) 
    
    def __setattr__(self, key, value):
        #print(key, value)
        self.__dict__[key] = value
    
    #def __del__(self):
    #   print('objeto coletado')
    
    #def __str__(self):
    #    return 'mostra na tela'
    def __len__(self):
        return 55


a = A()
#a(1,2,3,4,5,6,7,8,9, nome='matheus')
#a.nome = 'matheus queiroz'
#print(a.nome)

print(len(a))