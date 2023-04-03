from nornir import InitNornir
#from netmiko import send_command
from netmiko import Netmiko
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

# def nornir_basic_filtering_using_filter_method_example(task):
#     task.run(task=send_command, command_string="show ip int terse")

nr_filter = nr.filter(type="router", city="babolsar")
print(nr_filter.keys())
#results=nr_filter.run(task=nornir_basic_filtering_using_filter_method_example)