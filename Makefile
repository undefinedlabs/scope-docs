.PHONY: github

github:
	true

docs/release-notes.md: github
	./generate-release-notes.py > docs/release-notes.md
