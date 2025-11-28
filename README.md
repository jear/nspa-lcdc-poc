# nspa-lcdc-poc devops infra

<img width="1316" height="539" alt="image" src="https://github.com/user-attachments/assets/78696829-51c9-4571-adc5-65c631f6923f" />

# Infra svc running on Vmware
- Moprheus Entreprise
- Simplivity
- https://github.com/jear/my-infoblox

# VME
- https://hpe-vme-jear.lysdemolab.fr/login/account/1

## Kubernetes cluster hosting below services  ( 4 nodes  Rancher air-gapped ) with : 
- https://github.com/jear/my-rancher-air-gapped 
- https://github.com/jear/my-rook-ceph  ( For CSI with RWX )
- https://github.com/jear/my-metallb ( for k8s LoadBalancer )
- https://github.com/jear/my-traefik ( for Ingressroutes ) 
- https://github.com/jear/my-harbor
  - https://harbor.gpu02.lysdemolab.fr/

## Devops Infra services on Kubernetes 
- https://github.com/jear/my-keycloack
  - https://keycloak.gpu02.lysdemolab.fr/
- https://github.com/jear/my-keyfactor ( EJBCA OSS PKI )
  - https://ejbca.gpu02.lysdemolab.fr/
- https://github.com/jear/my-pulp  : for Disconnected Python Pypi.org  ( https://pulpproject.org/ )
  - https://pulp.gpu02.lysdemolab.fr/pulp/api/v3/
- https://github.com/jear/my-gitlab
  - https://gitlab.ingress-gpu02.lysdemolab.fr/
  - https://registry.ingress-gpu02.lysdemolab.fr
  - https://minio.ingress-gpu02.lysdemolab.fr
  - https://kas.ingress-gpu02.lysdemolab.fr
- Loadbalancer.org : GSLB = Polaris + PowerDNS
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
  - ToDo
- https://github.com/NginxProxyManager/nginx-proxy-manager
  - https://nginx-proxy-manager.lysdemolab.fr/login

# List of all images 
```
 kubectl get pods -A -o jsonpath='{range .items[*].spec.containers[*]}{.image}{"\n"}{end}'
releases-docker.jfrog.io/jfrog/router:7.177.8
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/artifactory-oss:7.117.18
releases-docker.jfrog.io/jfrog/nginx-artifactory-pro:7.117.18
releases-docker.jfrog.io/bitnami/postgresql:16.6.0-debian-12-r2
quay.io/ansible/awx:24.6.1
quay.io/sclorg/postgresql-15-c9s:latest
docker.io/redis:7
quay.io/ansible/awx:24.6.1
quay.io/ansible/awx-ee:24.6.1
quay.io/ansible/awx:24.6.1
docker.io/redis:7
quay.io/ansible/awx:24.6.1
quay.io/ansible/awx:24.6.1
gcr.io/kubebuilder/kube-rbac-proxy:v0.15.0
quay.io/ansible/awx-operator:2.19.1
keyfactor/ejbca-ce:9.1.1
docker.io/rancher/mirrored-calico-kube-controllers:v3.30.2
docker.io/rancher/mirrored-calico-node:v3.30.2
docker.io/rancher/mirrored-calico-node:v3.30.2
docker.io/rancher/mirrored-calico-node:v3.30.2
docker.io/rancher/mirrored-calico-node:v3.30.2
docker.io/rancher/mirrored-calico-typha:v3.30.2
docker.io/rancher/mirrored-calico-typha:v3.30.2
rancher/fleet-agent:v0.13.1
rancher/rancher-agent:v2.12.1
rancher/rancher-agent:v2.12.1
rancher/rancher-webhook:v0.8.1
rancher/system-upgrade-controller:v0.16.3
quay.io/jetstack/cert-manager-controller:v1.19.1
quay.io/jetstack/cert-manager-cainjector:v1.19.1
quay.io/jetstack/cert-manager-webhook:v1.19.1
quay.io/jetstack/cert-manager-acmesolver:v1.19.1
quay.io/jetstack/cert-manager-acmesolver:v1.19.1
quay.io/jetstack/cert-manager-acmesolver:v1.19.1
quay.io/jetstack/cert-manager-acmesolver:v1.19.1
registry.gitlab.com/gitlab-org/cloud-native/gitlab-operator:2.5.2
registry.gitlab.com/gitlab-org/build/cng/gitaly:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-exporter:16.1.0
registry.gitlab.com/gitlab-org/build/cng/gitlab-shell:v14.45.3
registry.gitlab.com/gitlab-org/build/cng/gitlab-shell:v14.45.3
registry.gitlab.com/gitlab-org/build/cng/gitlab-kas:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-kas:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-toolbox-ee:v18.5.2
minio/minio:RELEASE.2017-12-28T01-21-00Z
minio/mc:RELEASE.2018-07-13T00-53-22Z
registry.gitlab.com/gitlab-org/cloud-native/mirror/images/ingress-nginx/controller:v1.11.8@sha256:695d79381ee6af00c7f5c9fd434f50851d7d32838ad5b2c507e416cf2084fc79
registry.gitlab.com/gitlab-org/cloud-native/mirror/images/ingress-nginx/controller:v1.11.8@sha256:695d79381ee6af00c7f5c9fd434f50851d7d32838ad5b2c507e416cf2084fc79
docker.io/bitnamilegacy/postgresql:16.6.0
docker.io/bitnamilegacy/postgres-exporter:0.15.0-debian-11-r7
quay.io/prometheus-operator/prometheus-config-reloader:v0.83.0
quay.io/prometheus/prometheus:v3.4.2
docker.io/bitnamilegacy/redis:7.2.4-debian-12-r9
docker.io/bitnamilegacy/redis-exporter:1.58.0-debian-12-r4
registry.gitlab.com/gitlab-org/build/cng/gitlab-container-registry:v4.28.0-gitlab
registry.gitlab.com/gitlab-org/build/cng/gitlab-container-registry:v4.28.0-gitlab
registry.gitlab.com/gitlab-org/build/cng/kubectl:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-sidekiq-ee:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-toolbox-ee:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-webservice-ee:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-workhorse-ee:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-webservice-ee:v18.5.2
registry.gitlab.com/gitlab-org/build/cng/gitlab-workhorse-ee:v18.5.2
nvcr.io/nvidia/k8s-device-plugin:v0.17.4
nvcr.io/nvidia/k8s-device-plugin:v0.17.4
nvcr.io/nvidia/gpu-operator:v25.3.4
registry.k8s.io/nfd/node-feature-discovery:v0.17.3
registry.k8s.io/nfd/node-feature-discovery:v0.17.3
registry.k8s.io/nfd/node-feature-discovery:v0.17.3
registry.k8s.io/nfd/node-feature-discovery:v0.17.3
registry.k8s.io/nfd/node-feature-discovery:v0.17.3
registry.k8s.io/nfd/node-feature-discovery:v0.17.3
nvcr.io/nvidia/k8s/container-toolkit:v1.17.8-ubuntu20.04
nvcr.io/nvidia/k8s/container-toolkit:v1.17.8-ubuntu20.04
nvcr.io/nvidia/cloud-native/gpu-operator-validator:v25.3.4
nvcr.io/nvidia/cloud-native/gpu-operator-validator:v25.3.4
nvcr.io/nvidia/k8s/dcgm-exporter:4.3.1-4.4.0-ubuntu22.04
nvcr.io/nvidia/k8s/dcgm-exporter:4.3.1-4.4.0-ubuntu22.04
nvcr.io/nvidia/k8s-device-plugin:v0.17.4
nvcr.io/nvidia/k8s-device-plugin:v0.17.4
nvcr.io/nvidia/driver:580.82.07-ubuntu22.04
nvcr.io/nvidia/driver:580.82.07-ubuntu22.04
nvcr.io/nvidia/cloud-native/k8s-mig-manager:v0.12.3-ubuntu20.04
nvcr.io/nvidia/cloud-native/gpu-operator-validator:v25.3.4
nvcr.io/nvidia/cloud-native/gpu-operator-validator:v25.3.4
goharbor/harbor-core:v2.14.0
goharbor/harbor-db:v2.14.0
goharbor/harbor-jobservice:v2.14.0
goharbor/nginx-photon:v2.14.0
goharbor/harbor-portal:v2.14.0
goharbor/redis-photon:v2.14.0
goharbor/registry-photon:v2.14.0
goharbor/harbor-registryctl:v2.14.0
goharbor/trivy-adapter-photon:v2.14.0
quay.io/keycloak/keycloak:26.4.2
quay.io/keycloak/keycloak:26.4.2
mirror.gcr.io/postgres:17
index.docker.io/rancher/rke2-cloud-provider:v1.33.1-0.20250516163953-99d91538b132-build20250612
index.docker.io/rancher/rke2-cloud-provider:v1.33.1-0.20250516163953-99d91538b132-build20250612
index.docker.io/rancher/rke2-cloud-provider:v1.33.1-0.20250516163953-99d91538b132-build20250612
index.docker.io/rancher/rke2-cloud-provider:v1.33.1-0.20250516163953-99d91538b132-build20250612
index.docker.io/rancher/hardened-etcd:v3.5.21-k3s1-build20250612
index.docker.io/rancher/hardened-etcd:v3.5.21-k3s1-build20250612
index.docker.io/rancher/hardened-etcd:v3.5.21-k3s1-build20250612
index.docker.io/rancher/hardened-etcd:v3.5.21-k3s1-build20250612
rancher/klipper-helm:v0.9.8-build20250709
rancher/klipper-helm:v0.9.8-build20250709
rancher/klipper-helm:v0.9.8-build20250709
rancher/klipper-helm:v0.9.8-build20250709
rancher/klipper-helm:v0.9.8-build20250709
rancher/klipper-helm:v0.9.8-build20250709
rancher/klipper-helm:v0.9.8-build20250709
rancher/klipper-helm:v0.9.8-build20250709
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
index.docker.io/rancher/hardened-kubernetes:v1.33.4-rke2r1-build20250814
rancher/hardened-coredns:v1.12.3-build20250806
rancher/hardened-coredns:v1.12.3-build20250806
rancher/hardened-cluster-autoscaler:v1.10.2-build20250611
rancher/nginx-ingress-controller:v1.12.4-hardened7
rancher/nginx-ingress-controller:v1.12.4-hardened7
rancher/nginx-ingress-controller:v1.12.4-hardened7
rancher/nginx-ingress-controller:v1.12.4-hardened7
rancher/hardened-k8s-metrics-server:v0.8.0-build20250704
rancher/mirrored-sig-storage-snapshot-controller:v8.2.0
quay.io/metallb/controller:v0.15.2
quay.io/metallb/speaker:v0.15.2
quay.io/metallb/speaker:v0.15.2
quay.io/metallb/speaker:v0.15.2
quay.io/metallb/speaker:v0.15.2
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
quay.io/minio/minio:RELEASE.2024-12-18T13-15-44Z
ghcr.io/open-webui/open-webui:0.6.36
ollama/ollama:0.12.9
ghcr.io/open-webui/pipelines:main
apache/tika:3.2.2.0-full
quay.io/pulp/pulp-minimal:stable
quay.io/pulp/pulp-minimal:stable
docker.io/library/postgres:13
gcr.io/kubebuilder/kube-rbac-proxy:v0.13.0
quay.io/pulp/pulp-operator:v1.1.0
docker.io/library/redis:latest
quay.io/pulp/pulp-web:stable
quay.io/pulp/pulp-minimal:stable
quay.io/cephcsi/ceph-csi-operator:v0.4.0
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
docker.io/rook/ceph:v1.18.2
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
docker.io/rook/ceph:v1.18.2
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
docker.io/rook/ceph:v1.18.2
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/ceph/ceph:v19.2.3
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-provisioner:v5.2.0
registry.k8s.io/sig-storage/csi-resizer:v1.13.2
registry.k8s.io/sig-storage/csi-attacher:v4.8.1
registry.k8s.io/sig-storage/csi-snapshotter:v8.2.1
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-provisioner:v5.2.0
registry.k8s.io/sig-storage/csi-resizer:v1.13.2
registry.k8s.io/sig-storage/csi-attacher:v4.8.1
registry.k8s.io/sig-storage/csi-snapshotter:v8.2.1
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-provisioner:v5.2.0
registry.k8s.io/sig-storage/csi-resizer:v1.13.2
registry.k8s.io/sig-storage/csi-attacher:v4.8.1
registry.k8s.io/sig-storage/csi-snapshotter:v8.2.1
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-provisioner:v5.2.0
registry.k8s.io/sig-storage/csi-resizer:v1.13.2
registry.k8s.io/sig-storage/csi-attacher:v4.8.1
registry.k8s.io/sig-storage/csi-snapshotter:v8.2.1
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
quay.io/cephcsi/cephcsi:v3.15.0
registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.13.0
quay.io/cephcsi/cephcsi:v3.15.0
docker.io/rancher/mirrored-calico-operator:v1.38.3
traefik:v2.9.7
hashicorp/vault:1.20.4
hashicorp/vault-k8s:1.7.0

```
