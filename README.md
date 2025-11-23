# nspa-lcdc-poc devops infra

<img width="1332" height="684" alt="poc" src="https://github.com/user-attachments/assets/e14e2c7b-143f-4e1d-8d84-4b677cf306b9" />

# Infra svc running on Vmware
- Moprheus Entreprise
- Simplivity
- https://github.com/jear/my-infoblox

# VME
- https://hpe-vme-jear.lysdemolab.fr/login/account/1

## Kubernetes cluster hosting below services  ( 4 nodes  Rancher ) with : 
- https://github.com/jear/my-rook-ceph  ( For CSI with RWX )
- https://github.com/jear/my-metallb ( for k8s LoadBalancer )
- https://github.com/jear/my-traefik ( for Ingressroutes ) 

## Devops Infra services on Kubernetes (Rancher)
- https://github.com/jear/my-keycloack
  - https://keycloak.gpu02.lysdemolab.fr/
- https://github.com/jear/my-keyfactor ( EJBCA OSS PKI )
  - https://ejbca.gpu02.lysdemolab.fr/
- https://github.com/jear/my-pulp  : for Disconnected Python Pypi.org  ( https://pulpproject.org/ )
  - https://pulp.gpu02.lysdemolab.fr/pulp/api/v3/
- https://github.com/jear/my-gitlab
  - https://gitlab.ingress-gpu02.lysdemolab.fr/
- Loadbalancer.org 
  - https://lb-adc-01.lysdemolab.fr/ ( Trial expired )
  - https://lb-adc-01.lysdemolab.fr/ ( Trial expired )
- https://github.com/jear/my-awx ( Ansible )
  - https://awx.gpu02.lysdemolab.fr/#/login
- https://github.com/jear/my-vault ( for secrets not internal Morpheus Cyphers )
  - https://vault.gpu02.lysdemolab.fr/ui/vault/auth
- https://github.com/jear/my-artifactory ( OSS ) : for Disconnected Terraform/Puppet/Ansible provider repositories
  - https://artifactory.gpu02.lysdemolab.fr/ui/login

# AI services  (nVidia )
- k8s : https://github.com/jear/my-openwebui  : Disconnected  LLM with nVidia GPU
- HPE VME : HVM hypervisor + nVidia 


## Others ( optional )
- https://github.com/jear/my-step-ca
  - https://step-ca.lysdemolab.fr/acme/acme/directory
- FreeIPA : https://github.com/jear/hcp-pks/tree/master/ldap ( Private repo, please aske me to add you as collaborator )
  - https://freeipa.lysdemolab.fr/ipa/ui/
- https://github.com/jear/my-minio  ( S3 backend for Morpheus user  bucket / storage for default backup / storage for images  ... )
- https://github.com/NginxProxyManager/nginx-proxy-manager
