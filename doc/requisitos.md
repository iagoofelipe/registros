# Requisitos Funcionais
Requisitos para o desenvolvimento do sistema.

- o sistema deve aceitar a entrada de um [Registro](#registro)
- o sistema deve exibir os [Registros](#registro) feitos durante o mês atual, ou em um intervalo específico
- os [Registros](#registro) feitos em [Cartões](#cartão) entrarão na fatura e serão contabilizados no período vigente do cartão
- o sistema deve permitir o login de um usuário
- um [usuário](#usuário) pode possuir vários [perfis](#perfil), com diferentes níveis de acesso


## Registro
Representa uma operação financeira dentro do sistema.

#### Atributos
- tipo de operação (Entrada | Saída)
- valor
- título
- descrição
- [Categorias](#categoria)
- [Método](#método)

## Categoria
Rótulo utilizado como agrupador de [Registros](#registro).

## Conta
Uma conta bancária, a qual servirá como poupança e vínculo de [Cartões](#cartão).

#### Atributos
- [Cartões](#cartão)

## Cartão
Representação de um cartão de crédito, o qual conterá um conjunto de [Registros](#registro).

Um cartão possui datas de renovação e vencimento, o qual servirá para agrupar registros feitos neste período.

#### Atributos
- [Conta](#conta)
- 4 últimos dígitos (apenas para controle do usuário)
- data renovação
- data vencimento
- [Registros](#registro)

## Método
forma de processamento de um [Registro](#registro).

#### Atributos
- Métodos Entrada:
  - dinheiro | pix: [Registro](#registro) sem [Conta](#conta)
  - depósito: [Registro](#registro) com [Conta](#conta)

- Métodos Saída:
  - saque: [Registro](#registro) com [Conta](#conta)
  - fatura:  [Registro](#registro) feito em um [Cartão](#cartão)

## Usuário
Usuário do sistema, o qual pode realizar login e utilizar recursos do sistema.

Um usuário pode conter um conjunto de [Perfis](#perfil), realizando operações de acordo com seus níveis de acesso.

#### Atributos
- primeiro nome
- último nome
- usuário (cpf)
- senha
- [Perfis](#perfil)

## Perfil
Um perfil é um agrupador de [Registros](#registro) que permite aos usuários acessarem e manipularem, de acordo com suas permissões.

#### Atributos
- nome
- [Regra de Perfil](#regra-de-perfil)

## Regra de Perfil
Representa permissões que um usuário pode ter em um peril.

Esta tabela apresenta uma relação entre uma regra e o que o usuário pode fazer no perfil.

| Regra | Leitura | Escrita | Exclusão | Descrição |
| --- | --- | --- | --- | --- |
| `OWNER` | X | X | X | usuário proprietário do perfil |
| `VIEWER` | X | - | - | visualizador do perfil |
| `WRITER` | - | X | - | editor do perfil |

# Requisitos Não Funcionais

- O sistema deverá operar, em primeiro momento, no sistema operacional Windows.
- O usuário deve autenticar-se utilizando seu cpf e senha previamente cadastrados.