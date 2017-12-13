from ldap3 import *
import ldap3
#
# LDAP_URI = '192.168.20.100'
# LDAP_USER = 'hq\\administrator'  #域和用户之间必须是双斜划线
# LDAP_PASS = '*9K8fD5'
# BASE_DN = 'OU=技术中心,OU=WH,DC=hq,DC=wwwarehouse,DC=com'
#
# server = Server(LDAP_URI, port=389, get_info=ALL)
# conn = Connection(server, user=LDAP_USER, password=LDAP_PASS, authentication=NTLM, auto_bind=True)
# conn.search(BASE_DN, '(objectCategory=person)', search_scope=SUBTREE, attributes=['sAMAccountName', 'name', 'mail', 'manager'])
#
#
#
# from sql.models import users
#
# for item in conn.entries:
#     # print(item.sAMAccountName, item.name, item.mail)
#     username = item.sAMAccountName
#     if users.objects.filter(username=username).count() == 0:
#         user = users(username=item.sAMAccountName, email=item.mail,display=item.name, is_staff=1)
#         user.save()
#
# # conn1 = Connection(server, user='hq\\'+'leo.lee', password='81002384')
#
# # print(conn1.bind())

LDAP_URL = '192.168.20.100'
# LDAP_USER = 'hq\\administrator'  #域和用户之间必须是双斜划线
# LDAP_PASSWORD = '*9K8fD5'
LDAP_USER = 'hq\\chenyi.cai'
LDAP_PASSWORD = 'CaiChenyi1!'
BASE_DN = 'OU=技术中心,OU=WH,DC=hq,DC=wwwarehouse,DC=com'

server = Server(LDAP_URL, port=389)
conn = Connection(server=server, user=LDAP_USER, password=LDAP_PASSWORD)
print(conn)
# print(type(conn))
print(conn.bind())


conn.search(BASE_DN, '(objectCategory=person)', search_scope=SUBTREE, attributes=['sAMAccountName', 'name', 'Mail', 'Sn', 'GivenName'])
for i in conn.entries:
    if 'chenyi.cai' == i.sAMAccountName:
        print('----------------------')
        print(i)
        print('----------------------')
        break



