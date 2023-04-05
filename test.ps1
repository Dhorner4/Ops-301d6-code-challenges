# Define variables for the AD domain, company name, and org chart
$domainName = "sunflow.local"
$companyName = "SunFlow"
$orgChart = @{
    "CEO" = "Adam Johnson"
    "CTO" = "Aisha Khan"
    "Hardware Engineer" = "Javier Rodriguez"
    "Software Engineer" = "Amira Ahmed"
    "Mobile Developer" = "Adam Ali"
    "Electrical Engineer" = "Maria Garcia"
    "Mechanical Engineer" = "Ahmed Ali"
    "Senior Hardware Engineer" = "Tom Wright"
    "Senior Software Engineer" = "Fatima Hassan"
    "CFO" = "Sarah Patel"
    "Director of Operations" = "Mustafa Khan"
    "Manufacturing Manager" = "Emma Brown"
    "Procurement Manager" = "Naveed Ahmed"
    "Logistics Coordinator" = "Abdul Rahman"
    "Production Coordinator" = "Isabel Lopez"
    "Director of Sales & Marketing" = "Harry Thompson"
    "Marketing Manager" = "Sofia Gomez"
    "Sales Manager" = "Mohammed Ali"
    "Business Development Manager" = "Mira Patel"
    "Sales Representative 1" = "Ali Khan"
    "Sales Representative 2" = "Carmen Rodriguez"
    "Account Manager" = "Liam Wilson"
    "Director of Customer Service" = "Olivia Green"
    "Customer Service Manager" = "Rosa Hernandez"
    "Technical Support Manager" = "David Chen"
    "Customer Service Representative 1" = "Georgia Evans"
    "Customer Service Representative 2" = "Antonio Rodriguez"
    "Technical Support Representative" = "Aaliyah Ahmed"
    "Customer Success Manager" = "Tariq Khan"
}

# Create the AD forest and set the forest functional level to Windows Server 2019
# First you need to check if you have Active Directory Module installed on computer. 
# Get-Module -ListAvailable -Name ActiveDirectory
# If not run the below code
Install-WindowsFeature RSAT-AD-PowerShell
#Once the Active Directory Module is installed and loaded, than you can run the below 
Install-ADDSForest -DomainName $sunflow.local

# Create the organizational units
New-ADOrganizationalUnit -Name "Engineering" -Path "DC=sunflow,DC=local"
New-ADOrganizationalUnit -Name "Operations" -Path "DC=sunflow,DC=local"
New-ADOrganizationalUnit -Name "Sales & Marketing" -Path "DC=sunflow,DC=local"
New-ADOrganizationalUnit -Name "Customer Service" -Path "DC=sunflow,DC=local"

# Create the users and assign them to their respective organizational units
$ouPath = "OU=Engineering,DC=sunflow,DC=local"
New-ADUser -Name $orgChart["CTO"] -SamAccountName "cto" -UserPrincipalName "cto@$domainName" -Path $ouPath -AccountPassword (ConvertTo-SecureString "P@ssword1" -AsPlainText -Force) -Enabled $true
$ouPath = "OU=Engineering,DC=sunflow,DC=local"
New-ADUser -Name $orgChart["Hardware Engineer"] -SamAccountName "hardware" -UserPrincipalName "hardware@$domainName" -Path $ouPath -AccountPassword (ConvertTo-SecureString "P@ssword1" -AsPlainText -Force) -Enabled $true
$ouPath = "OU=Engineering,DC=sunflow,DC=local"
New-ADUser -Name $orgChart["Software Engineer"] -SamAccountName "software"-UserPrincipalName "software@$domainName" -Path $ouPath -AccountPassword (ConvertTo-SecureString "P@ssword1" -AsPlainText -Force) -Enabled $true
