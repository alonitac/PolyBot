import json


def get_instance_name(tags):
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']

    raise RuntimeError('Name was not found')


def prepare_ansible_inventory():
    with open('hosts.json') as f:
        instances = json.load(f)

    hosts = []
    for instance in instances:
        instance_name = get_instance_name(instance['Tags'])
        instance_ip = instance['PublicIpAddress']
        instance_username = 'ec2-user'

        hosts.append(
            f"{instance_name} ansible_host={instance_ip} ansible_user={instance_username}\n"
        )

    with open('hosts', 'w') as f:
        f.write('[bot]\n')
        f.writelines(hosts)
        f.write("\n[bot:vars]\nansible_python_interpreter=/usr/bin/python3")


if __name__ == '__main__':

    prepare_ansible_inventory()
