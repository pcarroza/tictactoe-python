from python.tictactoe import TicTacToe

class B:

    def foo(self):
        print("CLASE B")
class A(B):

    def foo(self):
        super().foo()
        print("IMPLEMENTACIÓN ")


if __name__ == '__main__':
    clasea = A()

    clasea.foo()
