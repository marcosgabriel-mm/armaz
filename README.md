# 📦 Armaz

Este módulo fornece uma solução para o gerenciamento de estoque e produtos no Odoo, permitindo o controle de quantidades, localizações e valores de forma intuitiva e desacoplada do módulo nativo de inventário.

## 🚀 Funcionalidades Principais

### 1. Gestão de Produtos (`estoque.produto`)
Implementação de um cadastro de produtos independente e personalizado, eliminando a necessidade de dependências complexas. O modelo foi desenhado para ser objetivo, incluindo atributos essenciais como **Código**, **Descrição**, **Categoria** e **Preço Padrão**, garantindo um relacionamento direto e otimizado com os registros de estoque.

Uma regra de negócio foi implementada no campo código, impedindo a inserção de dados duplicados e garantindo a unicidade dos registros através de uma constraint SQL.

>**Melhorias possíveis**: Implementar validação em tempo real no frontend para alertar o usuário antes da tentativa de salvamento, melhorando a experiência do usuário e reduzindo requisições desnecessárias ao servidor.

### 2. Controle de Estoque (`estoque`)
Sistema simplificado para monitoramento de disponibilidade em tempo real. Através de visualizações intuitivas, é possível acompanhar o status de cada item com facilidade.
- **Cálculos Automáticos**: O valor total é atualizado instantaneamente (`Quantidade` × `Preço Unitário`).
- **Indicadores Visuais**:
  - 🟢 **Disponível**: Produtos prontos para movimentação.
  - 🔴 **Fora de Estoque**: Alerta visual para itens indisponíveis.

A quantidade de produtos foi tratada com validação para impedir valores negativos, garantindo a integridade dos dados. O preço total no estoque é calculado automaticamente através de um campo computado (`Quantidade` × `Preço Padrão do Produto`). O sistema também permite alternar o estado de disponibilidade entre 'Disponível' e 'Fora de Estoque', facilitando o controle visual do inventário.

>**Melhorias possíveis**: Implementar um sistema de alertas quando o estoque atingir níveis mínimos configuráveis, adicionar histórico de movimentações para rastreabilidade completa.

## 📂 Estrutura de Menus
A navegação foi projetada para ser direta e eficiente, facilitando o acesso às operações diárias:

- **Estoque PD** (Menu Raiz)
  - **Estoque**: Visão geral e controle de todos os registros de estoque.
  - **Produtos**: Cadastro mestre e gerenciamento de produtos.

## 🛠️ Instalação

1. Coloque a pasta `estoque_pd` no diretório de `addons` do seu Odoo.
2. Reinicie o serviço do Odoo.
3. Ative o **Modo Desenvolvedor**.
4. Vá em **Apps** > **Atualizar Lista de Apps**.
5. Procure por **Estoque** e clique em **Instalar**.

## 📋 Requisitos

- Odoo 19.0+
- Módulo `base` (Nativo)
