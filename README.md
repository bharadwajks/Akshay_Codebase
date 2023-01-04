## Challenge #1

A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these resources on a cloud environment (GCP Cloud). Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.


Step1: Log into GCP Cloud Shell

Step2: Execute the scripts written in the Project creation folder in main.tf files...where main.tf files conatins the first step to create a project using terraform.

Step3: Enable neccessary firewall and VPC by writing the terraform scripts, where VPC.tf and firewall.tf has respective VPC & firewall setup.

## VPC
Setup the Virtual Private Cloud (VPC): It is a virtual network where we can  create and manage our GCP  resource in a more secure and scalable manner. Go to the VPC section of the GCP services, and click on the Create VPC button... I have written a script with the elp of terraform.. navigate to VPC.tf file



provider.tf file is nothing but a plugin that enables interaction with an API. 


If we are building a 3 tier app.. we should have follwoing as pre-requisites 

Cloud identity and organization 

Users and groups 

Administrative access  (IAM Permissions)

Set up billing 

Networking 
