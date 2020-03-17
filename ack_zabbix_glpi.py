from zabbix_api import ZabbixAPI
import sys
 
server = "http://10.1.10.90/zabbix"
username = "glpi"             
password = "Emergency@112"     
 
conexao = ZabbixAPI(server = server)
conexao.login(username, password)

reconhecer_evento = conexao.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no GLPI."})