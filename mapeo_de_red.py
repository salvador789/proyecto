#!/usr/bin/python3.8

from scapy.all import ARP, Ether, srp

red = '192.168.1.1/24'

paquete_arp = ARP(pdst=red)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

paquete = ether/paquete_arp

resultado = srp(paquete, timeout=4)[0]

dispositivos = []

for enviados, recividos in resultado:
 dispositivos.append({'Direccion Ip': recividos.psrc, 'Direccion Mac': recividos.hwsrc})

print("Dispositivos detectados en la red")
print("IP" + "             \t\t" + "Mac")

for dispositivo in dispositivos:
 print("{:16}     {}".format(dispositivo['Direccion Ip'], dispositivo['Direccion Mac']))

