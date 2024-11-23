import os
import subprocess
import time
import signal

def ejecutar_con_timeout(comando, timeout, log_file):
    """
    Ejecuta un comando con un límite de tiempo.
    Si excede el tiempo, envía SIGINT, seguido de SIGKILL si es necesario.
    Regresa el código de salida y el tiempo consumido.
    """
    with open(log_file, "a") as log:
        inicio = time.time()
        try:
            proceso = subprocess.Popen(
                comando, 
                shell=True, 
                stdout=log, 
                stderr=subprocess.STDOUT, 
                preexec_fn=os.setsid
            )
            while proceso.poll() is None:
                tiempo_transcurrido = time.time() - inicio
                if tiempo_transcurrido > timeout:
                    print(f"\n\tTimeout alcanzado. Enviando SIGINT al comando: {comando}")
                    os.killpg(os.getpgid(proceso.pid), signal.SIGINT)
                    time.sleep(5)  # Espera breve para permitir que SIGINT surta efecto

                    # Si el proceso sigue activo, fuerza la terminación con SIGKILL
                    if proceso.poll() is None:
                        print(f"\n\tComando aún activo. Enviando SIGKILL: {comando}")
                        os.killpg(os.getpgid(proceso.pid), signal.SIGKILL)
                    break
                time.sleep(1)

            resultado = proceso.wait()
            fin = time.time()
            return resultado, fin - inicio
        except Exception as e:
            print(f"Error al ejecutar '{comando}': {e}")
            os.killpg(os.getpgid(proceso.pid), signal.SIGKILL)
            return -1, 0
        finally:
            if proceso.poll() is None:
                proceso.terminate()
                proceso.wait()

def procesar_script(script,script_path, timeout):
    """
    Procesa un script .sh, ejecutando cada comando de Docker con un timeout.
    """
    log_file = script_path.replace(".sh", ".log")
    print(f"\nProcesando script: {script_path}")
    
    if not os.path.isfile(script_path):
        print(f"El archivo {script_path} no existe.")
        return

    with open(script_path, "r") as script:
        lineas = script.readlines()

    for linea in lineas:
        linea = linea.strip()
        if "docker" in linea:  # Filtrar solo los comandos relacionados con Docker
            print(f"\nEjecutando comando Docker: {linea}")
            resultado, tiempo_consumido = ejecutar_con_timeout(linea, timeout, log_file)
            if resultado == 124:
                print(f"\n\tTimeout alcanzado para '{linea}'.")
            elif resultado == 0:
                print(f"\n\t'{linea}' en {script} terminó correctamente en {tiempo_consumido:.2f} segundos.")
            else:
                print(f"\n\t'{linea}' en {script} terminó con código: {resultado} en {tiempo_consumido:.2f} segundos.")

def manejar_directorio(directorio, timeout):
    """
    Procesa todos los scripts dentro de un directorio.
    """
    scripts = ["L1.sh", "L3.sh","L5.sh"]
    print(f"Procesando el directorio: {directorio}")
    
    if not os.path.isdir(directorio):
        print(f"Directorio no encontrado: {directorio}")
        return

    for script in scripts:
        script_path = os.path.join(directorio, script)
        procesar_script(script,script_path, timeout)

def main():
    """
    Maneja la ejecución de los comandos Docker en múltiples directorios.
    """
    base_dir = os.path.abspath("Delays_")  # Convertir base_dir a absoluto
    niveles = ["1ms", "2ms","5ms", "7ms","10ms","20ms", "50ms","100ms"]
    timeout = 700  # Tiempo límite para cada comando Docker en segundos

    for nivel in niveles:
        directorio = os.path.join(base_dir + nivel, "docker_scripts")
        manejar_directorio(directorio, timeout)

if __name__ == "__main__":
    main()
