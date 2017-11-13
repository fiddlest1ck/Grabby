import glob
import requests
import yaml

yaml_dict = {"urls": list()}


def get_response_status(url):
    response = requests.get(url)
    return response.status_code


def parse_yml_files():
    yml_files = glob.glob('./configs/*.yml')
    for single_yml in yml_files:
        loaded_yaml = yaml.load(open(single_yml))
        yaml_dict['urls'].extend(loaded_yaml['urls'])
    return yaml_dict
