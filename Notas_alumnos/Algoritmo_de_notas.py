
def Sistema_Notas(nota):
    if nota < 5:
        categoria = "suspenso"
    elif nota < 7:
        categoria = "aprobado"
    elif nota < 9:
        categoria = "notable"
    else:
        categoria = "sobresaliente"

    print(f"Nota: {nota}")
    print(f"Categoría: {categoria}")

    return categoria


nota = float(input("Introduce la nota del alumno: "))
Sistema_Notas(nota)
