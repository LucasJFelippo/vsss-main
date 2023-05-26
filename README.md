# vsss-main

## Como utilizar esse repositório

 Você pode utilizar este belo repositório clonando ele para sua maquina. Para isso basta abrir o terminal/cmd, navegar até a pasta aonde você quer que ele seja salvo, e digitar o seguinte comando:

```
git clone https://github.com/lucasdefelippe/vsss-main
```

 Após isso você pode criar teus incriveis códigos no arquivo `main.py`.

 Caso queira programar com mais de um arquivo, criando assim um módulo, você pode criar uma nova pasta *\(recomendo dar um nome que faça sentido para ela, ao em vez de `pasta1`\)*. E após criar o arquivo principal do seu novo módulo, e importa-lo no `main.py`, você pode olhar o lindo módulo `communication` *(que eu criei :sunglasses:)* pra usar de base.

## Usando o módulo Communication

 O módulo de comunicação Communication faz toda a transmição de *data* entre o FiraSim, SSL-Vision, Referee e nosso código. Relaxa, você não precisa se preocupar com nada disso.
 
 Para utiliza-lo basta você importar a *class* **Env** do *path* `communication.main` *\(assim como mostrado na linha 1 do arquivo `main.py`\)*. Bastá agora você instanciar essa classe, na primeira vez que você fizer isso você deve rodar o *method* `buildEnv` para puxar as informações do FiraSim. Você deve chamar ela de novo a cada vez que você quiser que as informações sejam atualizadas *\(normalmente no fim do main loop do seu código\)*.

 <!-- Após isso crie uma instancia dela, você pode dar o nome que quiser para ela *\(linha 3\)*. Essa instancia terá todas as informações que o FiraSim te passará, porem antes de fazer qualquer coisa você deve mandar ela puxar essas informações, para isso basta chamar a função `buildEnv` *\(linha 4\)*. Essa função serve tanto para puxar os dados pela primeira vez, quanto atualiza-los posteriormente. -->

# Coletando Informações
 Para a coleta de informações, a *class* **Env** e seus atributos tem a seguinte estrutura:

 ```
    Env *class*
        BallF *class*
            x *int*
            y *int*
            z *int*
        [RobotF] *array,class*  \\ Array com várias instancias da class RobotF
            id *int*
            team *bool*         \\ True se for time Amarelo / False se for time Azul
            x *int*
            y *int*
            orientation *int*
            vx *int*
            vy *int*
            vorientation *int*
        FieldF *class*
            width *int*
            length *int*
            goal_width *int*
            goal_depth *int*
 ```

# Enviando comandos
 Para enviar comandos, você pode chamar os *method* do próprio objeto que deseja manipular *\(assim como mostrado na linha 9 do arquivo `main.py`\)*. Os metodos de cada *class* são:

 ```
    BallF.replace(x, y, vx = 0, vy = 0)
 ```
 Reposiciona a bola. *X* e *Y* são as novas coordenadas, (0, 0) sendo o centro da arena. *VX* e *VY* são as velocidades da bola em relação a cada eixo, se não informado, é utilizado 0 como valor padrão pra ambas.

 ```
    RobotF.on(left, right)
 ```
 Envia um comando para as rodas do robo, *left* e *right* são as velocidades das rodas esquerda e direita do robo.

 ```
    RobotF.replace(x, y, orientation = 0)
 ```
 Reposiciona o robo. *X* e *Y* são as novas coordenadas, (0, 0) sendo o centro da arena. *Orientation* é a orientação do robo em graus.
