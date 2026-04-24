# ALIF81_DevOps

```bash
docker build -t py3.14-fastapi .
docker tag 1dsd512s0d antonind5/py3.14-fastapi:1.1
docker push antonind5/py3.14-fastapi:1.1 
docker run -dit -p 8000:8000 antonind5/py3.14-fastapi:latest


```