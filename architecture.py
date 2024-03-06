from diagrams import Diagram, Cluster, Node, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import (
    VPC,
    InternetGateway,
    NATGateway,
    RouteTable,
    PublicSubnet,
    ELB,
    ALB,
)
from diagrams.aws.management import SystemsManager

with Diagram("Terraform AWS Architecture", show=False, direction="LR"):

    with Cluster("Region us-east-1"):
        vpc = VPC("prod-vpc")
        with Cluster("Availability Zone us-east-1a"):
            subnet = PublicSubnet("subnet-1")
            igw = InternetGateway("GW")
            rt = RouteTable("prod-route-table")
            sg = ELB("allow_web")  # Using ELB as a stand-in for a security group

            instance = EC2("web-server-instance")
            eip = ALB("EIP")  # Using ALB as a placeholder for Elastic IP

    vpc >> Edge(label="association") >> subnet
    igw >> Edge(label="0.0.0.0/0") >> rt
    igw >> Edge(label="::/0") >> rt
    subnet >> Edge(label="association") >> rt
    instance >> sg >> eip
