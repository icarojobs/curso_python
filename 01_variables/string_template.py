from datetime import date

name = "Bob"

greeting = "Hello, {} {} meu amigo!"

with_name = greeting.format(name, "Williams")
with_name_two = greeting.format("Icaro", "Jobs")

print(with_name)
print(with_name_two)


report = "Ribeirao Preto, {} de {} de {}"

today = date.today() # 2021-03-06

data = today.strftime("%d")
mes = today.strftime("%m")
ano = today.strftime("%Y")

date_now = report.format(data, mes, ano)

print(date_now)