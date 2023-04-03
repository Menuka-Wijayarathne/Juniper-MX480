from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
import yaml

#https://networkzblogger.com/2018/10/03/juniper-config-backup-on-gitlab/
input_file = '/home/jsadmin/Automation/hosts-Ericsson.yaml'

def main():

 A = ["10.108.129.9","10.108.129.10","10.203.57.9","10.203.57.10"]
 for value in A:
    print(value)



    
   
    dev = Device(host=value, user='menuka_08214', passwd='BIGcisco#1991$', port=22)
    # open a connection with the device and start a NETCONF session
    try:
        dev.open()
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        return

    # Create an instance of Config
    cu = Config(dev)

    # Print existing rescue configuration or save one if none exists
    try:
        rescue = cu.rescue(action='get', format='text')
        if rescue is None:
            print ('No existing rescue configuration.')
            print ('Saving rescue configuration.')
            cu.rescue(action='save')
            
        else:
            print ('Rescue configuration found:')
            cu.rescue(action='delete')
            cu.rescue(action='save')
            print (rescue)
    except Exception as err:
        print (err)

    # End the NETCONF session and close the connection
    dev.close()

if __name__ == "__main__":
    main()