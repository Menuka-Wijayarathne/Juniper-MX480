from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
import yaml


def main():

 input_file = '/home/jsadmin/Automation/hosts-Ericsson.yaml'


 for key, value in yaml.full_load(open(input_file)).items():

  
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