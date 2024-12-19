## Tablas de contenido

1. [Información General](#información-general)
2. [Tecnologias](#tecnologias)
3. [Instrucciones](#instrucciones-de-compilación)
4. [Prueba de escaneo](#prueba-de-escaneo)
5. [Prueba de reporte](#prueba-de-reporte)

### Información General
***
Cración de API en contenedor mediante FastAPI que permite cargar archivos y escanearlos mediante la API de VirusTotal.
***

### Tecnologias
***
* [Python](https://www.python.org/downloads/) : Version 3.13.1
* [Docker Desktop](https://www.docker.com/products/docker-desktop/): Version 4.36.0.0
* [Visual Studio Code](https://code.visualstudio.com) : Version 1.96.1
***

### Instrucciones de compilación
***
1. Acceder al correo y aceptar la inviaticion al repositorio
2. Clonar repositorio localmente
   ![image](https://github.com/user-attachments/assets/398c8c40-bcd0-4335-a017-d87cba8916e4)

3. Abrir el proyecto desde un editor de codigo (VS code)
   
   ![image](https://github.com/user-attachments/assets/083bc43c-c586-4520-b816-fec54e8028f2)

5. Ubicarse en la carpeta del proyecto (Fastapi) y abrir una terminal
   ![image](https://github.com/user-attachments/assets/766732b5-6c95-4c97-a6a2-a80b178c9c93)

6. Escribir el siguiente comando "docker-compose up", con este comando se estara ejecutando el proyecto
   ![image](https://github.com/user-attachments/assets/c0afc391-70dc-425c-8b47-c054db4c0b8e)

7. Abrir un navegador y pegar la siguiente url:  http://localhost:8000/docs, aqui se visualiza la documentacion de la API y se realizan pruebas
    ![image](https://github.com/user-attachments/assets/ee5236b6-5bee-4946-af93-b0e9ef84784a)

8. Clic en /scanner, se despliegan informacion y dar clic en botón "Try it out"
   ![image](https://github.com/user-attachments/assets/4998e78f-0802-49a3-9254-ffdc479204ed)
9. Clic en selecionar archivo y eligimos archivo a escanear
    ![image](https://github.com/user-attachments/assets/bc57c0ce-f6a6-49ad-82d5-797180dce2e9)
10. Clic en boton azul Execute para ver la info del escaneo
    ![image](https://github.com/user-attachments/assets/48796d8c-f2e8-4d1d-bd58-e1edcaf50094)
    ![image](https://github.com/user-attachments/assets/ccc9da7a-073a-44c1-970b-74a8baf0a298)
11. Para el reporte copiamos el dato resource
   ![image](https://github.com/user-attachments/assets/5a5c3dcf-727a-4b09-b039-4fc39c1cd302)
12. Desplegamos /report/{resourceScan} y dar clic en botón "Try it out"
    ![image](https://github.com/user-attachments/assets/ab3d8b67-e2a8-4cf5-9cf0-3c8172d828b0)
    ![image](https://github.com/user-attachments/assets/d0febc20-a102-4acf-969c-42be7ee9a333)

14. Pegamos el dato y damos clic en botón azul Execute
    ![image](https://github.com/user-attachments/assets/cdacaa7b-f78f-4819-9f4f-8595f48e5e65)
    ![image](https://github.com/user-attachments/assets/5c8bb31e-4c39-469b-8de1-8c9af3966356)
    ![image](https://github.com/user-attachments/assets/5a9f561b-7a87-475a-be61-f12f792c3ff4)
***

### Prueba de escaneo
***
1. Clic en /scanner, se despliegan informacion y dar clic en botón "Try it out"
   ![image](https://github.com/user-attachments/assets/4998e78f-0802-49a3-9254-ffdc479204ed)
2. Clic en selecionar archivo y eligimos archivo a escanear
    ![image](https://github.com/user-attachments/assets/bc57c0ce-f6a6-49ad-82d5-797180dce2e9)
3. Clic en boton azul Execute para ver la info del escaneo
    ![image](https://github.com/user-attachments/assets/48796d8c-f2e8-4d1d-bd58-e1edcaf50094)
    ![image](https://github.com/user-attachments/assets/ccc9da7a-073a-44c1-970b-74a8baf0a298)
***

### Prueba de reporte
***
1. Para el reporte copiamos el dato resource
   ![image](https://github.com/user-attachments/assets/5a5c3dcf-727a-4b09-b039-4fc39c1cd302)
2. Desplegamos /report/{resourceScan} y dar clic en botón "Try it out"
    ![image](https://github.com/user-attachments/assets/ab3d8b67-e2a8-4cf5-9cf0-3c8172d828b0)
    ![image](https://github.com/user-attachments/assets/d0febc20-a102-4acf-969c-42be7ee9a333)

3. Pegamos el dato y damos clic en botón azul Execute
    ![image](https://github.com/user-attachments/assets/cdacaa7b-f78f-4819-9f4f-8595f48e5e65)
    ![image](https://github.com/user-attachments/assets/5c8bb31e-4c39-469b-8de1-8c9af3966356)
    ![image](https://github.com/user-attachments/assets/5a9f561b-7a87-475a-be61-f12f792c3ff4)
***
