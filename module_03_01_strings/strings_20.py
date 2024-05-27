import re

my_str = """2024 Календарь соревнований:
07.04.2024 — Гран При Японии; 
21.04.2024 - Гран При Китая"""

my_reg = re.compile(r'\d{2}\.\d{2}\.\d{2}')
match = re.findall(my_reg, my_str)
print(match)