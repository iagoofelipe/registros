# Levantamento de Requisitos
Requisitos para o desenvolvimento do sistema.

- o sistema deve aceitar a entrada de um registro
- um registro é um tipo de entrada ou saída, a qual contém:
  - valor
  - título
  - descrição
  - categorias: rótulo que servirá como um agrupador de registros
  - método: [Método](#método)
- uma categoria é apenas um rótulo que servirá como um agrupador de registros
- o sistema deve exibir as entradas e saídas feitas durante o mês atual, ou em um intervalo específico
- o sistema deve exibir os registros feitos
- os registros feitos em [Cartões](#cartão) entrarão na fatura e serão contabilizados no período vigente do cartão

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

## Cartão
Representação de um cartão de crédito, o qual conterá um conjunto de [Registros](#registro).

#### Atributos
- [Conta](#conta)
- 4 últimos dígitos (apenas para controle do usuário)
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
