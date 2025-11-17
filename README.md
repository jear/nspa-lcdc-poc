# nspa-lcdc-poc

# Infra svc running on Vmware
- Moprheus Entreprise
- https://github.com/jear/my-infoblox

## Kubernetes cluster hosting below services  ( 4 nodes  Rancher ) with : 
- https://github.com/jear/my-rook-ceph  ( For CSI with RWX )
- https://github.com/jear/my-metallb ( for k8s LoadBalancer )
- https://github.com/jear/my-traefik ( for Ingressroutes ) 

## Devops Infra services on Kubernetes (Rancher)
- https://github.com/jear/my-keycloack
  - https://vault.gpu02.lysdemolab.fr/ui/vault/auth
- https://github.com/jear/my-keyfactor ( EJBCA OSS PKI )
  - https://ejbca.gpu02.lysdemolab.fr/
- https://github.com/jear/my-pulp  : for Disconnected Python Pypi.org  ( https://pulpproject.org/ )
  - https://pulp.gpu02.lysdemolab.fr/pulp/api/v3/
- https://github.com/jear/my-gitlab
  - https://gitlab.ingress-gpu02.lysdemolab.fr/
- https://github.com/jear/my-awx ( Ansible )
  - https://awx.gpu02.lysdemolab.fr/#/login
- https://github.com/jear/my-vault ( for secrets not internal Morpheus Cyphers )
  - https://vault.gpu02.lysdemolab.fr/ui/vault/auth
- https://github.com/jear/my-artifactory ( OSS ) : for Disconnected Terraform/Puppet/Ansible provider repositories
  - https://artifactory.gpu02.lysdemolab.fr/ui/login

# AI services on Kubernetes (Rancher)
- https://github.com/jear/my-openwebui  : Disconnected  LLM with nVidia GPU



## Others ( optional )
- https://github.com/NginxProxyManager/nginx-proxy-manager
- https://github.com/jear/my-step-ca
- FreeIPA : https://github.com/jear/hcp-pks/tree/master/ldap
- https://github.com/jear/my-minio
