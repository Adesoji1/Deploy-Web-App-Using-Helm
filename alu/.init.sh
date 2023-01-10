echo "docker build image"
echo "* backend"
docker build -t alux-backend -f flask/
echo "* frontend"
docker build -t alux-frontend -f frontend/

echo "-----------"

echo "docker tag image"
echo "* backend"
docker tab alux-backend:latest adesojialu/alux-backend:latest
echo "* frontend"
docker tab alux-frontend:latest adesojialu/alux-frontend:latest

echo "-----------"

echo "docker push image to registry"
echo "* backend"
docker push adesojialu/alux-backend:latest
echo "* frontend"
docker push adesojialu/alux-frontend:latest

echo "-----------"

echo "apply helm config files"
helm install -f helm/values.yaml alux helm/

echo "-----------"

echo "list helm repo"
helm list

echo "-----------"

echo "show k8s services"
kubectl get po,deploy,svc 


