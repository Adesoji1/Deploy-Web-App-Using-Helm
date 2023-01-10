# docker build image
## * backend
docker build -t alux-backend --no-cache -f flask/
## * frontend
docker build -t alux-frontend --no-cache -f frontend/

---

# docker tag image
## * backend
docker tab alux-backend:latest adesojialu/alux-backend:latest
## * frontend
docker tab alux-frontend:latest adesojialu/alux-frontend:latest

---

# docker push image to registry
## * backend
docker push adesojialu/alux-backend:latest
## * frontend
docker push adesojialu/alux-frontend:latest

---

# apply helm config files
helm install -f helm/values.yaml alux helm/

---

# list helm repo
helm list

---

## show k8s services
kubectl get po,deploy,svc 


