from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 11", "+79000000000"),
    Smartphone("Apple", "iPhone 15", "+79111111111"),
    Smartphone("Honor", "10xLite", "+79222222222"),
    Smartphone("Huawei", "x8b", "+79333333333"),
    Smartphone("Samsung", "Galaxy s21", "+79444444444")
]

for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")
