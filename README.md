# vsss-client package

### Instalação
#todo

#### Exemplo de Uso
#todo
### Arquivo de Configuração
#todo

### Regerando Protos / Ubuntu
Instale o `protobuf-compiler` 
```sh
apt install -y protobuf-compiler
protoc --version #Garanta que a versão seja 3+
```

Compilando protos
```sh
protoc -I=./protos --python_out=./protos ./protos/*.proto
```

