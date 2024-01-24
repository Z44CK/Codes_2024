from troposphere import Ref, Template, Parameter, Output
from troposphere.ec2 import Instance, SecurityGroup, SecurityGroupRule

template = Template()

nome_chave_parametro = template.add_parameter(
    Parameter(
            "KeyName",
            Description="Nome de um KeyPair EC2 existente para permitir o acesso SSH",
            Type="AWS::EC2::KeyPair::KeyName",
    )

)

for i in range(1, 4):
    ec2_instance = template.add_resource(
        Instance(
            f"MyEC2Instance{i}",
            ImageId="ami-xxxxxxxx",
            KeyName=Ref(nome_chave_parametro),
            InstanceType="t2.micro",
            SecurityGroups=[f"MySecurityGroup{i}"],
        )
    )

    grupo_de_seguranca = template.add_resource(
        SecurityGroup(
            f"MySecurityGroup{i}",
            GroupDescription=f"Permitir tráfego SSH e HTTP para MyEC2Instance{i}",
            SecurityGroupIngress=[
                SecurityGroupRule(
                    IpProtocol="tcp",
                    FromPort="22",
                    ToPort="22",
                    CidrIp="0.0.0.0/0",
                ),
                SecurityGroupRule(
                    IpProtocol="tcp",
                    FromPort="80",
                    ToPort="80",
                    CidrIp="0.0.0.0/0",
                ),
            ],
        )
    )

for i in range(1, 4):
    template.add_output(
        Output(
            f"PublicDns{i}",
            Description=f"DNS Publico da MyEC2Instance{i}",
            Value=ec2_instance.GetAtt("PublicDnsName"),
        )
    )

template_json = template.to_json()

print(template_json)
