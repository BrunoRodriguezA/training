import re


text_general = (
 "Contactos: Ana <ana.lopez@example.com>, "
 "Luis <luis.1989@dominio.es>; "
 "Tel: +34 612-345-678 y +34 91 123 45 67; "
 "IPs: 10.0.0.221, 172.16.10.5, 192.168.1.100; "
 "URLs: https://santander.com, http://intranet.local/login, "
 "https://grafana.miempresa.com/d/abc-123?orgId=1 "
 "SNMP OID: 1.3.6.1.2.1.1.5.0; Fecha: 2025-10-22."
 )

logs = """
 2025-10-22 07:01:12,345 INFO  node=uk-n1 job=prometheus scrape=ok 200 145ms
 2025-10-22 07:01:13,002 WARN  node=uk-n2 job=snmp-exporter scrape=timeout - 
9001ms
 2025-10-22 07:01:15,777 ERROR node=us-n3 job=grafana status=500 path=/api/ds 
321ms
 2025-10-22 07:02:01,110 INFO  node=br-n4 job=alertmanager scrape=ok 200 132ms
 1
"""
prom_metrics = """
 # HELP node_cpu_seconds_total Seconds the CPUs spent in each mode.
 # TYPE node_cpu_seconds_total counter
 node_cpu_seconds_total{cpu="0",mode="idle"} 12345.67
 node_cpu_seconds_total{cpu="0",mode="system"} 890.12
 node_cpu_seconds_total{cpu="1",mode="user"} 456.78
 http_requests_total{method="GET",code="200"} 1024
 http_requests_total{method="POST",code="500"} 12
 """

#s+@s1.2-3


# \d+ 
'[A-Za-z0-9_.+-]'

def ej1_emails(text=text_general):
    "Devuelve una lista con todos los emails válidos"
    p = re.compile(r'[\w.+-]+@[\w.+-]+\.[\w.-]+')
    return p.findall(text)

# print(ej1_emails())

#"Tel: +34 612-345-678 y +34 91 123 45 67; "
def ej2_telefonos_es(text=text_general):
    """Encuentra números de teléfono de España con formatos comunes (+34,   espacios o guiones)."""
    p = re.compile(r'(?:\+34[\s-]?)?(?:\d{2}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}|\d{3}[\s-]?\d{3}[\s-]?\d{3})')   
    return p.findall(text)

# print(ej2_telefonos_es())

def ej3_ips_privadas(text=text_general):
    """Extrae todas las IPs privadas (10.x.x.x, 172.16-31.x.x, 192.168.x.x)."""
    # p = re.compile(r'(?:10\.[0-255]+\.[0-255]+\.[0-255]+|172\.[16,31]+\.[0-255]+\.[0-255]+|192\.168\.[0-255]+\.[0-255]+)')
    p = re.compile(r'\b(?:10(?:\.\d{1,3}){3}|172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2}|192\.168(?:\.\d{1,3}){2})\b')
    return p.findall(text)

print(ej3_ips_privadas())



