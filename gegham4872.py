
import phonenumbers
from phonenumbers import carrier, timezone, geocoder
from phonenumbers.phonenumberutil import number_type

number = "+37493340308"
print(carrier._is_mobile(number_type(phonenumbers.parse(number))))
print(phonenumbers.parse("+37493340308"))

my_number = phonenumbers.parse("+37493340308", "ARM")
print(carrier.name_for_number(my_number, "HAY"))

print(timezone.time_zones_for_number(my_number))

print(geocoder.description_for_number(my_number, "HAY"))

print(phonenumbers.is_valid_number(my_number))
print(phonenumbers.is_possible_number(my_number))




