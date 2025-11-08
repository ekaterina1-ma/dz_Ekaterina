from address import Address
from mailing import Mailing

to_addr = Address(
    index="111111",
    city="Челябинск",
    street="Братьев Кашириных",
    house="1",
    apartment="71"
)

from_addr = Address(
    index="222222",
    city="Пласт",
    street="Связи",
    house="10",
    apartment="1"
)

shipment = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=1001,
    track='AB123456789RU'
)

print(
    f"Отправление {shipment.track} из "
    f"{shipment.from_address.index}, {shipment.from_address.city}, "
    f"{shipment.from_address.street}, {shipment.from_address.house} - "
    f"{shipment.from_address.apartment} в "
    f"{shipment.to_address.index}, {shipment.to_address.city}, "
    f"{shipment.to_address.street}, {shipment.to_address.house} - "
    f"{shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)
