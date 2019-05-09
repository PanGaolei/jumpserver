# -*- coding: utf-8 -*-
#

from django.utils.translation import ugettext_lazy as _

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

#
# Application
#

# app_type
APP_TYPE_CHROME = 'chrome'
APP_TYPE_PLSQL = 'plsql'
APP_TYPE_MSSQL = 'mssql'
APP_TYPE_MYSQL_WORKBENCH = 'mysql_workbench'
APP_TYPE_VMWARE = 'vmware'
APP_TYPE_OTHER = 'other'

# app_type
APP_TYPE_DB_LIST = [APP_TYPE_PLSQL, APP_TYPE_MSSQL, APP_TYPE_MYSQL_WORKBENCH]
APP_TYPE_BROWSER_LIST = [APP_TYPE_CHROME]

# app_type fields
APP_TYPE_BROWSER_LIST_FIELDS = [
    'browser_path', 'browser_target', 'browser_username', 'browser_password'
]
APP_TYPE_DB_LIST_FIELDS = [
    'db_path', 'db_ip', 'db_name', 'db_username', 'db_password'
]
APP_TYPE_VMWARE_FIELDS = [
    'vmware_path', 'vmware_target', 'vmware_username', 'vmware_password'
]
APP_TYPE_OTHER_FIELDS = [
    'other_path', 'other_cmdline', 'other_target', 'other_username',
    'other_password'
]

APP_TYPE_FIELDS_MAP = {
    APP_TYPE_CHROME: APP_TYPE_BROWSER_LIST_FIELDS,
    APP_TYPE_PLSQL: APP_TYPE_DB_LIST_FIELDS,
    APP_TYPE_MSSQL: APP_TYPE_DB_LIST_FIELDS,
    APP_TYPE_MYSQL_WORKBENCH: APP_TYPE_DB_LIST_FIELDS,
    APP_TYPE_VMWARE: APP_TYPE_VMWARE_FIELDS,
    APP_TYPE_OTHER: APP_TYPE_OTHER_FIELDS
}

# app_type choices
APP_TYPE_CHOICES = (
    (_('Browser'), (
        (APP_TYPE_CHROME, 'Chrome'),
    )
    ),
    (_('Database tools'), (
        (APP_TYPE_PLSQL, 'PL/SQL'),
        (APP_TYPE_MSSQL, 'msSQL'),
        (APP_TYPE_MYSQL_WORKBENCH, 'MySQL Workbench')
    )
    ),
    (_('Virtualization tools'), (
        (APP_TYPE_VMWARE, 'VMware Client'),
    )
    ),
    (_('Custom'), (
        (APP_TYPE_OTHER, 'Other'),
    )
    ),
)
