"""Tests for top-level kerygma_templates package exports and render_and_check API."""

from __future__ import annotations

import kerygma_templates
from kerygma_templates import RenderResult, render_and_check
from kerygma_templates.quality_checker import QualityReport


def test_package_exports():
    assert hasattr(kerygma_templates, "TemplateEngine")
    assert hasattr(kerygma_templates, "QualityChecker")
    assert hasattr(kerygma_templates, "QualityReport")
    assert hasattr(kerygma_templates, "RegistryLoader")
    assert hasattr(kerygma_templates, "EventContext")
    assert hasattr(kerygma_templates, "RenderResult")
    assert hasattr(kerygma_templates, "render_and_check")


def test_render_and_check():
    result, report = render_and_check("repo-launch", "mastodon")
    assert isinstance(result, RenderResult)
    assert isinstance(report, QualityReport)
    assert result.template_id == "repo-launch"
    assert result.channel == "mastodon"
    assert len(result.text) > 0
