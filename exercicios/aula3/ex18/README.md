### Exercicio 18 - a), b), c), d), f), i), j)

 - (a) Cria uma Classe `Pessoa`, contendo os atributos encapsulados, com seus respetivos sele-
tores (*getters*) e modificadores (*setters*), e ainda o construtor padrão. Atributos: `nome`;
`endereço`; `telefone`;

 - (b) Implemente o método de classe (`cria_anonimo`) para a classe `Pessoa` que gera uma
instância com o nome="John Doe", endereco="Unknown", telefone="Unknown".

 - (c) Considere, como subclasse da classe `Pessoa` (desenvolvida no exercício anterior) a classe `Fornecedor`. Considere que cada instância da classe `Fornecedor` tem, para além dos
atributos que caracterizam a classe `Pessoa`, os atributos `valor_credito` (correspondente
ao crédito máximo atribuído/admitido pelo fornecedor) e `valor_divida` (montante da
dívida para com o fornecedor). Implemente na classe `Fornecedor`, para além dos usuais
métodos seletores e modificadores, um método `obter_saldo` que devolve a diferença
entre os valores dos atributos `valor_credito` e `valor_divida`. Depois de implementada
a classe `Fornecedor`, crie um programa de teste adequado que lhe permita verificar
o funcionamento dos métodos implementados na classe `Fornecedor` e os herdados da
classe `Pessoa`.

 - (d) Considere, como subclasse da classe `Pessoa`, a classe `Empregado`. Considere que cada
instância da classe `Empregado` tem, para além dos atributos que caracterizam a classe
`Pessoa`, os atributos `codigo_setor`, `salario_base` (vencimento base) e `imposto` (percen-
tagem retida dos impostos). Implemente a classe `Empregado` com métodos seletores e
modificadores e um método `calcular_salario`. Escreva um programa de teste ade-
quado para a classe `Empregado`.

 - (f) Implemente a classe `Operario` como subclasse da classe `Empregado`. Um determinado
operário tem como atributos, para além dos atributos da classe `Pessoa` e da classe
`Empregado`, o atributo `valor_producao` (que corresponde ao valor monetário dos artigos
efetivamente produzidos pelo operário) e `comissao` (que corresponde à percentagem do
`valor_producao` que será adicionado ao vencimento base do operário). Note que deverá
redefinir nesta subclasse o método herdado `calcular_salario` (o salário de um operá-
rio é equivalente ao salário de um empregado usual acrescido da referida comissão).
Escreva um programa de teste adequado para esta classe.

