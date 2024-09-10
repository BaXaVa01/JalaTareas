# Información de ejemplo que tienes en tu matriz
# Supongo que tienes una estructura como esta:
# asignaciones = [[("Nombre de tarea 1", "https://enlace1.com"), ("Nombre de tarea 2", "https://enlace2.com")], ...]

# descripcion de la tarea, link, semana y clase
def createMd(asignaciones ):


    # Aqui vas a pegar la ruta donde se va a guardar el archivo 
    archivo_md = "C:\\Users\\carva\\Documents\\Obsidian Vault\\Tareas_Clases.md"

    # Abre (o crea) el archivo Markdown en modo escritura
    with open(archivo_md, "w", encoding="utf-8") as archivo:
        # Agrega el título principal
        
        # Variable que guarda el número de la clase actual
        
        claseAnterior = ""
        semanaAnterior = 0
        # Itera sobre las asignaciones de cada clase
        for clase in asignaciones:
            # Agregar un título para cada clase
            
            nombre_tarea, enlace_tarea, semana, nombreClase= clase

            if claseAnterior != nombreClase:
                archivo.write(f"##### **{nombreClase}**\n\n")
                claseAnterior = nombreClase
                semanaAnterior = 0  
            if semanaAnterior != semana:
                archivo.write(f"###### Semana {semana}\n\n")
                semanaAnterior = semana

            archivo.write(f"- [ ] {nombre_tarea}    ({enlace_tarea})\n")

            archivo.write("\n")
            

    print(f"Archivo Markdown '{archivo_md}' generado con exito.")
