# AWS Cloudformation Paramters Guide

    This is meant to be useful examples for navigating AWS Parameters
    
## Basic Structure

Parameters:
  <param name>:
    Description: <insert description>
    Type: <Type>
    
Parameters:
  SecurityGroupDescription:
    Description: This is a simple description
    Type: String
    
Parameters:
  SecurityGroupPort:
    Description: Simple Description of a number parameter (min/max value)
    Type: number
    MinValue: 1150
    MaxValue: 65535
    
## Explicit allowed values

Parameters:
  InstanceType
    Description: EC2 Instance type
    Type: String
    Default: t2.small
    AllowedValues:
      - t1.micro
      - t2.nano
      - t2.micro
      - t2.small
    ConstraintDescription: must be valid EC2 instance type
        
## CIDR regex

Parameters:
  SecurityGroupIngressCIDR:
    Description: The IP address range that can communicate to the EC2 instances
    Type: String
    Minlength: '9'
    Maxlength: '18'
    AllowedPattern: (\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,2})
    ContstraintDescription: must be a valid IP CIDR range of x.x.x.x/x
    
## CIDR list values

Parameters:
  DbSubnetIpBlocks:
    Description: Comma-delimeted list of three CIDR blocks
    Type: CommaDelimetedList
    Default: "10.0.48.0/24, 10.0.112.0/24, 10.0.176.0/24"
    

# Calling Parameters


## How to reference a parameter
Resources:
  <resource name>:
    Type: <AWS type>
    Properties:
      InstanceType: !Ref <param name>

## Select first item in a list parameter
Resources:
  <resource name>:
    Type: <AWS type>
    Properties:
      VpcId: !Ref <param name>
      CidrBlock: !Select [0, !Ref DbSubnetIpBlocks]
      
      
## Select SSM Parameter Store value
Parameters:
  <param name>:
    Description: <insert description>
    Type: <AWS Parameter Store Map>
    Default: <AWS Parameter Store Path>
    
Parameters:
  Parameter1:
    Description: This extracts the value from a parameter store parameter
    Type: AWS::SSM::Parameter::Value<String>
    Default: /dev/ec2/instanceType
    
Other Param Store Mappings:
AWS:SSM::Parameter::Name
AWS:SSM::Parameter::Value<String>
AWS:SSM::Parameter::Value<List<String>>
AWS:SSM::Parameter::Value<CommaDelimitedList>
AWS:SSM::Parameter::Value<AWS-Specific Parameter>
AWS:SSM::Parameter::Value<List<AWS-Specific Parameter>>

      
# Get value depending on a different parameter/resource example. AWS knows to build dependent resources first

Parameters:
  DbSubnetIpBlocks:
    Description: Comma-delimeted list of three CIDR blocks
    Type: CommaDelimetedList
    Default: "10.0.48.0/24, 10.0.112.0/24, 10.0.176.0/24"
    
Resources:

  MyEc2Instance:
    Type: AWS::EC2::Instance
    Properties:
      #we reference the Instance Type parameter
      InstanceType: !Ref InstanceType
      KeyName: !Ref KeyName
      ImageId: ami-0742b4e673072066f
      @ here we reference an internal Cloudformation source
      SubnetId: !Ref DbSubnet1

  DbSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref <param name>
      CidrBlock: !Select [0, !Ref DbSubnetIpBlocks]
