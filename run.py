#!/usr/bin/env python3
"""
Script de inicio para LCA_PRO
Ejecuta la aplicación Streamlit
"""

import sys
import os
from pathlib import Path

def main():
    # Asegurar que estamos en el directorio correcto
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Importar y ejecutar streamlit
    try:
        import streamlit as st
        import streamlit.web.cli as st_cli

        # Ejecutar la aplicación
        sys.argv = ["streamlit", "run", "LCA_PRO (1).py", "--server.port", "8501", "--server.address", "0.0.0.0"]
        st_cli.main()

    except ImportError as e:
        print(f"Error: No se pudo importar streamlit. {e}")
        print("Ejecuta 'pip install -r requirements.txt' para instalar las dependencias.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()