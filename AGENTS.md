# Technische und architektonische Leitlinien

## Mission

Dieses Projekt ist ein Open-Source-Werkzeug zum Generieren, Bewerten und automatischen
Vorselektieren hochwertiger Markennamen.

Es ersetzt keine juristische Markenprüfung.

## Langfristige Pipeline

```text
Generate
   ↓
Score
   ↓
Domain Availability
   ↓
GitHub Availability
   ↓
App Store Availability
   ↓
Web Search
   ↓
Trademark Databases
   ↓
Final Report
```

## Projektphilosophie

Dieses Repository verfolgt zwei Ziele:

1. Ein nützliches Werkzeug entwickeln.
2. Ein Referenzprojekt für modernes Python werden.

Prioritäten:

- Lesbarkeit
- Wartbarkeit
- Reproduzierbarkeit
- Korrektheit
- Gute Developer Experience

Keine unnötige Komplexität.

## Architektur

Bevorzugte Struktur:

```text
src/
    brand_name_finder/
        cli.py
        generator.py
        scoring.py
        models.py
        providers/
```

Lieber wenige gut benannte Module als viele kleine Dateien.

## Technologie

Das Projekt verwendet Python 3.13 oder neuer.

Verwendete Werkzeuge:

- uv
- Typer
- Ruff
- mypy
- pytest
- Coverage
- GitHub Actions
- Codespaces
- Dev Containers

Keine zusätzlichen Frameworks ohne klaren Nutzen.

## Codequalität

- Der Code ist vollständig typisiert.
- Ruff ist für Formatierung und Linting maßgeblich.
- mypy soll sauber bleiben.
- Neue Features sollen Tests erhalten.
- Coverage niemals künstlich senken.
- Die CI muss grün bleiben.

## Entscheidungsprinzipien

Wenn mehrere Lösungen möglich sind, bevorzuge diejenige, die

1. leichter lesbar ist,
2. weniger Konzepte einführt,
3. weniger Abhängigkeiten benötigt,
4. einfacher testbar ist und
5. leichter erklärbar ist.

Abstraktionen erst einführen, wenn ein konkreter Bedarf entstanden ist.

Jede zusätzliche Abhängigkeit muss ihren Nutzen rechtfertigen.

## Arbeitsweise

Vor jeder Änderung:

- bestehende Architektur verstehen
- Konsistenz erhalten
- unnötige Refactorings vermeiden
- kleine, klar abgegrenzte Commits bevorzugen
- größere Architekturentscheidungen im Commit erläutern

Nicht vorzeitig optimieren.

Lieber viele kleine Verbesserungen als große Umbauten.

## Leitsatz

> Make the next change the obvious change.
