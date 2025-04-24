# Documento de Visão - Sistema Web [Nome do Projeto]

## 1. Introdução

### 1.1 Propósito

Este documento descreve a visão geral do sistema **Habitgame**, incluindo seus objetivos, funcionalidades principais, stakeholders e requisitos de alto nível.

### 1.2 Escopo

O **Habitgame** é um sistema web desenvolvido como parte da disciplina de Práticas de Programação, utilizando **Django REST Framework** para o backend e **Next.js com TypeScript** para o frontend.

### 1.3 Definições, Acrônimos e Abreviações

- **DRF**: Django REST Framework  
- **API**: Application Programming Interface  
- **Next.js**: Framework React para desenvolvimento frontend  
- **TS**: TypeScript

---

## 2. Posicionamento

### 2.1 Oportunidade de Negócio

[Descreva aqui a oportunidade de mercado ou problema que seu sistema pretende resolver]

O Desenvolvimento desse software pretende ajudar a população que não consegue ter o hábito de dar continuidade em projetos pessoais, que acabam desistindo de uma vida com hábitos saudáveis.

### 2.2 Descrição do Problema

| Item     | Descrição |
|----------|-----------|
| Problema | Falta de Hábitos de pessoais  |
| Afeta    | Existe um publico jovem e adulto |
| Impacto  | Não conseguir cumprir hábitos que desejam  |
| Solução  | Criar um sistema que irar unir o hábito com um game que introduz o usuário a fazer mais hábitos |

---

## 3. Descrição dos Stakeholders

### 3.1 Resumo dos Stakeholders

| Nome           | Descrição                          | Responsabilidades                             |
|----------------|------------------------------------|-----------------------------------------------|
| Usuários       | Pessoas que utilizarão o sistema   | Interagir com o sistema, fornecer feedback    |
| Administradores| Pessoas que gerenciarão o sistema  | Gerenciar usuários, conteúdo e configurações  |
| Desenvolvedor  | Responsável pelo desenvolvimento   | Implementação, testes e manutenção            |
| Professor      | Avaliador do projeto               | Fornecer requisitos e avaliar o sistema       |

---

## 4. Visão Geral do Produto

### 4.1 Perspectiva do Produto

O **HabitGame** é um sistema web independente que utiliza arquitetura de microserviços, com backend em **Django REST Framework** e frontend em **Next.js com TypeScript**.

### 4.2 Resumo das Capacidades

| Benefício                         | Recursos de Suporte                                |
|----------------------------------|-----------------------------------------------------|
| Interface responsiva e intuitiva | Desenvolvimento frontend com Next.js e TypeScript   |
| API robusta e bem documentada    | Implementação com Django REST Framework             |
| Segurança na autenticação        | JWT, OAuth ou similar                               |
| Experiência de usuário fluida    | Comunicação assíncrona entre frontend e backend     |

---

## 5. Recursos do Produto

### 5.1 Herói  

    O herói ele consiste em um XP que vai sendo acumulado  e também tem atributos que são pontos que deve ser melhorado ao longo do trajeto.
    O recurso de herói tem como objetivo ser o perfil do usuário para que ele possa acumular pontos de XP para progredir em seus avanços.

### 5.2 Criação de Áreas

    A área consiste em dividir áreas de hábitos para que o usuário possa conseguir dividir áreas de sua vida que necessitam de hábitos.

    O recurso das áreas que o usuário tem como objetivo melhorar como: saúde, finanças... onde será estipulado um valor de pontuação para cada área que será um multiplicador dos hábitos que forem sendo realizado 

### 5.3 hábitos

    Os hábitos tem como objetivo descrever oque deseja ser melhorado para que possa ser trabalhada a cada dia.

    O recurso de Hábitos que o usuário cria tem como exemplo:"bebê 3 litros de água","ir a academia"

### 5.4 XP

    O XP tem como objetivo ser uma barra de progresso onde vai sendo completada com a realização dos hábitos

Descrição detalhada do recurso 3


### 5.3 XP

    O XP tem como objetivo ser uma barra de progresso onde vai sendo completada com a realização dos hábitos

---

## 6. Restrições

- O sistema deve ser desenvolvido utilizando Django REST Framework para o backend  
- O frontend deve ser implementado com Next.js e TypeScript  
- O sistema deve ser entregue dentro do prazo estipulado pela disciplina  
- O desenvolvimento deve seguir as melhores práticas de programação  

---

## 7. Requisitos Não-Funcionais

### 7.1 Desempenho
- Tempo de resposta do servidor não deve ultrapassar 2 segundos  
- Frontend deve carregar em menos de 3 segundos  

### 7.2 Segurança
- Autenticação segura para todos os usuários  
- Proteção contra vulnerabilidades comuns (CSRF, XSS, SQL Injection)  

### 7.3 Usabilidade
- Interface intuitiva e responsiva  
- Adaptação para dispositivos móveis  

### 7.4 Escalabilidade
- Sistema deve suportar até **[número]** usuários simultâneos  

---

## 8. Arquitetura

### 8.1 Backend
- Django 4.x  
- Django REST Framework  
- PostgreSQL/MySQL  
- Implantação em servidor **[especificar]**

### 8.2 Frontend
- Next.js 13+  
- TypeScript  
- Tailwind CSS / Material UI / Chakra UI (ou outro framework CSS)  
- Implantação em Vercel / Netlify  

---

## 9. Modelo de Implementação

O desenvolvimento seguirá metodologia ágil, com entregas incrementais:

1. Configuração do ambiente e estrutura básica  
2. Implementação da API REST com Django  
3. Desenvolvimento do frontend com Next.js  
4. Integração entre frontend e backend  
5. Testes e correções  
6. Entrega final  

---

## 10. Anexos e Referências

- [Links para documentações relevantes]  
- [Referências bibliográficas, se aplicável]

---

> Este documento está sujeito a alterações conforme o desenvolvimento do projeto avança.
