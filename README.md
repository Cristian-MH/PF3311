# PF3311
Programa de chat utilizando Python y OpenAI API.

## Informacion general
- Curso: PF3311
- Entrega: Tarea 4
- Autor: Cristian Martínez Hernández 

## 1) Crear API Key de OpenAI
1. Inicia sesion en la plataforma de OpenAI.
2. Crea una API key nueva.
3. Guardala en un lugar seguro. No la compartas ni la subas a Git.

## 2) Configurar proyecto
1. (Opcional) Crear entorno virtual:
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
2. Instalar dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Crear archivo `.env` a partir de `.env.test`:
   ```powershell
   Copy-Item .env.example .env
   ```
4. Editar `.env` y pegar tu key real en `OPENAI_API_KEY`.

## 3) Ejecutar chat en consola
```powershell
python app.py
```
Escribe `salir` para terminar.

## 4) Seguridad para Git
- `.env` ya esta ignorado por `.gitignore`.
- Antes de hacer `git push`, verifica que no exista ninguna key en archivos versionados.
