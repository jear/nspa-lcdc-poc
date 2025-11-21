# Palo VM deployment guide
https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/set-up-a-vm-series-firewall-on-an-esxi-server/install-a-vm-series-firewall-on-vmware-vsphere-hypervisor-esxi/perform-initial-configuration-on-the-vm-series-on-esxi

```

configure
set deviceconfig system type static
set deviceconfig system ip-address 10.69.41.8 netmask 255.255.255.0 default-gateway 10.69.41.254 dns-setting servers primary 10.69.0.151
```
