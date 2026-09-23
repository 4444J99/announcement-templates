"""announcement-templates: Template engine and announcement library for distribution.

Part of ORGAN VII (Kerygma) — the marketing and distribution layer
of the eight-organ creative-institutional system.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from kerygma_templates.engine import RenderResult, TemplateEngine
from kerygma_templates.quality_checker import QualityChecker, QualityReport
from kerygma_templates.registry_loader import EventContext, RegistryLoader

__version__ = "0.2.0"


def render_and_check(
    template_id: str,
    channel: str,
    context: dict[str, Any] | None = None,
    templates_dir: Path | str | None = None,
) -> tuple[RenderResult, QualityReport]:
    """Load templates, render a template for a channel, and quality-check the output."""
    if context is None:
        from kerygma_templates.cli import sample_context

        context = sample_context()

    engine = TemplateEngine()
    if templates_dir is not None:
        tdir = Path(templates_dir)
    else:
        from kerygma_templates.cli import _find_templates_dir

        tdir = _find_templates_dir()

    if tdir.is_dir():
        engine.load_directory(tdir)

    result = engine.render(template_id, context, channel)
    checker = QualityChecker()
    report = checker.check(result.text, channel, template_id, result.unresolved_vars)
    return result, report


__all__ = [
    "EventContext",
    "QualityChecker",
    "QualityReport",
    "RegistryLoader",
    "RenderResult",
    "TemplateEngine",
    "render_and_check",
]
