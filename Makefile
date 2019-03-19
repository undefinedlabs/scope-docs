.PHONY: github

github:
	true

docs/release-notes.md docs/ios-release-notes.md docs/python-release-notes.md: github
	./generate-release-notes.py
