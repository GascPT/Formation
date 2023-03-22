#!/bin/python
Import-Module ActiveDirectory

# Add the user to Active Directory
New-ADUser `
    -Name "Franz" `
    -DisplayName "Franz" `
    -GivenName "Franz" `
    -Surname "Ferdinand" `
    -UserPrincipalName "ferdi@GlobeXpower.com" `
    -SamAccountName "ferdi" `
    -EmailAddress "ferdi@GlobeXpower.com" `
    -Office "Springfield, OR" `
    -Company "GlobeX USA" `
    -Department "TPS Department" `
    -Title "TPS Reporting Lead" `
    -Enabled $True `
    -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) `
    -Path "CN=Users,DC=corp,DC=globexpower,DC=com"