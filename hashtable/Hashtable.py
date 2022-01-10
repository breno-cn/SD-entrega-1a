ERRO = 5

class Hashtable:

    def __init__(self) -> None:
        # A gente pode usar o dict do python? deixar temporario pra não perder muito tempo
        self.data = dict()

    def create(self, key: str, value: str) -> None:
        if key in self.data:
            return ERRO

        self.data[key] = value

    def read(self, key: str) -> str:
        if key not in self.data:
            return ERRO

        return self.data[key]

    def update(self, key: str, value: str) -> None:
        if key not in self.data:
            return ERRO

        self.data[key] = value

    def delete(self, key: str, value: str) -> None:
        if key not in self.data:
            return ERRO

        self.data[key] = None
