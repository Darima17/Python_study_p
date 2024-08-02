import yaml


def gen_tasks():
    # Read the YAML file
    with open('../materials/todo.yml', 'r') as f:
        data = yaml.safe_load(f)

    tasks = []

    # Create tasks for installing packages
    for package in data['server']['install_packages']:
        tasks.append({
            'name': f'Install package: {package}',
            'package': {
                    'name': package,
                    'state': 'present'
            }
        })

    # Create tasks for copying files
    for name_files in data['server']['exploit_files']:
        tasks.append({
            'name': f'Copy file: {name_files}',
            'copy': {
                'src': name_files,
                'dest': '/tmp'}
        })

    # Execute files.
    all_g = ','.join(data['bad_guys'])
    tasks.append({
        'name': 'Execute files:',
        'command': [
            {'cmd': 'python3 /tmp/exploit.py'},
            {'cmd': 'python3 /tmp/consumer.py -e ' + all_g}
        ],
        'when': '"ok" in result.stdout'
    })

    return tasks


if __name__ == '__main__':
    playbook: list = [
        {
            'name': 'deploy',
            'hosts': 'localhost',
            'become': 'yes',
            'tasks': gen_tasks()
        }
    ]
    # Write the playbook to a new YAML file
    with open('../src/deploy.yml', 'w') as result_f:
        yaml.safe_dump(playbook, result_f, sort_keys=False)
