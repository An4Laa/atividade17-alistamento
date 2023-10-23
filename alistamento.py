from datetime import date

genero = str(input("Digite 'M' para gênero masculino e 'F' para genero feminino: "))
genero = genero.upper()

if genero == "F" :
    print("Você não precisa se alistar.")

else :
    ano_n = int(input("Digite o seu ano de nascimento: "))
    ano_h = date.today().year
    ano_a = ano_h - ano_n
    print(f"Você tem {ano_a} anos.")

    if ano_a < 18 :
        print("Você ainda não precisa se alistar.")
        ano_f = 18 - ano_a
        print(f"Ainda lhe restam {ano_f} tranquilos anos. Descanse.")
    elif ano_a == 18 :
        print("Caramba! Bem na hora! Se aliste agora.")
    elif ano_a > 18 :
        print("Já passou do tempo de se alistar.")
        tempo_p = ano_a - 18
        print(f"Você devia ter se alistado a {tempo_p} anos.")