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
```

> **REGLA CRÍTICA — fecha de publicación**: `date` debe ser **siempre el día en que se hace commit del post**, nunca una fecha futura. El CI de GitHub Pages construye con `hugo --gc --minify --baseURL "https://tucultivoencasa.com/"` (sin `--buildFuture`), por lo que cualquier post con `date` posterior a la fecha del build será **silenciosamente ignorado** y no se publicará hasta un push o trigger futuro. Cuando el usuario pide un artículo, lo quiere publicado **en el momento**, no mañana. Si hoy es `2026-06-10`, entonces `date: 2026-06-10`. Sin excepciones.