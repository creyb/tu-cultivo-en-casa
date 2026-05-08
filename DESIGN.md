---
name: Rustic-Urban Garden Journal
colors:
  surface: '#faf9f7'
  surface-dim: '#dadad8'
  surface-bright: '#faf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeec'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1b'
  on-surface-variant: '#434843'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#737872'
  outline-variant: '#c3c8c1'
  surface-tint: '#506354'
  primary: '#334537'
  on-primary: '#ffffff'
  primary-container: '#4a5d4e'
  on-primary-container: '#c0d5c2'
  inverse-primary: '#b7ccb9'
  secondary: '#8b4f35'
  on-secondary: '#ffffff'
  secondary-container: '#ffb192'
  on-secondary-container: '#7a4129'
  tertiary: '#3e4240'
  on-tertiary: '#ffffff'
  tertiary-container: '#565957'
  on-tertiary-container: '#cdd0cd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b7ccb9'
  on-primary-fixed: '#0e1f13'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#ffdbcd'
  secondary-fixed-dim: '#ffb597'
  on-secondary-fixed: '#360f00'
  on-secondary-fixed-variant: '#6e3820'
  tertiary-fixed: '#e1e3e1'
  tertiary-fixed-dim: '#c4c7c5'
  on-tertiary-fixed: '#191c1b'
  on-tertiary-fixed-variant: '#444746'
  background: '#faf9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e3e2e0'
typography:
  display-xl:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1140px
  gutter: 24px
---

## Brand & Style

This design system establishes a bridge between the raw, tactile world of organic gardening and the structured, precise environment of metropolitan living. The brand personality is "The Sophisticated Cultivator"—knowledgeable and professional, yet deeply connected to nature. 

The aesthetic follows a **Tactile-Minimalist** approach. It maintains the high-utility and cleanliness of modern digital interfaces while integrating the warmth of physical materials. We prioritize generous white space to evoke the feeling of an open terrace, balanced with subtle photographic textures of wood grain, weathered clay, and poured concrete. The emotional response should be one of "attainable tranquility"—transforming a chaotic urban balcony into a curated sanctuary.

## Colors

The palette is grounded in three distinct environmental pillars:
- **Moss Green (Primary):** A deep, desaturated green used for navigation, primary actions, and high-level headings. It represents the vitality of the plants themselves.
- **Soft Terracotta (Secondary):** Used for interactive elements like buttons, calls to action, and highlights. This evokes the warmth of clay pots and sun-baked bricks.
- **Urban Grey/Cement (Tertiary):** A cool, neutral grey used for structural elements, borders, and secondary text. It provides the "urban" framework that contains the greenery.

The background uses a warm "Parchment" white (#F9F8F6) instead of pure white to maintain the organic, rustic feel. Darker cement tones are reserved for footer backgrounds and high-contrast UI components.

## Typography

This design system uses a high-contrast typographic pairing to reflect its dual nature:

- **The Rustic:** **Libre Caslon Text** is used for all editorial headings. Its characterful serifs and traditional proportions evoke botanical journals and classical gardening heritage.
- **The Urban:** **Metropolis** is used for body copy, UI labels, and navigation. Its geometric, clean construction ensures maximum readability and a contemporary, "city-ready" feel.

All labels and small metadata should be set in Metropolis All-Caps with increased letter spacing to provide a structured, architectural look to the data.

## Layout & Spacing

The layout follows a **Fixed Grid** system centered on the page, mimicking the deliberate arrangement of a well-planned terrace garden. 

We utilize a 12-column grid for desktop views. Content should feel structured and modular. Large vertical margins (xl) are encouraged between major sections to prevent the "clutter" that often plagues small-space gardening. Negative space is a functional tool here, representing the "breathable air" required in urban environments.

## Elevation & Depth

This design system avoids heavy shadows in favor of **Tonal Layers** and **Subtle Textures**. Depth is created through stacking colors:
- **Level 0 (Base):** The parchment background.
- **Level 1 (Card/Surface):** White or very light cement-toned surfaces.
- **Level 2 (Inlay):** Recessed elements using a 1px border in Moss Green or Urban Grey.

Where depth is absolutely necessary (e.g., modals or floating buttons), we use an **Ambient Shadow**: a very soft, diffused shadow tinted with the primary Moss Green (#4A5D4E) at 8% opacity. This feels more like a natural cast shadow from a leaf or pot rather than a digital effect.

## Shapes

The shape language is **Soft (0.25rem)**. We avoid perfectly circular "pill" shapes and sharp "stark" corners. The goal is to mimic the slightly eased edges of planed wood or weathered stone. 

Image containers should occasionally use asymmetric rounding (e.g., top-left and bottom-right only) to suggest organic, non-linear growth patterns found in nature.

## Components

- **Buttons:** Primary buttons use a solid Moss Green background with white Metropolis text. Secondary buttons use a Soft Terracotta outline with a 1.5px stroke. The hover state should involve a subtle shift in saturation rather than brightness.
- **Cards:** Content cards feature a 1px Urban Grey border. The header image of the card should have no rounding on the bottom, allowing it to "sit" directly on the card's text area like a planter on a ledge.
- **Input Fields:** Use a Cement-toned background with a bottom-only border in Moss Green. This creates a "shelf" look that feels architectural.
- **Chips/Tags:** Used for plant categories (e.g., "Full Sun," "Succulent"). These should use the Soft Terracotta color at 15% opacity with dark terracotta text.
- **Progress Indicators:** For "Growth Trackers" or "Watering Schedules," use a thick, textured bar that mimics the look of soil or wood grain.
- **Dividers:** Use a subtle, dashed line in Urban Grey to denote separation, reminiscent of architectural blueprints or garden site plans.