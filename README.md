# 🔬 Proyecto de investigación cientifica

## 📃 Descripción 
Sistema para la recopilación de datos de experimentales de un laboratorio cientifico, su análisis y generación de informe final.

## ✨ Carácteristicas 

### 🟢 Características Realizadas

1. **✏️ Agregar un experimento**  
   Permite ingresar los datos básicos de un experimento, como:  
   - Nombre del experimento  
   - Fecha de realización       
   - Datos experimentales (valores numéricos o decimales)

2. **🔍 Visualizar los experimentos**  
   Muestra una lista de todos los experimentos ingresados, con opciones para:       
   - Ver con una vista de tabla los experimentos ingresados.

3. **🧮 Realizar cálculos**  
   Cálculo de estadísticas básicas (promedio, valor máximo y mínimo):  
   - Promedio, valor máximo y mínimo de los experimentos.     

4. **📊 Comparar experimentos**  
   Implementar la funcionalidad para comparar múltiples experimentos:     
   - Impresión de los experimentos disponibles en una lista, mostrando los datos de cada experimento.
   - Al final se imprime una tabla con las conclusiones de la comparación.

5. **🗑️  Eliminar un experimento**
   Permite al usuario decidir qué experimento desea eliminar por su Id

7. **🔚 Salir**  
   La opción de salida está operativa:  
   - Se sale del menú principal con la palabra clave `salir` o el número `7`  

### 🔴 Características Pendientes

1. **📑 Generar informe final**  
   Desarrollar una funcionalidad que permita generar un informe completo con:  
   - Descripción general de los experimentos (Tabla)
   - Resultados de los cálculos realizados (Tabla)
   - Análisis comparativo (cuando aplique) (Tabla)
   - Recomendaciones y conclusiones 

2. **💾 Exportar informe a archivo de texto**  
   Agregar la capacidad de exportar el informe generado en un archivo de texto (`.txt`), que incluya:  
   - Título y fecha del informe 
   - Secciones organizadas con los datos, cálculos y conclusiones  
   - Formato legible para compartir o almacenar 

3. **Visualización de resultados**  
   Configurar para que las conclusiones de la comparació´n se imprpiman en una tabla con columnas:
   - Id
   - Experimento
   - Mejor promedio
   - Max
   - Min


## 🛠️ Configuración del Entorno de Desarrollo

Sigue estos pasos para configurar el entorno virtual y las dependencias de tu proyecto en Python.

### 1. Clonar el repositorio
Primero, clona el repositorio desde GitHub:

```bash
git clone https://github.com/david-dev0415/investigacion-cientifica.git
```

Cambia a la carpeta del proyecto:

```bash
cd tu-repositorio
```

---

### 2. Crear el entorno virtual
Crea un entorno virtual llamado `venv` dentro del directorio del proyecto:

```bash
python -m venv venv
```

---

### 3. Activar el entorno virtual
Dependiendo de tu sistema operativo, activa el entorno virtual:

- **Windows:**
  
  ```bash
  .\venv\Scripts\activate
  ```

- **macOS/Linux:**
  
  ```bash
  source venv/bin/activate
  ```

Si la activación fue exitosa, verás el nombre del entorno virtual (por ejemplo, `(venv)`) antes del prompt de tu terminal.

---

### 4. Instalar dependencias
Con el entorno virtual activado, instala las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 5. Ejecutar el proyecto
Una vez instaladas las dependencias, ejecuta el script principal:

```bash
python main.py
```

Sigue las instrucciones en pantalla para interactuar con el sistema *Investigación Científica*.

---

### 🔄 Desactivar el entorno virtual
Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual con el siguiente comando:

```bash
deactivate
```

---

### 🚧 Notas adicionales
- Asegúrate de tener **Python 3.7 o superior** instalado.
- Si necesitas agregar nuevas dependencias, instálalas con `pip install <paquete>` y actualiza el archivo `requirements.txt` con:

  ```bash
  pip freeze > requirements.txt
  ```

## 🤝 Contribuir 
1. Haz un fork del repositorio.
2. Crea una nueva rama:
  ```bash
  git checkout -b feature/nueva-funcionalidad
  ```
3. Realiza tus cambios y haz commit:
  ```bash
  git commit -m 'Agrega nueva funcionalidad'
  ```
4. Sube tus cambios:
  ```bash
  git push origin feature/nueva-funcionalidad
  ```
5. Abre un Pull Request.

## 📄 Licencia 
Este proyecto está bajo la Licencia MIT.
```