#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Pius", "Gabriel")
say_my_name("Khainja", "Ongaro")
say_my_name("Gabby")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
