# VPC Networks - Controlling Access Lab

## Overview

In this lab, I created a more secure, scalable, and manageable web server deployment in Google Cloud using the VPC network. This process involved setting up two nginx web servers, configuring firewall rules, and exploring IAM roles and service accounts to control access to resources.

By the end of the lab, I had two web servers (blue and green) running in my VPC network, each serving web traffic. I learned to manage access to these servers using tagged firewall rules and applied IAM roles to implement the principle of least privilege.

## Objectives

In this lab, I performed the following tasks:

1. Created two nginx web servers (blue and green) in the default VPC network.
2. Configured firewall rules to control external HTTP access using network tags.
3. Created a service account and assigned IAM roles.
4. Explored Network Admin and Security Admin roles and tested their permissions.

## Lessons Learned

### 1. Importance of VPC Networks and Tagged Firewall Rules

Using a VPC network allowed I to isolate my web servers and control the traffic that could reach them. By applying tagged firewall rules, I selectively granted HTTP access to specific servers, in this case, the "blue" server only. In real-world scenarios, this level of control is essential for securing web applications and sensitive data, as it prevents unauthorized traffic from reaching critical infrastructure.

**Screenshot Suggestion**: Insert a screenshot here to show the configuration of firewall rules in the console.

### 2. Redundancy and Availability

The lab setup involved two web servers (blue and green) to ensure redundancy. If one server failed, the other would still serve traffic. This concept is crucial for maintaining high availability in real-world web applications. Organizations need to ensure that their web services remain online even during failures, which can be achieved through load balancing or redundant server setups.

**Screenshot Suggestion**: Insert a screenshot showing both web servers running in the Compute Engine console.

### 3. Principle of Least Privilege with Service Accounts

By creating a service account and assigning it specific IAM roles (Network Admin and Security Admin), I upheld the principle of least privilege. This practice minimizes the risk of accidental or malicious changes to my network and security settings. In real-world applications, assigning the correct permissions to service accounts is vital to ensuring the security of cloud environments.

### 4. Real-World Application of Network and Security Admin Roles

- **Network Admin Role**: In this lab, I learned that the Network Admin role allows listing and managing network resources but does not permit modifications to firewall rules. In a real-world organization, this role would be appropriate for a team managing the network but not the security configurations.
- **Security Admin Role**: The Security Admin role allows full control over firewall rules. This is vital in ensuring the correct security measures are applied, such as blocking unauthorized traffic or opening ports for specific services. Security Admins should be carefully assigned to prevent accidental exposure of sensitive resources.

**Screenshot Suggestion**: Insert a screenshot showing the JSON credentials for the service account being uploaded and applied.

### 5. Impact of Firewall Rules in Real-World Scenarios

In this lab, I created a firewall rule that allowed external HTTP access to the blue server only. In real-world web deployments, similar rules are used to limit access to specific services, reducing the attack surface of an organization’s infrastructure.

For instance, only allowing HTTP traffic to my public web server while blocking access to sensitive internal resources is a common practice in securing modern applications.

### 6. Automating Server Configuration with Cloud Shell

Using Cloud Shell and gcloud commands allowed I to quickly create and manage VMs, firewall rules, and service accounts. In a production environment, automating these tasks using scripts or CI/CD pipelines can streamline infrastructure setup and reduce human error.

## Real-World Applications

- **E-commerce**: Tagging rules can ensure only authorized traffic reaches web servers, protecting customer data and ensuring high availability.
- **Healthcare**: Service accounts with minimal privileges ensure patient data is secure and systems remain compliant with regulations like HIPAA.
- **Finance**: Firewalls and strict IAM roles protect transaction data and reduce the risk of fraud.

**Screenshot Suggestion**: Insert screenshots to show the curl output testing access to both blue and green servers from the test-vm instance.

## Skills Gained

- Understanding VPC networks and how they contribute to secure infrastructure.
- Configuring firewall rules using network tags for fine-grained access control.
- Working with IAM roles and service accounts to implement security best practices.
- Automating server and network management using Cloud Shell and gcloud commands.

By completing this lab, I have learned how to securely deploy and manage web servers on Google Cloud and how to apply real-world security and networking principles.
