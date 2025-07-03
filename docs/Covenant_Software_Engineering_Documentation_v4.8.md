# Covenant Mobile — Software Engineering Documentation v4.8

## Mission

Launch the unstoppable Covenant Mobile agentic swarm with a Kivy-based GUI packaged to Android APK using Buildozer.

## Status
- ✅ Core architecture scaffold committed to GitHub
- ✅ Virtual environment locked and isolated
- ✅ All base agents stubbed out
- ✅ GitHub repo initialized, private
- ✅ Version tracking complete

## Immutable Objectives
- All future changes after v4.8 to go via *patch only* after launch
- No directory or class structure changes before v4.8 is live

## Planned Final Launch Steps

1. **Minimum viable GUI** (`app.py`) with Kivy
   - Simple status panel
   - Test agent activation button
   - Ephemeral console
2. **Test Kivy** in Termux or fallback Linux/WSL
3. **Set up Buildozer** environment for APK
4. **Build the APK**
5. **Deploy to test device**
6. **Run regression smoke test**
   - Ensure all agents initialize
   - Ephemeral store works
   - No code errors
7. **Release candidate** tagged v5
8. **Future changes only via patch branch**

## Project Directories
```
covenant_mobile/
  core/
  agents/
  gui/
  tests/
  utils/
  ephemeral_store/
  workflows/
  docs/
```

## Tools / Stack
- Python 3.12
- Kivy for GUI
- Buildozer for APK packaging
- Pytest for automated tests
- GitHub for version control
- Termux for ephemeral dev environment

## Rally Cry

> **No further structural changes before v4.8 goes live. Patches only afterward.**

👑 Hero of Ancient Grounds, you are unstoppable.

