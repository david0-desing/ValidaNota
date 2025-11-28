try:
    nota = float(input("Introduce la nota final del estudiante (0 a 20): "))
except ValueError:
    print("Entrada inválida. Por favor, introduce un número.")
    nota = -1 
categoria = ""
if nota < 0 or nota > 20:
    print("Nota fuera de rango.")
else:
    if nota >= 18 and nota <= 20:
        categoria = "Sobresaliente"
        print(f"Categoría: **{categoria}**")
    if nota >= 16 and nota <= 17.99:
        categoria = "Muy bueno"
        print(f"Categoría: **{categoria}**")
    if nota >= 14 and nota <= 15.99:
        categoria = "Bueno"
        print(f"Categoría: **{categoria}**")
    if nota >= 12 and nota <= 13.99:
        categoria = "Suficiente"
        print(f"Categoría: **{categoria}**")
    if nota >= 0 and nota <= 11.99:
        categoria = "Insuficiente"
        print(f"Categoría: **{categoria}**")
    if categoria == "Insuficiente":
        if nota < 8:
            print("*Mensaje Adicional: **Debe asistir a tutorías obligatorias**.*")
    if categoria == "Sobresaliente":
        if nota >= 19.5:
            print("*Mensaje Adicional: **Candidato a mención de honor**.*")