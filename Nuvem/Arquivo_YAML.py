import yaml

cloud_group_config = {
    "app_name": "MyCloudApp",
    "environment": "Production",
    "instances": [
        {"id": 1, "type": "t2.micro", "dns": "MyEC2Instance1_PublicDns"},
        {"id": 2, "type": "t2.micro", "dns": "MyEC2Instance2_PublicDns"},
        {"id": 3, "type": "t2.micro", "dns": "MyEC2Instance3_PublicDns"},
    ],
}

with open("cloud_app_config.yaml", "w") as yaml_file:
    yaml.dump(cloud_group_config, yaml_file, default_flow_style=False)

print("Arquivo de configuração YAML gerado: cloud_app_config.yaml")
