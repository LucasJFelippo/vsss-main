# vsss-client package

### Instalação
```sh
pip install git+https://github.com/fbot-furg/vsss_api.git
```

#### Exemplo de Uso
```py
from lib import FIRASim , Team, Command

fira = FIRASim()

cmd = Command(Team.BLUE, 1, -10, 10)
cmd = Command(Team.YELLOW, 1, 10, -10)
fira.send_command([cmd])

while True:
    robot = fira.robot(Team.BLUE, 1)
    ball = fira.ball()
    
    print(ball.x, ball.y)
```

### Arquivo de Configuração
`config.ini`
```ini
[FIRA]
vision_address = 224.0.0.1
vision_port = 10002
command_address = 127.0.0.1
command_port = 20011
```

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

