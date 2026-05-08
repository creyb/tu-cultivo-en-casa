---
name: hugo-content-generator
description: Cuando el usuario solicita generar un post para Hugo, este skill crea un archivo Markdown con frontmatter válido y estructura SEO consistente.
---

# Skill: Hugo Post Generator

## Objetivo
Generar posts en formato Markdown listos para publicación en Hugo, con estructura SEO consistente y frontmatter válido.

---

## Contexto
Este skill se usa con un sistema basado en Hugo (static site generator) y un LLM local (Ollama) para automatizar la creación de contenido.

---

## Reglas obligatorias

### 1. Formato de salida
Siempre devolver SOLO Markdown válido.

No explicaciones. No comentarios. No texto fuera del bloque.

---

### 2. Frontmatter obligatorio

Todo post debe incluir:

```yaml
---
title: string
date: YYYY-MM-DD
draft: false
categories: [string]
tags: [string]
---