# 🎮 Jogoteca - Sua Biblioteca de Jogos Digital 🕹️

[![GitHub stars](https://img.shields.io/github/stars/ThiagoRodSilva/jogoteca?style=social)](https://github.com/ThiagoRodSilva/jogoteca)
[![GitHub forks](https://img.shields.io/github/forks/ThiagoRodSilva/jogoteca?style=social)](https://github.com/ThiagoRodSilva/jogoteca)
[![GitHub issues](https://img.shields.io/github/issues/ThiagoRodSilva/jogoteca)](https://github.com/ThiagoRodSilva/jogoteca/issues)
[![GitHub license](https://img.shields.io/github/license/ThiagoRodSilva/jogoteca)](https://github.com/ThiagoRodSilva/jogoteca/blob/main/LICENSE)
[![Language](https://img.shields.io/badge/language-Python-blue)](https://github.com/ThiagoRodSilva/jogoteca)

## 📖 Introdução

Bem-vindo ao Jogoteca! Uma aplicação web desenvolvida em Python para organizar e gerenciar sua coleção de jogos favoritos. Com uma interface intuitiva e recursos práticos, o Jogoteca é a solução perfeita para gamers que desejam manter um registro de sua biblioteca de jogos.

## 🔍 Sobre o Projeto

O Jogoteca é uma aplicação web que permite aos usuários criar uma biblioteca pessoal de jogos, incluindo informações como título, gênero, plataforma, status (jogado, jogando, para jogar) e notas pessoais. O projeto foi construído utilizando Python e Flask, com uma estrutura de banco de dados para persistência dos dados.

### 🎯 Objetivo Principal

- Organizar sua coleção de jogos de forma digital
- Facilitar o gerenciamento de jogos por plataforma e status
- Permitir anotações e avaliações pessoais
- Oferecer uma interface amigável para navegação e busca

## ✨ Recursos Principais

- 🎮 Cadastro e gerenciamento de jogos
- 👤 Sistema de usuários com autenticação
- 🔍 Busca e filtragem por diferentes critérios
- 📊 Organização por plataforma e status
- 📝 Sistema de notas e avaliações
- 🖼️ Upload de capas de jogos
- 📱 Interface responsiva

## 🚀 Instalação

Siga estas etapas para instalar e executar o Jogoteca em sua máquina local:

1. **Clone o repositório:**
```bash
git clone https://github.com/ThiagoRodSilva/jogoteca.git
cd jogoteca
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Prepare o banco de dados:**
```bash
python prepara_banco.py
```

5. **Execute a aplicação:**
```bash
python jogoteca.py
```

A aplicação estará disponível em `http://localhost:5000`.

## 💻 Como Usar

1. **Acesse a aplicação:**
   Abra seu navegador e acesse `http://localhost:5000`

2. **Cadastre-se:**
   Crie uma nova conta clicando em "Registrar" no canto superior direito

3. **Adicione jogos:**
   Após o login, clique em "Adicionar Jogo" e preencha as informações solicitadas

4. **Gerencie sua coleção:**
   Use a barra de busca e os filtros para encontrar jogos específicos
   Atualize o status dos jogos e adicione notas pessoais

### Exemplo de Uso

```python
# Exemplo de como adicionar um novo jogo através da interface
- Clique em "Adicionar Jogo"
- Preencha: Nome: "The Witcher 3", Gênero: RPG, Plataforma: PC
- Adicione uma capa do jogo (opcional)
- Clique em "Salvar"
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, siga estas etapas para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Faça commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Contribuição

- Mantenha o código limpo e bem documentado
- Siga o estilo de código existente
- Atualize a documentação conforme necessário
- Teste suas mudanças antes de submeter

## 📄 Licença

Este projeto está sob a licença [LICENSE](LICENSE). Por favor, verifique o arquivo para obter mais informações.

## 📞 Contato

ThiagoRodSilva - trodriguessilva.dev@gmail.com

Link do Projeto: [https://github.com/ThiagoRodSilva/jogoteca](https://github.com/ThiagoRodSilva/jogoteca)
