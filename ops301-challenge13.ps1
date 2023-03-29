#!/usr/bin/env python3
#Script: Ops 301 Class 13 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/29/2023
# Assistance from https://blog.netwrix.com/2018/06/07/how-to-create-new-active-directory-users-with-powershell/

# Main

Import-Module ActiveDirectory
New-ADUser -Name "Franz Ferdinand" -GivenName "Franz" -Surname "Ferdinand" -SamAccountName "F.Ferdinand" -UserPrincipalName "ferdi@GlobeXpower.com" -AccountPassword(Read-Host -AsSecureString "Input Password") -Enabled $true
Get-ADUser F.Ferdinand

# Done