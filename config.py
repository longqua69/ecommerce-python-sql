import yaml
import pprint
 
def read_yaml():
    """ A function to read YAML file"""
    with open('compose.yml') as f:
        config = yaml.safe_load(f)
 
    return config

def write_yaml():
    with open('compose.yml') as f:
        config = yaml.safe_load(f)
 
if __name__ == "__main__":
 
    # read the config yaml
    my_config = read_yaml()
 
    # pretty print my_config
    pprint.pprint(my_config)