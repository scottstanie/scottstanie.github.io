.PHONY: cv cv-docx

# Regenerate every CV variant from research/cv.yml
cv:
	python3 research/render_cv.py
	@git --no-pager diff --stat research/ 2>/dev/null || true

# Requires: brew install pandoc
cv-docx: cv
	pandoc research/cv-full.md -o research/cv-full.docx
	pandoc research/cv-industry.md -o research/cv-industry.docx
	@echo "Upload the .docx files to Drive (File > Open > Upload) to refresh the Google Docs."
