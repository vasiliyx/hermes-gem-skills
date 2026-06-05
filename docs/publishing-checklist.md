# Publishing Checklist

Before publishing a skill here:

1. Confirm Vasiliy explicitly selected this skill for GitHub sharing.
2. Check `SKILL.md` frontmatter:
   - starts at byte 0 with `---`
   - has `name`
   - has `description`
   - has a non-empty body
3. Remove private data:
   - tokens/API keys/passwords
   - private chat IDs/contact IDs
   - personal addresses/financial/medical data
   - local-only credentials and machine-specific secrets
4. Confirm licensing:
   - original Hermes-authored content is okay
   - third-party material must have compatible license/attribution
5. Add verification steps and common pitfalls.
6. Run:
   ```bash
   python3 scripts/validate_skills.py
   ```
7. Commit with a clear message:
   ```bash
   git add skills/<category>/<skill-name>
   git commit -m "feat: add <skill-name> skill"
   git push
   ```
