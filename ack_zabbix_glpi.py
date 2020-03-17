from zabbix_api import ZabbixAPI
import sys

server = "http://zabbix_ip_addresses/zabbix"
username = "zabbix_username"
password = "zabbix_password"

conexao = ZabbixAPI(server = server)
conexao.login(username, password)

reconhecer_evento = conexao.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no GLPI."})
