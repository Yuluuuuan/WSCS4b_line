requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f line 1.0.0
	brane remove -f line
	brane build container.yml
	brane push line
