#!/usr/bin/env python3
"""Generate README.md for awesome-mac from data/apps.json.

README tables are generated, not hand-edited: edit data/apps.json,
then run this script.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "apps.json")
OUT = os.path.join(ROOT, "README.md")

CATEGORIES = [
    ("productivity", "Productivity", "Launchers, task managers, calendars, and email clients — the apps that run your day."),
    ("developer-tools", "Developer tools", "Editors, database clients, API tools, and diff viewers built for Mac developers."),
    ("utilities-menu-bar", "Utilities & menu-bar tools", "Menu-bar organizers, clipboard managers, automation, and screenshot tools that make macOS better."),
    ("window-management", "Window management", "Snapping, tiling, and workspace tools for people who are done dragging windows around."),
    ("media-design", "Media & design", "Image and video editors, screen recorders, media players, and design tools."),
    ("security-privacy", "Security & privacy", "Password managers, firewalls, malware scanners, and privacy monitors you can trust."),
    ("ai-powered", "AI-powered apps", "AI chat clients, local-model tools, and AI writing/transcription assistants with real Mac apps."),
    ("file-management", "File management", "Alternative file managers, FTP/cloud clients, and file search utilities."),
    ("terminal-shell", "Terminal & shell enhancements", "Terminal emulators, shells, prompts, and multiplexers that make the command line pleasant."),
    ("system-performance", "System & performance", "Menu-bar system monitors, disk cleaners, and battery/fan tools."),
    ("note-taking-writing", "Note-taking & writing", "Notes apps, markdown editors, and writing environments."),
]


def anchor(title):
    return title.lower().replace(" ", "-").replace("&", "").replace("--", "-")


def badge(lic, pricing, native):
    oss = "Yes" if lic != "Commercial" else "No"
    nat = "Yes" if native else "No"
    lp = f"{lic} / {pricing}" if lic != "Commercial" else pricing
    return oss, nat, lp


def main():
    apps = json.load(open(DATA))
    by_cat = {slug: [] for slug, _, _ in CATEGORIES}
    for a in apps:
        by_cat[a["category"]].append(a)

    total = len(apps)
    verified = sum(1 for a in apps if a["verified"])
    oss = sum(1 for a in apps if a["license"] != "Commercial")

    lines = []
    lines.append("# Awesome Mac [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    lines.append("> A curated, verified directory of the **best macOS apps and tools** — open-source, free, and paid, every entry tagged with its license and pricing model.\n")
    lines.append(f"Every entry was checked against its official site, docs, or repo on **2026-10-06**. Entries that could not be verified on an official source carry an honest `verified: false` flag in the machine-readable catalog ([`data/apps.json`](data/apps.json)) instead of a guessed description; license terms are quoted from official repos/pages, never inferred.\n")
    lines.append(f"**{total} apps** across **{len(CATEGORIES)} categories** · {verified} verified · {oss} open-source.\n")
    lines.append("## Contents\n")
    for slug, title, _ in CATEGORIES:
        lines.append(f"- [{title}](#{anchor(title)})")
    lines.append("- [Guides](#guides)")
    lines.append("- [Contributing](#contributing)")
    lines.append("- [License](#license)\n")
    lines.append("---\n")

    for slug, title, blurb in CATEGORIES:
        entries = sorted(by_cat[slug], key=lambda a: a["name"].lower())
        lines.append(f"## {title}\n")
        lines.append(blurb + "\n")
        lines.append("| Name | What it does | License / pricing | Open source? | Native? |")
        lines.append("|---|---|---|---|---|")
        for a in entries:
            oss_yes, nat_yes, lp = badge(a["license"], a["pricing"], a["native"])
            desc = a["description"].replace("|", "\\|")
            lines.append(f"| [{a['name']}]({a['homepage']}) | {desc} | {lp} | {oss_yes} | {nat_yes} |")
        lines.append("")

    lines.append("## Guides\n")
    lines.append("- [Choosing guide](docs/choosing-guide.md) — how to pick apps without installing everything.")
    lines.append("- [Categories](docs/categories.md) — scope notes for each category and how this list differs from OSS-only lists.")
    lines.append("- [Excluded & retired](docs/excluded-and-retired.md) — apps we checked and rejected, with reasons.\n")
    lines.append("## Contributing\n")
    lines.append("See [CONTRIBUTING.md](CONTRIBUTING.md). Add entries to `data/apps.json`, then regenerate this README with `python3 generate_readme.py`.\n")
    lines.append("## License\n")
    lines.append("MIT — see [LICENSE](LICENSE). The listed apps keep their own licenses.\n")

    open(OUT, "w").write("\n".join(lines) + "\n")
    print(f"wrote {OUT}: {total} entries, {verified} verified")


if __name__ == "__main__":
    main()
