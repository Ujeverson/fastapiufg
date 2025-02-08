# Padrões de Desenvolvimento

## Commits

Utilize o padrão [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>(escopo opcional): <descrição breve>

[Texto opcional explicando o motivo da alteração]
```

### Tipos Comuns de Commits

- **test:** indica qualquer tipo de criação ou alteração de códigos de teste. Exemplo: Criação de testes unitários.
- **feat:** indica o desenvolvimento de uma nova feature ao projeto. Exemplo: Acréscimo de um serviço, funcionalidade, endpoint, etc.
- **refactor:** usado quando houver uma refatoração de código que não tenha qualquer tipo de impacto na lógica/regras de negócio do sistema. Exemplo: Mudanças de código após um code review
- **style:** empregado quando há mudanças de formatação e estilo do código que não alteram o sistema de nenhuma forma.
Exemplo: Mudar o style-guide, mudar de convenção lint, arrumar indentações, remover espaços em brancos, remover comentários, etc..
- **fix:** utilizado quando há correção de erros que estão gerando bugs no sistema.
Exemplo: Aplicar tratativa para uma função que não está tendo o comportamento esperado e retornando erro.
- **chore:** indica mudanças no projeto que não afetem o sistema ou arquivos de testes. São mudanças de desenvolvimento.
Exemplo: Mudar regras do eslint, adicionar prettier, adicionar mais extensões de arquivos ao .gitignore
- **docs:** usado quando há mudanças na documentação do projeto.
Exemplo: adicionar informações na documentação da API, mudar o README, etc.
- **build:** utilizada para indicar mudanças que afetam o processo de build do projeto ou dependências externas.
Exemplo: Gulp, adicionar/remover dependências do npm, etc.
- **perf:** indica uma alteração que melhorou a performance do sistema.
Exemplo: alterar ForEach por while, melhorar a query ao banco, etc.
- **ci:** utilizada para mudanças nos arquivos de configuração de CI.
Exemplo: Circle, Travis, BrowserStack, etc.
- **revert:** indica a reverão de um commit anterior.

Fonte e mais informações: [link](https://medium.com/linkapi-solutions/conventional-commits-pattern-3778d1a1e657)

### Exemplo de Commit
```text
feat(api): endpoint para autenticação
```

## Branches

Use o padrão de **[Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)** para organização das branches:

- **main:** Branch principal, contendo a versão de produção.
- (avaliar) **develop:** Branch de desenvolvimento, contendo as últimas funcionalidades desenvolvidas.

Ao criar uma nova branch, crie com base na branch **main** (avaliar) e siga o padrão de nome:

```
<tipo>/#<id_do_card_no_trelo>-<descrição>
```

### Tipos Comuns de Branches
- **feat:** Para novas funcionalidades
- **fix:** Para correções de bugs
- **hotfix:** Para correções urgentes
- **refactor:** Para refatorações
- **test:** Para criação ou atualização de testes
- **docs:** Para criação ou atualização de documentação

### Exemplo de Nomes de Branches
- `feat/#123-adicionar-autenticacao`
- `fix/#92-corrigir-bug-login`

## Processo de Pull Request

1. Certifique-se de que sua branch está atualizada com a `main` antes de abrir o PR.
2. Adicione uma descrição clara e preencha o template de Pull Request.
3. Adicione uma ou mais pessoas para revisar o PR.

## Pre-Commit: Formatação, estilo e verificação de código

Utilizamos o `.pre-commit-config.yaml` para automatizar verificações de estilo e formatação de código.
A cada novo commit o pre-commit é executado e realiza as verificações e formatações configuradas. Caso alguma verificação falhe, o commit é bloqueado.
Os hooks configurados são:

- **ruff:** Para verificação de linting e formatação de código Python.
- **detect-private-key:** Para detectar chaves privadas adicionadas ao repositório.
- **trailing-whitespace:** Para remover espaços em branco desnecessários.
- **check-docstring-first:** Para garantir que docstrings sejam definidas antes do código.
- **end-of-file-fixer:** Para assegurar que os arquivos terminem com uma nova linha.

Ao clonar o repositório pela primeira vez, instale e configure o pre-commit no seu ambiente local:

```bash
pip install pre-commit
pre-commit install
```

Para executar o pre-commit manualmente em todos os arquivos:

```bash
pre-commit run --all-files
```
