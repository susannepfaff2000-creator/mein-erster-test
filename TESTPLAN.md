# Testplan: Login-Funktion 

## Ziel
Ich möchte prüfen, ob der Login korrekt funktioniert.

## Testfälle 
1. **Login mit gültigen Daten**
 - **Schritte:** Benutzername und Passwort eingeben
 - **Erwartet:** Anmeldung erfolgreich

2. **Login mit falschem Passwort**
 - **Schritte:** Passwort absichtlich falsch eingeben
 - **Erwartet:** Fehlermeldung „Passwort ungültig“

3.**Login mit Leerem Passwortfeld**
 - **Schritte:** Benutzername eingeben, Passwort Leer Lassen
 - **Erwartet:** Hinweis „Bitte Passwort eingeben“  

4. **Login mit deaktiviertem Benutzerkonto**
 - **Schritte:** Benutzername und Passwort eines deaktivierten Users eingeben
 - **Erwartet:** Hinweis „Konto deaktiviert, bitte Support kontaktieren“
