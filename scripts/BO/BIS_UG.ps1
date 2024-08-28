Start-Transcript -Path "C:\log.txt"

cd C:\ebid\ebid_medias\

<#
Invoke-WebRequest -Uri https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/eniq_bo/WINDOWS_HARDENING -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($("esjkadm100:Naples!0512"))) } -O WINDOWS_HARDENING.iso


Invoke-WebRequest -Uri https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/eniq_bo/Ericsson_Business_Intelligence_Deployment_Automation_Package_Media -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($("esjkadm100:Naples!0512"))) } -O Ericsson_Business_Intelligence_Deployment_Automation_Package_Media.iso
#>
#downloading files from Nexus
Start-Process "chrome.exe" "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/eniq_bo/WINDOWS_HARDENING"

Start-Process "chrome.exe" "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/eniq_bo/Ericsson_Business_Intelligence_Deployment_Automation_Package_Media"

sleep 65


#copying packages from downloads to ebid_medias path
Copy-Item -Path C:\Users\Administrator\Downloads\WINDOWS_HARDENING -Destination C:\ebid\ebid_medias\ -Recurse  -Force -PassThru  

Copy-Item -Path C:\Users\Administrator\Downloads\Ericsson_Business_Intelligence_Deployment_Automation_Package_Media -Destination C:\ebid\ebid_medias\ -Recurse  -Force -PassThru 

Rename-Item C:\ebid\ebid_medias\WINDOWS_HARDENING C:\ebid\ebid_medias\WINDOWS_HARDENING.iso -Force

Rename-Item C:\ebid\ebid_medias\Ericsson_Business_Intelligence_Deployment_Automation_Package_Media C:\ebid\ebid_medias\Ericsson_Business_Intelligence_Deployment_Automation_Package_Media.iso -Force





##########################################
$EBID_media='Ericsson_Business_Intelligence_Deployment_Automation_Package_Media.iso'

####Mounting iso images

$EBID = (Mount-DiskImage -ImagePath C:\ebid\ebid_medias\$EBID_media -PassThru | Get-Volume).DriveLetter

###Copying EBID Automation package to C:\ebid\
Copy-Item -Path ${EBID}:\ebid_automation -Destination C:\ebid\ -Recurse  -Force -PassThru


<#
editing ini files based on requirement
to be added later when there is a requirement
write-host "starting sleep"
sleep 120
#>

cd C:\ebid\ebid_automation\
#copy-item  ebid_automation.ini -destination ebid_automation1.ini

((Get-Content -path C:\ebid\ebid_automation\ebid_automation.ini -Raw) -replace 'Universe_Report_Promotion = No','Universe_Report_Promotion = Yes') | Set-Content -Path C:\ebid\ebid_automation\ebid_automation1.ini
Get-Content -path C:\ebid\ebid_automation\ebid_automation1.ini
ls

remove-item -Force -path ebid_automation.ini
rename-item ebid_automation1.ini ebid_automation.ini



#Automated Upgrade Process
Start-AwaitSession
Receive-AwaitResponse
Send-AwaitCommand C:\ebid\ebid_automation\ebid_master_script.ps1

sleep 15
Receive-AwaitResponse
#Wait-AwaitResponse "Enter FQDN of ENIQ Server:"
#Send-AwaitCommand '10.59.131.126'
Send-AwaitCommand 'atclvm638.athtem.eei.ericsson.se'


sleep 5
Receive-AwaitResponse
#Wait-AwaitResponse ""
Send-AwaitCommand  'dcuser'

sleep 5
Receive-AwaitResponse
#Wait-AwaitResponse ""
Send-AwaitCommand  'dcuser'

sleep 5
Receive-AwaitResponse
#Wait-AwaitResponse "Enter the drive letter where you want to take the backup (e.g.- D or E or F):"
Send-AwaitCommand  'E'

<#
Receive-AwaitResponse
#Wait-AwaitResponse "Enter Product Key:"
Send-AwaitCommand 'DJ40F-32SU140-ACHWP0A-2AM00W1-TA'
#>





<#
sleep 5
Receive-AwaitResponse
#Wait-AwaitResponse "Username of ENIQ Server:"
Send-AwaitCommand 'root'

sleep 5
Receive-AwaitResponse
#Wait-AwaitResponse "Password of ENIQ Server:"
Send-AwaitCommand 'shroot12'
#>


sleep 400
Receive-AwaitResponse
#Wait-AwaitResponse "Enter Windows Administrator Password:"
Send-AwaitCommand  'teamci@2017'

sleep 15
Receive-AwaitResponse
#Wait-AwaitResponse "Rebooting Server"
sleep 10
Receive-AwaitResponse
#Stop-AwaitSession

Write-Host "***wait for the Restart and login after 5 min***"


Stop-Transcript
