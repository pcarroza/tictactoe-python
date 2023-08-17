
class Terminal:

    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def read_string(self, title):
        response = None
        ok = False
        while not ok:
            try:
                response = input(title)
                ok = True
            except Exception:
                self.write_error("de cadena de caracteres")
        return response

    def read_int(self, title):
        response = None
        ok = False
        while not ok:
            try:
                response = int(input(title))
                ok = True
            except Exception:
                self.write_error("de número")
        return response

    def read_char(self, title):
        response = None
        ok = False
        while not ok:
            value = self.read_string(title)
            if len(value) != 1:
                self.write_error("caracter")
            else:
                response = value[0]
                ok = True
        return response


    @classmethod
    def write(cls, title):
        print(title)

    @classmethod
    def write_error(cls, format):
        print("ERROR DE FORMATO! Introdusca el valor con formato" + format + '.')


if __name__ == '__main__':

    color = Terminal.instance().read_char("Ingrese valor: ")

    print(color)
