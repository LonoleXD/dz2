








class dog:
    def __init__(self, poroda, ves, vozrast, lubimayaeda, intellekt):
        self.poroda = poroda
        self.ves = ves
        self.vozrast = vozrast
        self.lubimayaeda = lubimayaeda
        self.intellekt = intellekt
class dogs:
    def __init__(self):
        self.olux = []
    def add_dog(self, poroda, ves, vozrast, lubimayaeda, intellekt):
        doge = dog( poroda, ves, vozrast, lubimayaeda, intellekt)
        self.olux.append(doge)
    def display_dog(self):
        if self.olux == []:
            print("Песов нет")
        else:
            print("Есть песы:")
            for doge in self.olux:
                    print(doge.poroda, doge.ves, doge.vozrast, doge.lubimayaeda, doge.intellekt)


doggg = dogs()
doggg.add_dog("Порода - Чихуахуа", "Вес - 4 кг", "Возраст - 2 года," "Любимая еда - мусор", "", "Интеллект - низкий")
doggg.display_dog()
