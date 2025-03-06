from ping import ping_subnet
#from ssh import qytang_ssh
routers = ping_subnet(input("Please SUBNET you want to ping: "))
print(routers)
print(f"There are {len(routers)} routers in your network")