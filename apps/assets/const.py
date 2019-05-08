# -*- coding: utf-8 -*-
#

UPDATE_ASSETS_HARDWARE_TASKS = [
   {
       'name': "setup",
       'action': {
           'module': 'setup'
       }
   }
]

ADMIN_USER_CONN_CACHE_KEY = "ADMIN_USER_CONN_{}"
TEST_ADMIN_USER_CONN_TASKS = [
    {
        "name": "ping",
        "action": {
            "module": "ping",
        }
    }
]

ASSET_ADMIN_CONN_CACHE_KEY = "ASSET_ADMIN_USER_CONN_{}"

SYSTEM_USER_CONN_CACHE_KEY = "SYSTEM_USER_CONN_{}"
TEST_SYSTEM_USER_CONN_TASKS = [
   {
       "name": "ping",
       "action": {
           "module": "ping",
       }
   }
]


ASSET_USER_CONN_CACHE_KEY = 'ASSET_USER_CONN_{}_{}'
TEST_ASSET_USER_CONN_TASKS = [
    {
        "name": "ping",
        "action": {
            "module": "ping",
        }
    }
]


TASK_OPTIONS = {
    'timeout': 10,
    'forks': 10,
}

CACHE_KEY_ASSET_BULK_UPDATE_ID_PREFIX = '_KEY_ASSET_BULK_UPDATE_ID_{}'

# asset > application > app_type
APP_TYPE_CHROME = 'chrome'
APP_TYPE_PLSQL = 'plsql'
APP_TYPE_MSSQL = 'mssql'
APP_TYPE_MYSQL_WORKBENCH = 'mysql_workbench'
APP_TYPE_VMWARE_CLIENT = 'vmware'
APP_TYPE_OTHER = 'other'

DB_APP_TYPE = [APP_TYPE_PLSQL, APP_TYPE_MSSQL, APP_TYPE_MYSQL_WORKBENCH]

APP_TYPE_CHOICES = (
    (APP_TYPE_CHROME, 'Chrome'),
    (APP_TYPE_PLSQL, 'PL/SQL'),
    (APP_TYPE_MSSQL, 'msSQL'),
    (APP_TYPE_MYSQL_WORKBENCH, 'MySQL Workbench'),
    (APP_TYPE_VMWARE_CLIENT, 'VMware Client'),
    (APP_TYPE_OTHER, 'Other'),
)

