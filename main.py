class Contato:
    def __init__(self, nome, email, telefone, cep):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cep = cep

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Cep: {self.cep}'


class ListaContatos:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, contato):
        self.contatos.remove(contato)

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)


class Interface:
    def __init__(self):
        self.lista_contatos = ListaContatos()

    def menu(self):
        print('1 - Adicionar contato')
        print('2 - Remover contato')
        print('3 - Listar contatos')
        print('0 - Sair')

    def adicionar_contato(self):
        nome = input('Nome: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        cep = input('Cep:')
        contato = Contato(nome, email, telefone, cep)
        self.lista_contatos.adicionar_contato(contato)

    def remover_contato(self):
        nome = input('Nome: ')
        contato = next((c for c in self.lista_contatos.contatos if c.nome == nome), None)
        if contato:
            self.lista_contatos.remover_contato(contato)
            print(f'{nome} removido da lista de contatos')
        else:
            print(f'{nome} não encontrado na lista de contatos')

    def listar_contatos(self):
        self.lista_contatos.listar_contatos()

    def executar(self):
        while True:
            self.menu()
            opcao = input('Digite uma opção: ')
            if opcao == '1':
                self.adicionar_contato()
            elif opcao == '2':
                self.remover_contato()
            elif opcao == '3':
                self.listar_contatos()
            elif opcao == '0':
                break
            else:
                print('Opção inválida')


if __name__ == '__main__':
    interface = Interface()
    interface.executar()
