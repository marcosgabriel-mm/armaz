# 📦 Estoque PD - Gestão de Estoque Simples

Este módulo fornece uma solução para o gerenciamento de estoque e produtos no Odoo, permitindo o controle de quantidades, localizações e valores de forma intuitiva e desacoplada do módulo nativo de inventário.

## 🚀 Funcionalidades Principais

### 1. Gestão de Produtos (`estoque.produto`)
Implementação de um cadastro de produtos independente e personalizado, eliminando a necessidade de dependências complexas. O modelo foi desenhado para ser objetivo, incluindo atributos essenciais como **Código**, **Descrição**, **Categoria** e **Preço Padrão**, garantindo um relacionamento direto e otimizado com os registros de estoque.

### 2. Controle de Estoque (`estoque`)
Sistema simplificado para monitoramento de disponibilidade em tempo real. Através de visualizações intuitivas, é possível acompanhar o status de cada item com facilidade.
- **Cálculos Automáticos**: O valor total é atualizado instantaneamente (`Quantidade` × `Preço Unitário`).
- **Indicadores Visuais**:
  - 🟢 **Disponível**: Produtos prontos para movimentação.
  - 🔴 **Fora de Estoque**: Alerta visual para itens indisponíveis.

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
