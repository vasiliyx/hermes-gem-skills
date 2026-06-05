# Hermes Gem Skills

A curated public library of high-value Hermes skills that Vasiliy explicitly selects for sharing.

This repository is intentionally selective: it is **not** a dump of every local Hermes skill. Only skills that Vasiliy asks to publish belong here.

## What belongs here

1. Reusable Hermes `SKILL.md` workflows with clear trigger conditions.
2. Skills that are safe to share publicly: no private paths, tokens, personal data, client data, or hidden operational details.
3. Skills with practical verification steps and pitfalls.
4. Skills that other Hermes users can install or adapt.

## What does not belong here

1. Private or profile-specific memories.
2. Secrets, credentials, API keys, tokens, private chat IDs, internal service URLs.
3. One-off task logs, stale project progress, PR numbers, issue numbers, or temporary instructions.
4. Third-party copyrighted material copied without a compatible license.

## Repository layout

```text
skills/<category>/<skill-name>/SKILL.md   # published skills
proposals/                                # candidate skill briefs before Vasiliy approves publication
docs/                                     # usage and publishing guidance
scripts/validate_skills.py                # lightweight local validator
```

## Install a skill from this repo

Copy a skill folder into your Hermes profile:

```bash
mkdir -p ~/.hermes/skills/<category>
cp -R skills/<category>/<skill-name> ~/.hermes/skills/<category>/
```

Or install a direct raw `SKILL.md` URL if your Hermes build supports it:

```bash
hermes skills install https://raw.githubusercontent.com/vasiliyx/hermes-gem-skills/main/skills/<category>/<skill-name>/SKILL.md
```

Then start a new Hermes session or reload skills.

## Publishing policy

1. Vasiliy selects the skill.
2. Hermes sanitizes it for public sharing.
3. Hermes validates frontmatter and structure.
4. Hermes commits and pushes to this repository.
5. Optional: collaborators can propose additions through pull requests or GitHub issues.

## Current status

No skills have been published yet in this initial scaffold. This prevents accidentally sharing local/private skills before explicit selection.
