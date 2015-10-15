#PROJECT_PATH = "/Users/spanky/Dropbox/if/transhominid/transhominid.inform"
I7_COMPILER = ./i7.osx
#I7_EXTENSION_DIR = ~/Library/Inform/Extensions/
#I7_INTERNAL_PATH = "/Applications/Inform.app/Contents/Resources/Internal"
#I7_EXTERNAL_PATH = "/Users/spanky/Library/Inform"

# Needed because these targets are not actual files
.PHONY: interpreter extensions all
.DEFAULT_GOAL := all

interpreter:
	$(MAKE) -C interpreter/cheapglk
	$(MAKE) -C interpreter/glulxe

extensions:
	rsync -r Untitled.extensions/ $(I7_EXTENSION_DIR)

all: interpreter extensions
	$(I7_COMPILER) -c Untitled.inform

