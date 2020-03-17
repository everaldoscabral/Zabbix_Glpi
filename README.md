## Zabbix integration with GLPI
These scripts automatic opening and closing GLPI tickets using API.

Source: https://github.com/janssenlima/zabbix-glpi
> **Tested and running on Ubuntu 18.04 64 bit.**
## Requirements
- **Script**: 
    - **ack_zabbix_glpi.py** is the script that recognizes the event in Zabbix via API.
    - **tickets_zabbix_glpi.php** is the script that opens and closes tickets in GLPI using the Webservices plugin.
 
- **Zabbix 4.4.1**
    - In **/etc/zabbix/zabbix_agentd.conf** find and set: EnableRemoteCommands=1
- **PHP 5.6**

     Include: (for both servers)
    - **php-soap**
    - **php-xmlrpc**
- **GLPI 4.9.5**
    - **Webservices Plugin** install latest from https://forge.glpi-project.org/projects/webservices/files
- **Python 2.7**
- API Zabbix development in Python, just execute in terminal -> # **pip install zabbix-api** ( on both servers: **GLPI** and **Zabbix** - if they are on different linux servers )

## Installing
Download scripts: **ack_zabbix_glpi.py** and **tickets_zabbix_glpi.php** and mvoe into zabbix directory: **_/usr/lib/zabbix/externalscripts_**.

-> # mv * zabbix * /usr/lib/zabbix/externalscripts/

-> # chmod + x /usr/lib/zabbix/externalscripts/* zabbix *

##  Zabbix web interface
1. Configuration > Action
2. From top right corner: Event source > Triggers > Create action.
3. On the next screen give the name of the action. Ex: Name > **Open GLPI ticket**.

### For Open Tickets:
1. In **Action** tab:
   - **Name:** Open GLPI ticket
   - **Type of calculation:** And/Or
   - **Conditions:** Trigger severity is greater than or equals _Warning_; Host equals _your-host_
   
2. In **Operations > Operations** tab click **New** and completes (all default only):
   - **Default operation step duration:** 60s
   - **Operations**:
       - **Operation type:** Remote command
       - **Target list:** Host: Zabbix server
       - **Type:** Custom script
       - **Execute on:** Zabbix server
       - **Commands:** 
       > php5.6 /usr/lib/zabbix/externalscripts/tickets_zabbix_glpi.php eventhost="{HOSTNAME}" event="DOWN" state="{TRIGGER.STATUS}" hostproblemid=0 lasthostproblemid=0 servico="{TRIGGER.NAME}" triggerid="{TRIGGER.ID}" eventzabbix="{EVENT.ID}"
3. Click Update (_Operations_) > Update
 
### For Close Tickets:
1. In **Action** tab:
   - **Name:** Close GLPI ticket
   - **Type of calculation:** And/Or
   - **Conditions:** Host equals _your-host_
   
2. In **Recovery operations > Operations** tab click **New** and completes (all default only):
   - **Operations**:
       - **Operation type:** Remote command
       - **Target list:** Host: Zabbix server
       - **Type:** Custom script
       - **Execute on:** Zabbix server
       - **Commands:** 
       > php5.6 /usr/lib/zabbix/externalscripts/tickets_zabbix_glpi.php eventhost="{HOSTNAME}" event="UP" state="{TRIGGER.STATUS}" hostproblemid=1 lasthostproblemid=1 servico="{TRIGGER.NAME}" triggerid="{TRIGGER.ID}" eventzabbix="{EVENT.ID}"
       
3. Click Update (_Operations_) > Update

#### <<< Finaly test >>> 
