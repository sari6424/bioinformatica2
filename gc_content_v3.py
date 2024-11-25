# def gc_content(sequence):
#     sequence = sequence.rstrip("\n")
#     sequence = sequence.upper()
#     g_count = sequence.count("G")
#     c_count = sequence.count("C")
#     gc_content = g_count + c_count
#     gc_content = gc_content / len(sequence)
#     gc_content = round(gc_content * 100, 2)
#
#     return gc_content
#     pass
#
# fasta_file = "levadura.fasta"
# output_file = fasta_file.split(".")[0]
# output_file = output_file + "_gc_content.txt"
# print(output_file)
#
# sequence = str()
#
#
# with open(fasta_file) as file:
#     for line in file:
#         if line.startswith(">"):
#             pass
#         else:
#             line = line.rstrip("\n")
#             sequence += line
#
# print(gc_content(sequence))
#
# gc_content = gc_content(sequence)
# file1 = open(output_file, "w")
# file1.write(f"el contenido gc es {gc_content}\n")
# file1.close()
#
#
# # se debe documentar si las excepciones se ignoran o que se hace con ellas

# contenido
def gc_content(sequence):
    # Partir por enter / lineas
    sequence = sequence.rstrip("\n")
    # Pasar el contenido a mayúsculas
    sequence = sequence.upper()
    # Contar las G
    g_count = sequence.count("G")
    # Contar las C
    c_count = sequence.count("C")
    # Sumar las G y C
    gc_content = g_count + c_count
    # Pasar a porcentaje
    gc_content = gc_content / len(sequence)
    gc_content = round(gc_content * 100, 2)

    return gc_content

# Obtener el archivo
fasta_file = "levadura.fasta"

# Output file
output_file = fasta_file.split(".")[0]
output_file = output_file + "_gc_content.txt"
print(output_file)

sequence = ""

try:
    # Leer el archivo
    with open(fasta_file) as file:
        # Por cada línea del archivo fasta
        for line in file:
            # Si la línea no es un encabezado
            if not line.startswith(">"):
                line = line.rstrip("\n")
                sequence += line
except FileNotFoundError:
    print(f"El archivo {fasta_file} no se encuentra en el directorio")
    # Para evitar correr más código
    exit()


# Calcular el contenido GC
gc_content = gc_content(sequence)

# Imprimimos el contenido GC
print(gc_content)

# Guardar el contenido GC en un archivo
out = open(output_file, "w")
out.write(f"el contenido gc es {gc_content}\n")
out.close()