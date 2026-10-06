# Choosing Guide

How to pick apps from this list without installing everything at once.

## Start with the defaults Apple already ships

macOS ships a lot for free: Notes, Reminders, Finder, Terminal, Safari, Mail, Calendar, and the built-in Spotlight search. Start there, and only add an app when you hit a real limitation. Many people never need a window manager beyond Split View, and Notes is genuinely good.

## Decide your budget philosophy up front

This list tags every app's pricing honestly:

- **Open source** — free forever, and you can audit the code. Start here when privacy or cost matters: Rectangle, IINA, Maccy, Ollama.
- **Free / Freemium** — the free tier is real, not a trial. Raycast, Notion, Obsidian, and Warp all do serious work for $0.
- **Paid (one-time)** — often the best value in the Apple ecosystem. Things 3, Pixelmator Pro, CleanShot X, and Keyboard Maestro cost less than a few months of a subscription and are maintained for years.
- **Subscription** — fine for tools you use daily, but audit your stack once a year; subscription creep is the real macOS tax.

## Prefer native when it matters

The `Native` column in the README marks apps built on macOS frameworks (AppKit/SwiftUI/Catalyst). Native apps tend to be faster, use less memory, and respect system behaviors (drag and drop, accessibility APIs, keyboard shortcuts). Electron apps like VS Code and Obsidian are the notable exceptions that earn their weight in other ways.

## Security-sensitive apps: check provenance

For anything touching your password manager, firewall, or camera (see [Security & privacy](../README.md#security--privacy)), prefer open-source tools (LuLu, BlockBlock, OverSight) or long-established vendors. See the exclusions log ([excluded-and-retired.md](excluded-and-retired.md)) for tools we checked and rejected.

## One-at-a-time rule

Install one app per job, use it for a week, then decide. Menu-bar utilities and window managers compound silently — two years of "I'll try this one too" is how you end up with 40 launch agents.
