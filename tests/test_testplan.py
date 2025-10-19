from pathlib import Path

def test_testplan_exists():
  """prüft, ob die Datei TESTPLAN.md existiert"""
  assert Path("TESTPLAN.md").exists(), "TESTPLAN.md fehlt!"

def test_testplan_has_sections():
  """Prüft, ob die wichtigstens Überschriften vorhanden sind"""
  text = Path("TESTPLAN.md").read_text(encoding="utf-8")
  assert "# Testplan: Login-Funktion" in text 
  assert "## Ziel" in text 
  assert "## Testfälle" in text 

def test_contains_testcases():
  """prüft, ob mindestens ein Testfall definiert ist"""
  text = PAth("TESTPLAN.md").read_text(encoding="utf-8")
  assert"**Login mit" in text, "Keine Testfälle gefunden!" 
