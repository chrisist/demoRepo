#adsfsadfdsafasdfsdfadsf#adsfsadfdsafasdfsdfadsf#adsfsadfdsafasdfsdfadsf
#adsfsadfdsafasdfsdfadsf
#adsfsadfdsafasdfsdfadsf
#adsfsadfdsafasdfsdfadsf

import wmi

c = wmi.WMI()
for service in c.Win32_Service():
    print(service.Name)
